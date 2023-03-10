import random
from tkinter import *
from tkinter import messagebox

import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_01 = ("Arial", 40, "italic")
FONT_02 = ("Arial", 60, "bold")

chosen_word = {}

def right_answer():
    to_learn.remove(chosen_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/to_learn.csv", index=False)
    next_card()


def next_card():
    global chosen_word
    global flip_timer
    window.after_cancel(flip_timer)
    chosen_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=chosen_word["French"], fill="black")
    canvas.itemconfig(card_background, image=card_bg_front)
    flip_timer = window.after(3000, show_back)

def show_back():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=chosen_word["English"], fill="white")
    canvas.itemconfig(card_background, image=card_bg_back)

window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    data = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    messagebox.showinfo(title="New File", message="No File found.\nNew file created!")
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

flip_timer = window.after(3000, show_back)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_bg_front = PhotoImage(file="images/card_front.png")
card_bg_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_bg_front)
card_title = canvas.create_text(400, 150, text="Title", font=FONT_01)
card_word = canvas.create_text(400, 250, text="word", font=FONT_02)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
check_button = Button(image=right_image, command=right_answer)
check_button.grid(row=1, column=0)

cross_image = PhotoImage(file="images/wrong.png")
cancel_button = Button(image=cross_image, command=next_card)
cancel_button.grid(row=1, column=1)


next_card()

window.mainloop()


