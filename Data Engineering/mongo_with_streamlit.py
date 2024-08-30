import streamlit as st
from pymongo import MongoClient

# CRUD functions

client = None
db = None


def connect_to_mongo():
    global client, db
    try:
        client = MongoClient("mongodb://localhost:27017/")
        get_db_name = st.text_input("Database Name")

        # Check if the user has entered a database name
        if get_db_name:
            db_names = client.list_database_names()
            if get_db_name not in db_names:
                st.warning("Database not found. Creating a new database.")
                db = client[get_db_name]
                st.success("Connected to MongoDB.")
            else:
                st.success("Database found and connected.")
                db = client[get_db_name]
        else:
            st.info("Please enter a database name.")
    except Exception:
        st.error("Failed to connect to MongoDB.")


def create_documents(collection_name, document):
    collection = db[collection_name]
    result = collection.insert_one(document)
    st.success(f"Document inserted with ID: {result.inserted_id}")


def read_documents(collection_name):
    collection = db[collection_name]
    documents = collection.find()
    for doc in documents:
        st.json(doc)


def update_document(collection_name, query, new_values):
    collection = db[collection_name]
    result = collection.update_one(query, {"$set": new_values})
    if result.matched_count > 0:
        st.success(
            f"Documents matched: {result.matched_count}, Document modified: {result.modified_count}"
        )
    else:
        st.warning("No documents matched the query.")


def delete_document(collection_name, query):
    collection = db[collection_name]
    result = collection.delete_one(query)
    if result.deleted_count > 0:
        st.success("Document deleted.")
    else:
        st.warning("No documents matched the query.")


# Streamlit UI

st.title("MongoDB CRUD Operations")

connect_to_mongo()

operation = st.sidebar.selectbox(
    "Select Operation", ["Create", "Read", "Update", "Delete"]
)

collection_name = st.text_input("Collection Name")

if operation == "Create":
    document = st.text_area("Document (JSON Format)", height=200)
    if st.button("Create Document"):
        if collection_name and document:
            try:
                document = eval(document)  # Use json.loads(document) for safer parsing
                create_documents(collection_name, document)
            except Exception as e:
                st.error(f"Error Creating Document: {e}")

elif operation == "Read":
    if st.button("Read Documents"):
        if collection_name:
            try:
                read_documents(collection_name)
            except Exception as e:
                st.error(f"Error Reading Documents: {e}")

elif operation == "Update":
    query = st.text_area("Query (JSON Format)", height=100)
    new_values = st.text_area("New Values (JSON Format)", height=100)
    if st.button("Update Document"):
        if collection_name and query and new_values:
            try:
                query = eval(query)  # Use json.loads(query) for safer parsing
                new_values = eval(
                    new_values
                )  # Use json.loads(new_values) for safer parsing
                update_document(collection_name, query, new_values)
            except Exception as e:
                st.error(f"Error Updating Document: {e}")

elif operation == "Delete":
    query = st.text_area("Query (JSON Format)", height=100)
    if st.button("Delete Document"):
        if collection_name and query:
            try:
                query = eval(query)  # Use json.loads(query) for safer parsing
                delete_document(collection_name, query)
            except Exception as e:
                st.error(f"Error Deleting Document: {e}")
