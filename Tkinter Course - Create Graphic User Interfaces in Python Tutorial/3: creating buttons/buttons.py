from tkinter import *

def myClick():
    myLabel = Label(root, text="Look! I cklicked a button!!")
    myLabel.pack()

root = Tk()

myButton = Button(root, text="Click Me", padx=30, pady=5)
myButton.pack()

root.mainloop()