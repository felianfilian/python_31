from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_01 = ("Arial", 24, "bold")

window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=800, height=600)

label_01 = Label(text="Flashcards", font=FONT_01)
label_01.grid(row=0, column=1)

window.mainloop()


