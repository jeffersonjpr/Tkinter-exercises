from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Slider")
root.geometry("400x250")

vertical = Scale(root, from_=500, to=200, orient=VERTICAL)
horizontal = Scale(root, from_=200, to=500, orient=HORIZONTAL)

vertical.pack()
horizontal.pack()

phone_number = Label(root, text="Phone Number: ")
phone_number.pack()

def sliders():
    global phone_number
    phone_number.config(text=str(vertical.get()) + "-" + str(horizontal.get()))
    root.geometry(str(vertical.get()) + "x" + str(horizontal.get()))
    root.update()

btn = Button(root, text="Save", command=sliders).pack()

mainloop()
