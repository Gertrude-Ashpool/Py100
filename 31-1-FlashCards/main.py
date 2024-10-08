from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ------------------------------ SAVE PROGRESS ---------------------------------------------

to_learn = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ------------------------------ GENERATE CARD ---------------------------------------------------


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(vocabulary_text, text=french_word, fill="black")
    flip_timer = window.after(3000, flip_card)

# ------------------------------ FLIP CARD ---------------------------------------------------


def flip_card():
    english_word = current_card["English"]
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(vocabulary_text, text=english_word, fill="white")

# ------------------------------ UI SETUP ----------------------------------------------------


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)
window.config(background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
vocabulary_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.config(background=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# X Button
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# Check Button
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
