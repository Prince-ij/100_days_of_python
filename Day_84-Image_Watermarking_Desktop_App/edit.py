from tkinter import *
from tkinter import colorchooser, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageEnhance
from io import BytesIO

class Edit:
    def __init__(self):
        self.root = Tk()
        self.root.title('Add Watermark')
        self.root.config(height=500, width=800, bg='ivory')

        self.add_text_btn = Button(text='Add Text', width=15, command=self.add_text)
        self.add_text_btn.place(x=30, y=40)
        self.text_var = StringVar()
        self.text = None
        self.logo = None
        self.background = None

        self.add_logo_btn = Button(text='Add Logo', width=15, command=self.add_logo)
        self.add_logo_btn.place(x=300, y=40)
        self.canvas = Canvas(width=500, height=400, bg='gray')

        self.upload_btn = Button(text='📤 Upload Image',
                                 height=2,
                                 width=30,
                                 command=self.upload_image).place(x=160, y=280)

        self.canvas.place(x=30, y=100)
        self.change_pic = Button(text='Change Photo', width=10, command=self.upload_image)
        self.change_pic.place(x=20, y=510)
        save = Button(text='save', command=self.save)
        save.place(x=520, y=510)


        self.root.mainloop()

    def add_logo(self):
        if self.background:
            self.im_x = 250
            self.im_y = 220

            if not self.logo:
                self.upload_logo()

                for labels in self.root.place_slaves():
                    if (labels.place_info()["anchor"]) == 'w':
                        labels.place_forget()

                self.img_size = Scale(from_=10, to=150, orient='horizontal', label='Resize Image Ratio',
                                      sliderlength=20, length=150, command=self.resizing_image)

                self.img_size.set(40)
                self.img_size.place(anchor='w', x=600, y=180)

                self.brightness = Scale(from_=0.1, to=2.0, orient='horizontal', label='Brightness', digits = 3, resolution = 0.01,
                                        troughcolor='#FFFF00', sliderlength=20, length=150, command=self.brighten)
                self.brightness.set(1)

                self.brightness.place(anchor='w', x=600, y=240)

                self.sharpness = Scale(from_=-0.1, to=2.0, orient='horizontal', label='Sharpness', digits = 3, resolution = 0.01,
                                       troughcolor='#DC143C', sliderlength=20, length=150, command=self.sharpen)
                self.sharpness.set(1)
                self.sharpness.place(anchor='w', x=600, y=300)


                self.contrast = Scale(from_=0.1, to=2.0, orient='horizontal', label='Contrast', digits = 3, resolution = 0.01,
                                    troughcolor='#36454F', sliderlength=20, length=150, command=self.contrasting)
                self.contrast.set(1)
                self.contrast.place(anchor='w', x=600, y=360)

                self.canvas.bind('<B1-Motion>', self.relocate_img)

            else:
                messagebox.showinfo('limited version', 'Sorry , this is a limited version, '
                                                       'you only have one text and logo to add')
        else:
            messagebox.showerror("showerror", "Upload Image First !")


    def add_text(self):
        # check for background

        if self.background:

            # checks if text already exists on screen
            if not self.text:

                # clears previous labels at that position
                for labels in self.root.place_slaves():
                    if (labels.place_info()["anchor"]) == 'w':
                        labels.place_forget()

                # defining the variables for changing the text
                self.size = 14
                self.sizing = Scale(from_=1, to=72, orient='horizontal', label='Font Size',
                                    sliderlength=20, length=150,)
                self.sizing.set(self.size)

                self.sizing.bind('<ButtonRelease-1>', self.update_text)
                self.sizing.place(anchor='w', x=600, y=240)

                self.text_var = StringVar()
                self.text = Entry(textvariable=self.text_var)
                self.text.insert(0, 'Enter Text Here')
                self.text.bind('<ButtonRelease>', self.update_text)
                self.text.place(anchor='w', x=600, y=180)


                self.font = StringVar()
                self.font.set('Times New Roman')
                self.fonting = OptionMenu(self.root, self.font,'Arial', 'Times New Roman', 'Comic Sans MS',
                                          'Courier New', 'Impact', 'Georgia', command=self.update_text)
                self.fonting.place(anchor='w', x=600, y=300)

                self.color_btn = Button(text='Color', command=self.color_picker)
                self.color_btn.place(anchor='w', x=600, y=360)

                self.style = StringVar()
                self.style.set('normal')
                self.styling = OptionMenu(self.root, self.style, 'normal', 'bold', 'italic', command=self.update_text)
                self.styling.place(anchor='w', x=600, y=420)

                self.color = '#000000'
                self.x = 250
                self.y = 220

                # creating the text using canvas
                self.text = self.canvas.create_text(self.x, self.y, text=self.text_var.get(), font=(self.font.get(), self.size,
                                                                                              self.style.get()), fill=self.color)

                self.canvas.bind('<B1-Motion>', self.move_text)
            else:
                messagebox.showinfo('limited version', 'Sorry , this is a limited version, '
                                                       'you only have one text and logo to add')
        else:
            messagebox.showerror('showerror', 'Image must be Uploaded First !')

    def color_picker(self):
        # method for choosing color oof text
        self.color = colorchooser.askcolor(title="Pick Colour")[1]
        self.canvas.delete(self.text)
        self.text = self.canvas.create_text(self.x, self.y, text=self.text_var.get(),
                                            font=(self.font.get(), self.sizing.get(),
                                                  self.style.get()), fill=self.color)


    def upload_image(self):
        # re-initialize variables

        self.text = None
        self.logo = None
        self.background = None

        # method for uploading image from desktop
        f_types = [('Jpg Files', '*.jpg'), ('Png Files', '*.png'), ('Jpeg Files', '*.jpeg')]
        filename = askopenfilename(filetypes=f_types)
        img = Image.open(filename)

        # clearing of labels in position
        for labels in self.root.place_slaves():
            if (labels.place_info()["y"]) == '280':
                labels.place_forget()

        # saving the initial image size
        self.original_size = img.size

        # using pillow library to resize image to fit screen
        self.pic = ImageTk.PhotoImage(img.resize((512, 400)))
        # making image background of canvas
        self.background = self.canvas.create_image(0, 0, anchor='nw', image=self.pic)

    def move_text(self, event):
        # changing the text position to follow mouse , successfully relocating text
        # on screen

        # get position of mouse
        self.x = event.x
        self.y = event.y

        self.canvas.delete(self.text)
        self.text = self.canvas.create_text(self.x, self.y, text=self.text_var.get(),
                                            font=(self.font.get(), self.sizing.get(),
                                                  self.style.get()), fill=self.color)

    def update_text(self, event):
        # updating the text value in the image
        self.canvas.delete(self.text)
        self.text = self.canvas.create_text(self.x, self.y, text=self.text_var.get(),
                                            font=(self.font.get(), self.sizing.get(),
                                                  self.style.get()), fill=self.color)

    def upload_logo(self):
        f_types = [('Jpg Files', '*.jpg'), ('Png Files', '*.png'), ('Jpeg Files', '*.jpeg')]
        filename = askopenfilename(filetypes=f_types)
        self.img = Image.open(filename)

        self.logo_pic = ImageTk.PhotoImage(self.img.resize((50, 50)))

        self.logo = self.canvas.create_image(self.im_x, self.im_y, image=self.logo_pic)

    def resizing_image(self, event):
        self.ratio = self.img_size.get()
        self.logo_pic = ImageTk.PhotoImage(self.img.resize((self.ratio, self.ratio)))
        self.canvas.delete(self.logo)
        self.logo = self.canvas.create_image(self.im_x, self.im_y, image=self.logo_pic)


    def brighten(self, event):
        self.bright_value = self.brightness.get()

        self.im = ImageEnhance.Brightness(self.img)
        self.im = self.im.enhance(self.bright_value)

        self.logo_pic = ImageTk.PhotoImage(self.im.resize((self.ratio, self.ratio)))
        self.canvas.delete(self.logo)
        self.logo = self.canvas.create_image(self.im_x, self.im_y, image=self.logo_pic)

    def sharpen(self, event):
        self.sharp_value = self.sharpness.get()

        self.im = ImageEnhance.Sharpness(self.im)
        self.im = self.im.enhance(self.bright_value)

        self.logo_pic = ImageTk.PhotoImage(self.im.resize((self.ratio, self.ratio)))
        self.canvas.delete(self.logo)
        self.logo = self.canvas.create_image(self.im_x, self.im_y, image=self.logo_pic)


    def contrasting(self, event):
        self.contrast_value = self.contrast.get()

        self.im = ImageEnhance.Contrast(self.im)
        self.im = self.im.enhance(self.bright_value)

        self.logo_pic = ImageTk.PhotoImage(self.im.resize((self.ratio, self.ratio)))
        self.canvas.delete(self.logo)
        self.logo = self.canvas.create_image(self.im_x, self.im_y, image=self.logo_pic)

    def relocate_img(self, event):
        self.im_x = event.x
        self.im_y = event.y

        self.canvas.delete(self.logo)
        self.logo = self.canvas.create_image(self.im_x, self.im_y, image=self.logo_pic)

    def save(self):
        # save postscipt image
        eps = self.canvas.postscript(colormode='color')
        # use PIL to convert to PNG
        im = Image.open(BytesIO(bytes(eps, 'ascii')))

        file_path = asksaveasfilename(defaultextension=".png",
                                      filetypes=[("PNG files", "*.png"),
                                                 ("JPEG files", "*.jpg"),
                                                 ("All Files", "*.*")])

        if file_path:
            im = im.resize(self.original_size)
            im.save(file_path, optimize=True)
            messagebox.showinfo('success', 'File Saved Successfully')
