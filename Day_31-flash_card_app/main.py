from tkinter import *
import pandas
import random

try:
    words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv("data/french_words.csv")
word_dict = words.to_dict(orient="records")

def familier():
    item = canvas.itemcget(word_label, 'text')
    for word_key in word_dict:
        if word_key["French"] == item:
            word_dict.remove(word_key)
    words_to_learn = word_dict
    words_to_learn = pandas.DataFrame(words_to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    display_french()

def display_english(word_key):
    word = word_key["English"]
    canvas.itemconfig(front, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word_label, text=word, fill="white")

def display_french():
    global change
    root.after_cancel(change)
    word_key = random.choice(word_dict)
    word = word_key["French"]
    canvas.itemconfig(front, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word_label, text=word, fill="black")
    change = root.after(3000, display_english, word_key)


root = Tk()

root.title("Flashy")
change = root.after(3000, display_english)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

front = canvas.create_image(400, 275, image=card_front)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 256, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, padx=50, pady=0)

right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

right_button = Button(image=right, highlightthickness=0, command=familier)
right_button.grid(row=1, column=0, padx=50, pady=10)

wrong_button = Button(image=wrong, highlightthickness=0, command=display_french)
wrong_button.grid(row=1, column=1, padx=50, pady=10)

display_french()

root.mainloop()
