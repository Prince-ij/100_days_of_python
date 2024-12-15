from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter = [random.choice(letters) for _ in range(nr_letters)]
    symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    number = [random.choice(numbers) for _ in range(nr_numbers)]

    passwd = letter + number + symbol

    random.shuffle(passwd)
    passwd = "".join(passwd)

    passwd_entry.insert(0, passwd)
    pyperclip.copy(passwd)

    gen_passwd = Button(text="Regenerate Password", command=re_generate_password)
    gen_passwd.grid(row=3, column=2)

def re_generate_password():
    passwd_entry.delete(0, END)
    generate_password()
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get()
    email = email_entry.get()
    passwd = passwd_entry.get()

    if not (passwd and website):
        messagebox.showinfo(title="Warning", message="Do not leave any field blank")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Your Details:\nEmail: {email}\n"
                                    f"Password: {passwd}\n Save Details ?")

        new_data = f"{website}  | {email}   | {passwd}\n"

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(new_data)

            web_entry.delete(0, END)
            email_entry.delete(0, END)
            passwd_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Password Manager")
root.config(height=400, width=400)
root.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email = Label(text="Email/Username: ")
email.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "prince_ij@gmail.com")

passwd = Label(text="Password: ")
passwd.grid(row=3, column=0)

passwd_entry = Entry(width=21)
passwd_entry.grid(row=3, column=1)

gen_passwd = Button(text="Generate Password", command=generate_password)
gen_passwd.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)



root.mainloop()
