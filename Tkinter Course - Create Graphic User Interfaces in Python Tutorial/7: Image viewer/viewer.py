from tkinter import *
from PIL import ImageTk, Image, ImageOps
import glob



root = Tk()
root.title('Image viewer')

list_of_images_paths = glob.glob("images/*.jpg") + glob.glob("images/*.png")
list_of_images = []
print(list_of_images_paths)
for image_path in list_of_images_paths:
    list_of_images.append(ImageTk.PhotoImage(ImageOps.fit(
        Image.open(image_path), (500, 500))))


myImage = list_of_images[0]
myLabel = Label(image=myImage)
myLabel.grid(row=0, column=0, columnspan=3)

def change_image(image_index):
    global myLabel
    global button_back
    global button_next
    
    myLabel.grid_forget()
    myLabel = Label(image=list_of_images[image_index])
    button_back = Button(root, text='<<<', command=lambda: change_image(image_index - 1))
    button_next = Button(root, text='>>>', command=lambda: change_image(image_index + 1))
    myLabel.grid(row=0, column=0, columnspan=3)
    
    if not image_index:
        button_back = Button(root, text='<<<', state=DISABLED)
    elif image_index == len(list_of_images) - 1:
        button_next = Button(root, text='>>>', state=DISABLED)
        
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)


button_back = Button(root, text="<<<", state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_next = Button(root, text=">>>", command=lambda: change_image(1))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_next.grid(row=1, column=2)

root.mainloop()
