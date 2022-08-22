from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Checkboxes")

var1 = StringVar()
var2 = IntVar()

checkbox1 = Checkbutton(root, text="Option 1", variable=var1, onvalue="Liga", offvalue="Desl")
checkbox1.deselect()
checkbox1.pack()
checkbox2 = Checkbutton(root, text="Option 2", variable=var2).pack()

def save_options():
    print(f"Options selected: {str(var1.get())} {str(var2.get())}")

myButton = Button(root, text="Save options",command=save_options)
myButton.pack()

mainloop()
