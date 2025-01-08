from flask import Flask, render_template

# Create an instance of the Flask class for our web application
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
