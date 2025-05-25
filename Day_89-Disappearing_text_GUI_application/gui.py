from idlelib.configdialog import font_sample_text
from tkinter import *

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('Disappearing text app')
        self.root.geometry('900x700')
        self.root.config(padx=30, pady=30)

        self.count = 5


        self.header = Label(text='Disappearing Text', font=('Arial', 45, 'bold'))
        self.header.pack()

        self.info = Label(text='Start Typing , Once you stop for 5 secs, You lose your work.',
                          font=('Comic Mono Sans', 12, 'normal')
                          )
        self.info.pack()

        self.timer = Label(text=f'Timer: 0{self.count}', font=('Georgia', 15, 'bold'))
        self.timer.config(fg='red')
        self.timer.pack()

        self.start_button = Button(text='Start', borderwidth=10, fg='#ad00FF', command=self.start)
        self.start_button.place(x=900, y=80)

        self.text_space = Text(borderwidth=5, bg='gray', fg='white',
                               font=('times', 15, 'bold'), padx=10, pady=10)

        self.text_space.pack()

        self.text_space.bind('<Key>', self.reset)


        self.root.mainloop()

    def start(self):
        self.text_space.focus_set()
        self.start_button.destroy()
        self.count -= 1
        self.timer.config(text=f'Timer: 0{self.count}')
        if self.count > 0:
            self.root.after(1000, self.start)
        else:
            self.root.destroy()

    def reset(self, event):
        self.count = 6


