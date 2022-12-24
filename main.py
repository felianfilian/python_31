from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_01 = ("Arial", 40, "italic")
FONT_02 = ("Arial", 60, "bold")

data = pandas.read_csv("data/french_words.csv").to_dict()
print(data)

def next_card():
    pass


window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=FONT_01)
canvas.create_text(400, 250, text="word", font=FONT_02)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
check_button = Button(image=right_image, command=next_card)
check_button.grid(row=1, column=0)

cross_image = PhotoImage(file="images/wrong.png")
cancel_button = Button(image=cross_image, command=next_card)
cancel_button.grid(row=1, column=1)

window.mainloop()


