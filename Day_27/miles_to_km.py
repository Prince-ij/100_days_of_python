from tkinter import *

def calculate():
    mile = float(input.get())
    kilometer = round(mile * 1.609);
    km.config(text=str(kilometer))

root = Tk()
root.minsize(width=500, height=400)
root.title("Miles to Km Converter")

input = Entry()
input.grid(row=1, column=2)

miles = Label(text="Miles")
miles.grid(row=1, column=3)

equals = Label(text="is equal to")
equals.grid(row=2, column=1)

km = Label(text="0")
km.grid(row=2, column=2)

km_str = Label(text="Km")
km_str.grid(row=2, column=3)

button = Button(text="Calculate", command=calculate)
button.grid(row=3, column=2)

root.mainloop()
