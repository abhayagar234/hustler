from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


random_word = {}
BACKGROUND_COLOR = "#B1DDC6"
df_dict = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    df_dict = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------- SAVE FLASHCARDS ------------------------------- #
def is_known():
    df_dict.remove(random_word)
    data = pd.DataFrame(df_dict)
    print(len(data))
    data.to_csv("words_to_learn.csv", index=False)
    next_flashcard()


# ---------------------------- SHOW ANSWER ------------------------------- #
def show_answer():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_word["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ---------------------------- NEXT FLASHCARD ------------------------------- #
def next_flashcard():
    global random_word, flip_timer
    window.after_cancel(flip_timer)

    random_word = random.choice(df_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_word["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=next_flashcard)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(
    padx=50, pady=50, bg=BACKGROUND_COLOR
)  # padding x and y and background color

flip_timer = window.after(3000, func=show_answer)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(
    file="/Users/Abhay/hustler/hustler/Python/100_days_of_code/capstone_project_2/images/card_front.png"
)
card_back_img = PhotoImage(
    file="/Users/Abhay/hustler/hustler/Python/100_days_of_code/capstone_project_2/images/card_back.png"
)
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text=" ", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text=" ", font=("Ariel", 60, "bold"))
cross_image = PhotoImage(
    file="/Users/Abhay/hustler/hustler/Python/100_days_of_code/capstone_project_2/images/wrong.png"
)
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_flashcard)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(
    file="/Users/Abhay/hustler/hustler/Python/100_days_of_code/capstone_project_2/images/right.png"
)
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_flashcard()


window.mainloop()
