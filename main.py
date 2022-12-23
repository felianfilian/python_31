from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_01 = ("Arial", 24, "bold")

window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0)

# label_01 = Label(text="Flashcards", font=FONT_01)
# label_01.grid(row=0, column=1)

window.mainloop()


