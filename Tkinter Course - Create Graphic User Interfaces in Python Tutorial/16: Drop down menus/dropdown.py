from cgitb import text
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Dropdown")


options = ["Monday", "Tuesday",
           "Wednesday", "Thursday",
           "Friday", "Saturday"]

var = StringVar()
var.set(options[0])

drop = OptionMenu(root, var, *options)
drop.pack(padx=10, pady=5)


def show():
    myLabel = Label(root, text=var.get()).pack()


myBtn = Button(root, text="Show selection", command=show).pack()

mainloop()
