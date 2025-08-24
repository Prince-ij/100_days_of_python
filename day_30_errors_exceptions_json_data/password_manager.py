from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD FINDER------------------------------- #

def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(message="No Data File Found!")
    else:
        web_name = website_entry.get()
        if web_name not in data:
            messagebox.showerror(message="No details for the website exists")
        else:
            email = data[web_name]['email']
            password = data[web_name]['password']

            message = f"\nEmail: {email}\nPassword: {password}"

            messagebox.showinfo(title="Details: ", message=message)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website : {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(bg="#32ffee", pady=30, padx=30)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:", bg="#32ffee")
website_label.grid(row=1, column=0, pady=10)
email_label = Label(text="Email/Username:", bg="#32ffee")
email_label.grid(row=2, column=0, pady=10)
password_label = Label(text="Password:", bg="#32ffee")
password_label.grid(row=3, column=0, pady=10)

#Entries
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1, pady=10)
website_entry.focus()

search_button = Button(text="search", width=25, command=find_password)
search_button.grid(row=1, column=2, pady=10)
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2, pady=10)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1, pady=10)

# Buttons
generate_password_button = Button(text="Generate Password", width=25, command=generate_password)
generate_password_button.grid(row=3, column=2, pady=10)
add_button = Button(text="Add", width=50, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
