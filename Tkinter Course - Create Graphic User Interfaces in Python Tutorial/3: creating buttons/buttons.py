from tkinter import *

def myClick():
    myLabel = Label(root, text="Look! I cklicked a button!!")
    myLabel.pack()

root = Tk()

myButton = Button(root, text="Click Me", command=myClick, fg="green", bg="black")
myButton.pack()

root.mainloop()