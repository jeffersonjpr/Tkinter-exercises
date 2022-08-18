from tkinter import *

def myClick():
    myLabel = Label(root, text="Look! I cklicked a button!!")
    myLabel.pack()

root = Tk()

entry = Entry(root, width=50, bg="blue", fg="white")
entry.pack()

myButton = Button(root, text="Click Me", command=myClick, fg="green", bg="black")
myButton.pack()

root.mainloop()