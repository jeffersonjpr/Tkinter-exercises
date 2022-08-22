from tkinter import *

root = Tk()
root.title("Main Window")
lbl = Label(root, text="This is the main window").pack(padx=50)


def newWindow():
    top = Toplevel()
    top.title("Second Window")
    lbl = Label(top, text="This is a new window").pack(padx=50, pady=20)
    btn = Button(top, text="Close", command=top.destroy).pack(padx=50, pady=20)


btn = Button(root, text="New Window", command=newWindow)
btn.pack(padx=50)

mainloop()
