from tkinter import *
root = Tk() 

def clicked(val):
    global myLabel
    myLabel.configure(text=val)

modes = [("X-bacon", "X-bacon"), ("X-salada", "X-salada"),
         ("X-ratão", "X-ratão"), ("X-brguer", "X-burguer")]

burguer = StringVar()
burguer.set("X-burguer")

for text, mode in modes:
    Radiobutton(root, text=text, variable=burguer,
                value=mode, padx=5, pady=5).pack(anchor=CENTER)

myButton = Button(root, text='Ok', command=lambda: clicked("Option: " + str(burguer.get())))
myButton.pack(padx=10, pady=10)

myLabel = Label(root, text="Option: " + str(burguer.get()))
myLabel.pack(padx=5, pady=5)

root.mainloop()