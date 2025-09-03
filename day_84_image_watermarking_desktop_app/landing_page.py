from tkinter import *
from edit import Edit


class LandingPage:
    def __init__(self):
        self.root = Tk()
        self.root.config(height=500, width=600, pady=20, padx=20, bg='orange')
        self.root.title('Brandify App')
        self.header = Label(text='Brandify App', font=('Arial', 56, ('bold', 'italic')), highlightthickness=0, fg='yellow', bg='orange')
        self.header.pack(padx=20, pady=20)
        self.sub_heading = Label(text='Add Watermarks to your Images easily. Establish your brand with Brandify',
                                 font=('Arial', 23, 'normal'), fg='white', bg='orange')
        self.sub_heading.pack(padx=20, pady=20)
        self.watermark_image = PhotoImage(file='watermark_bg.png')
        self.image = Label(image=self.watermark_image)
        self.image.pack()

        self.start_button = Button(
            text='Start Now',
            width=20,
            font=('Arial', 23, 'bold'),
            fg='red',
            bg='pink',
            command=self.edit_page
        )
        self.start_button.pack(padx=40, pady=40)


        self.root.mainloop()

    def edit_page(self):
        self.root.destroy()
        self.root = Edit()

