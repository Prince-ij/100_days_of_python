from tkinter import *
from PIL import Image, ImageTk
import math
import home
WIN='orange'
LOSE='yellow'

class Result:
    def __init__(self, res, level, speed, accuracy):
        self.root = Tk()
        self.root.config(padx=20, pady=20)
        self.root.state('zoomed')
        if res == 'win':
            self.root.title('Results')
            self.root.config(bg=WIN)

            self.left_margin = Label(width=50, bg=WIN)
            self.left_margin.grid(row=0, column=0)

            self.message = Label(text='Congratulations', bg=WIN, font=('Comic M Sans', 35, 'bold'))
            self.message.grid(row=0, column=2)

            self.space1 = Label(width=50, bg=WIN)
            self.space1.grid(row=1, column=2)

            img = Image.open('trophy.png')

            self.pic = ImageTk.PhotoImage(img.resize((400, 400)))

            self.trophy = Label(image=self.pic)
            self.trophy.grid(row=2, column=2, rowspan=4)

            self.typing_info = Label(text=f'Typing Speed\n\n{speed} WPM\n\n\nAccuracy\n\n{math.floor(accuracy)}%')
            self.typing_info.config(font=('Georgia', 17, 'bold'), bg=WIN)
            self.typing_info.grid(row=3, column=5)

            self.space2 = Label(width=50, bg=WIN)
            self.space2.grid(row=7, column=2)


            self.show_level = Label(text=f'You are a Typing {level.capitalize()}.', bg=WIN, font=('TImes New Roman', 25, 'italic'))
            self.show_level.grid(row=8, column=2)


            if level == 'Typing Master':
                self.next_level = Button(text='Back to Home', width=20, bg='#3366ff', command=self.start_page)
                self.next_level.grid(row=10, column=3)
            else:
                self.next_level = Button(text='Next Level', width=20, bg='#3399ff', command=self.start_page)
                self.next_level.grid(row=10, column=3)

        else:
            self.root.title('Results')
            self.root.config(bg=LOSE)

            self.left_margin = Label(width=50, bg=LOSE)
            self.left_margin.grid(row=0, column=0)

            self.message = Label(text='OOPS, What a big LOser', bg=LOSE, font=('Comic M Sans', 35, 'bold'))
            self.message.grid(row=0, column=2)

            self.space1 = Label(width=50, bg=LOSE)
            self.space1.grid(row=1, column=2)

            img = Image.open('loser.png')

            self.pic = ImageTk.PhotoImage(img.resize((400, 400)))

            self.trophy = Label(image=self.pic)
            self.trophy.grid(row=2, column=2, rowspan=4)

            self.typing_info = Label(text=f'Typing Speed\n\n{speed} WPM\n\n\nAccuracy\n\n{math.floor(accuracy)}%')
            self.typing_info.config(font=('Georgia', 17, 'bold'), bg=LOSE)
            self.typing_info.grid(row=3, column=5)

            self.space2 = Label(width=50, bg=LOSE)
            self.space2.grid(row=7, column=2)

            self.show_level = Label(text=f'You are a LOSER !!!.', bg=LOSE, font=('TImes New Roman', 25, 'italic'))
            self.show_level.grid(row=8, column=2)


            self.retry = Button(text='Retry', width=20, bg='#33ff33', command=self.start_page)
            self.retry.grid(row=10, column=3)


        self.root.mainloop()

    def start_page(self):
        self.root.destroy()
        home.GUI()