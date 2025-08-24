from tkinter import *
from typer import Typer

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('700x800')
        self.root.config(bg='#f234ff', padx=50, pady=10)
        self.root.title('Typing Master 🖋')
        self.root.state('zoomed')


        self.header = Label(text='Typing Master 🖋', font=('Comic M Sans', 40, 'bold'))
        self.header.config(padx=10, pady=20, bg='#f234ff', fg='white')
        self.header.pack()

        self.subheader = Label(text='Welcome to Typing Master, test your typing skills and see your level.',
                               font=('Arial', 22, 'normal'))
        self.subheader.config(padx=10, pady=10, bg='#f234ff', fg='white')
        self.subheader.pack()

        self.choose = Label(text='Pick a level (by clicking on the corresponding circle)')
        self.choose.config(fg='#ffffff', bg='#f234ff', pady=30, font=('Comic M Sans', 16, 'bold'))
        self.choose.pack()

        self.canvas = Canvas(height=400, width=600)
        self.canvas.pack()

        self.ncircle = self.circle(self.canvas, 100, 50, 30, fill='orange')
        self.novice = self.canvas.create_text(100, 100, text='Typing Novice',
                                              font=('Comic M Sans', 18, 'normal'))
        self.canvas.tag_bind(self.ncircle, '<Button-1>', lambda event: self.activate(event, 'novice'))

        self.jcircle = self.circle(self.canvas, 300, 50, 30, fill='#0000ff')
        self.canvas.tag_bind(self.jcircle, '<Button-1>', lambda event: self.activate(event, 'junior'))
        self.junior = self.canvas.create_text(300, 100, text='Typing Junior',
                                              font=('Comic M Sans', 18, 'normal'))

        self.scircle = self.circle(self.canvas, 500, 50, 30, fill='purple')
        self.canvas.tag_bind(self.scircle, '<Button-1>', lambda event: self.activate(event, 'senior'))
        self.senior = self.canvas.create_text(500, 100, text='Typing Senior',
                                              font=('Comic M Sans', 18, 'normal'))

        self.kcircle = self.circle(self.canvas, 100, 170, 30, fill='#ff0000')
        self.canvas.tag_bind(self.kcircle, '<Button-1>', lambda event: self.activate(event, 'king'))
        self.king = self.canvas.create_text(100, 230, text='Typing King',
                                            font=('Comic M Sans', 18, 'normal'))

        self.ecircle = self.circle(self.canvas, 300, 170, 30, fill='brown')
        self.canvas.tag_bind(self.ecircle, '<Button-1>', lambda event: self.activate(event, 'emperor'))
        self.emperor = self.canvas.create_text(300, 230, text='Typing Emperor',
                                               font=('Comic M Sans', 18, 'normal'))

        self.saintc = self.circle(self.canvas, 500, 170, 30, fill='#33aaff')
        self.canvas.tag_bind(self.saintc, '<Button-1>', lambda event: self.activate(event, 'saint'))
        self.saint = self.canvas.create_text(500, 230, text='Typing Saint',
                                             font=('Comic M Sans', 18, 'normal'))

        self.mcircle = self.circle(self.canvas, 300, 300, 30, fill='grey')
        self.canvas.tag_bind(self.mcircle, '<Button-1>', lambda event: self.activate(event, 'master'))
        self.master = self.canvas.create_text(300, 350, text='Typing Master',
                                              font=('Comic M Sans', 18, 'normal'))


        self.root.mainloop()

    def circle(self, canvas, x, y, r, **kwargs):
        self.id = canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)
        return self.id

    def activate(self, event, level=None):
        self.root.destroy()
        Typer(level)
