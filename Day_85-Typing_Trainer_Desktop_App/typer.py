from data import data, WPM
from tkinter import *
from result import Result
from random import choice


class Typer:
    def __init__(self, level):
        self.root = Tk()
        self.root.title('Show me your skills')
        self.root.config(padx=400, pady=20, bg='#0D1117')
        self.root.state('zoomed')
        self.secs = 59
        self.mins = 0
        self.accuracy = None
        self.speed = None
        self.res = None
        self.current_level = level
        self.text = choice(data[self.current_level])

        self.timer = Label(text=f'{self.mins:02d} : {self.secs:02d}', pady=10, bg='#0D1117', fg='white',
                           font=('Arial', 25, 'normal'))
        self.timer.grid(row=1, column=1)

        self.level = Label(text=f'Level: Typing {self.current_level.capitalize()}', pady=10, bg='#0D1117', fg='#ffddff',
                           font=('Times New Roman', 16, 'normal'))
        self.level.grid(row=1, column=4)

        self.text_c = Canvas(width=500, height=300, highlightthickness=0)
        self.text_c.config(bg='ivory')
        self.text_c.grid(row=2, column=1, columnspan=4)


        self.space = Canvas(width=500, height=15, bg='#0D1117', highlightthickness=0)
        self.space.grid(row=3, column=1, columnspan=4)


        self.enter_box = Text(width=60, height=10, pady=10)
        self.enter_box.grid(row=4, column=1, columnspan=4)

        self.space = Canvas(width=500, height=15, bg='#0D1117', highlightthickness=0)
        self.space.grid(row=5, column=1, columnspan=4)

        self.start_button = Button(text='start', width=20, borderwidth=15, bg='#00ff12', command=self.text_paste)
        self.start_button.grid(row=6, column=3)


        self.root.mainloop()

    def text_paste(self):
        self.start_button.destroy()
        self.text_c.create_text(250, 150, text=self.text,
                              font=('Arial', 14, 'normal'),
                              width=450,
                              justify='left'
                              )
        self.start()

    def start(self):
        if self.mins == 0 and self.secs == 0:
            typed_words = self.enter_box.get('1.0', END)
            actual_words = self.text
            num_of_words = len(typed_words.split(' '))
            self.speed = num_of_words
            num_of_correct = 0
            for i in range(len(typed_words)):
                if typed_words[i] == actual_words[i]:
                    num_of_correct += 1
            self.accuracy = (num_of_correct / len(typed_words)) * 100
            if self.speed >=  WPM[self.current_level] and self.accuracy > 89:
                self.res = 'win'
            else:
                self.res = 'lose'
            self.root.destroy()
            Result(self.res, self.current_level, self.speed, self.accuracy)
            return

        if self.secs == 0 and self.mins > 0:
            self.mins -= 1
            self.secs = 59
        else:
            self.secs -= 1

        self.timer.config(self.timer, text=f'{self.mins:02d} : {self.secs:02d}')


        self.root.after(1000, self.start)