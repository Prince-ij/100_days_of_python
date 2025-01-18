from tkinter import *
from data import Data

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.config(padx=20, pady=20, bg='green', width=400, height=400)
        self.img = PhotoImage(file='image.png')
        background_label = Label(self.root, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.root.title('Ij\'s Flight Club')

        self.header = Label(text='Ij\'s Flight Club', font=('Arial', 34, 'bold'), fg='green', highlightthickness=0)
        self.header.pack(padx=20, pady=20)
        self.subheader = Label(text='Welcome to My Flight Club!\n Here we find the cheapest Flights',\
                                font=('Arial', 14), fg='green', highlightthickness=0)
        self.subheader.pack(padx=20, pady=20)


        self.name = Entry(width=30)
        self.name.pack(padx=20, pady=10)
        self.name.focus()
        self.name.insert(0, 'Name')
        self.email = Entry(width=30)
        self.email.pack(padx=20, pady=10)
        self.email.insert(0, 'Email')

        self.validate_email = Entry(width=30)
        self.validate_email.pack(padx=20, pady=10)
        self.validate_email.insert(0, 'Re-Enter Email')

        self.get_flights = Button(text='Get Flights', command=self.get_flights)
        self.get_flights.pack(padx=20, pady=10)

        self.root.mainloop()

    def get_flights(self):
        email = self.email.get()
        email2 = self.validate_email.get()
        name = self.name.get()

        if email != email2:
            self.email.delete(0, END)
            self.email.insert(0, 'Emails do not match')
            self.email.config(fg='red')
            self.root.after(3000, lambda: self.email.config(fg='black'))
            self.validate_email.delete(0, END)
            self.validate_email.insert(0, 'Emails do not match')
            self.validate_email.config(fg='red')
            self.root.after(3000, lambda: self.validate_email.config(fg='black'))
            return

        if '@' not in email or '.' not in email:
            self.email.delete(0, END)
            self.email.insert(0, 'Invalid Email')
            self.email.config(fg='red')
            self.root.after(3000, lambda: self.email.config(fg='black'))
            return

        data = Data()
        data.post_customer(name, email)
        
        self.root.destroy()
        self.root = Tk()
        self.root.config(padx=20, pady=20, bg='cyan', width=400, height=400, background='green')
        self.root.title('Ij\'s Flight Club')
        self.img = PhotoImage(file='image.png')
        background_label = Label(self.root, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.label = Label(text=f'Hello {name}!\nWelcome to the Club \nWe will send you the best flight deals to {email}',\
                            font=('Arial', 24), fg='green', highlightthickness=0)
        self.label.pack(padx=20, pady=20, fill='both', expand=True)
