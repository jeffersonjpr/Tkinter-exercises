from tkinter import *
root = Tk() 

rb = IntVar()

def clicked(val):
    global myLabel
    myLabel.configure(text=val)

Radiobutton(root, text='Option 1', variable=rb, value=1, padx=5, pady=5).pack()
Radiobutton(root, text='Option 2', variable=rb, value=2, padx=5, pady=5).pack()
Radiobutton(root, text='Option 3', variable=rb, value=3, padx=5, pady=5).pack()

myLabel = Label(root, text=rb.get())
myLabel.pack()

myButton = Button(root, text='Click Me', command=lambda: clicked("Option: " + str(rb.get())))
myButton.pack(padx=5, pady=5)
#mainloop
root.mainloop() #this will keep the window open until you close it