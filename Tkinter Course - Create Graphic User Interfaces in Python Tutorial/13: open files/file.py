from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Open file dialog")


def open_file():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    lbl = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_lbl = Label(image=my_image).pack()


btn = Button(root, text="Open", command=open_file).pack(padx=50, pady=20)

mainloop()
