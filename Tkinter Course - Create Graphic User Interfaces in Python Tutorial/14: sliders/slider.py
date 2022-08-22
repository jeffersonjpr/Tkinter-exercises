from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Slider")
root.geometry("200x200")

phone_number = Label(root, text="Phone Number: ")
phone_number.pack()


def sliders():
    global phone_number
    phone_number.config(text=str(vertical.get()) + "-" + str(horizontal.get()))
    root.geometry(str(vertical.get()) + "x" + str(horizontal.get()))
    root.update()


vertical = Scale(root, from_=500, to=200, orient=VERTICAL, command=print)
horizontal = Scale(root, from_=200, to=500, orient=HORIZONTAL, command=print)
vertical.pack()
horizontal.pack()

btn = Button(root, text="Set", command=sliders).pack()

mainloop()
