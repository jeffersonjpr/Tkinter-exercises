from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hands up')
root.iconbitmap("@red-python.xbm")

myImage = ImageTk.PhotoImage(Image.open("stockimage.jpg"))
myLabel = Label(image=myImage)
myLabel.pack()

button_quit = Button(root, text="Run", command=root.quit)
button_quit.pack()



root.mainloop()
