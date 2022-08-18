from tkinter import *

def myClick():
    message = "Hello " + entry.get()
    myLabel = Label(root, text=message)
    myLabel.pack()

root = Tk()
root.title("Calculator")

entry = Entry(root)
entry.pack()
entry.insert(0, "Enter your name")

myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()
