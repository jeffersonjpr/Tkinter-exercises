from tkinter import *
from urllib import response
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message Box")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, askretrycancel
def showinfomb():
    response = messagebox.showinfo("This is a message box", "Show info message box")
    print(response)

def showwarningmb():
    response = messagebox.showwarning("This is a message box", "Show warning message box")
    print(response)

def showerrormb():
    response = messagebox.showerror("This is a message box", "Show error message box")
    print(response)

def askquestionmb():
    response = messagebox.askquestion("This is a message box", "Ask question message box")
    print(response)
    
def askokcancelmb():
    response = messagebox.askokcancel("This is a message box", "Ask ok cancel message box")
    print(response)
    
def askyesnomb():
    response = messagebox.askyesno("This is a message box", "Ask yes no message box")
    print(response)
    
def askretrycancelmb():
    response = messagebox.askretrycancel("This is a message box", "Ask retry cancel message box")
    print(response)

Button(root, text="Show Info", command=showinfomb).pack(padx=50)
Button(root, text="Show Warning", command=showwarningmb).pack(padx=50)
Button(root, text="Show Error", command=showerrormb).pack(padx=50)
Button(root, text="Ask Question", command=askquestionmb).pack(padx=50)
Button(root, text="Ask Ok Cancel", command=askokcancelmb).pack(padx=50)
Button(root, text="Ask Yes No", command=askyesnomb).pack(padx=50)
Button(root, text="Ask Retry Cancel", command=askretrycancelmb).pack(padx=50)

mainloop()