from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Jefferson")
myLabel3 = Label(root, text="-------------")

myLabel1.grid(row=0, column=0)
myLabel3.grid(row=1, column=2) #relative to each other
myLabel2.grid(row=2, column=5)

root.mainloop()