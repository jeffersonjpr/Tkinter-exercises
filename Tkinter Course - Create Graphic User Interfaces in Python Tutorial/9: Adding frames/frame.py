import tkinter


from tkinter import *
from tkinter.ttk import Labelframe

root = Tk()
root.title('Frames')

frame1 = LabelFrame(root, text='First Frame', padx=30, pady=10)
frame1.pack(padx=10, pady=10,  side=LEFT)
frame2 = LabelFrame(root, text='Second Frame', padx=30, pady=10)
frame2.pack(padx=10, pady=10, side=RIGHT)

b1 = Button(frame1, text='Click Me')
b2 = Button(frame1, text='Click Me To')
b3 = Button(frame2, text='Do not Click Me')
b4 = Button(frame2, text='Click Me Instead')

b1.pack()
b2.pack()
b3.pack()
b4.pack()

root.mainloop()