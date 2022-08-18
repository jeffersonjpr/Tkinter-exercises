from tkinter import *

root = Tk()
root.title("Calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

queue = []
opr = []

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear():
    entry.delete(0, END)

def button_operation(operation):
    if not entry.get():
        return
    queue.append(entry.get())
    opr.append(operation)
    entry.delete(0, END)
    print(queue)
    print(opr)

def button_equals():
    if not entry.get():
        return
    queue.append(entry.get())
    
    result = int(queue.pop(0))
    while(queue):
        if opr.pop(0) == "+":
            result += int(queue.pop(0))
        else:
            result -= int(queue.pop(0))
    
    entry.delete(0, END)
    entry.insert(0, str(result))
    
#defining buttons
button_1 = Button(root, text="1", padx=40, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20,
                  command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20,
                  command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20,
                  command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20,
                  command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20,
                  command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20,
                  command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20,
                  command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20,
                  command=lambda: button_click(0))
button_add = Button(root, text="add", padx=33, pady=20,
                    command=lambda: button_operation("+"))
button_sub = Button(root, text="sub", padx=33, pady=20,
                    command=lambda: button_operation("-"))
button_eqs = Button(root, text="=", padx=145, pady=20,
                    command=button_equals)
button_clr = Button(root, text="Clear", padx=130,
                    pady=20, command=button_clear)

#putting buttons on the screen
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_sub.grid(row=4, column=1)
button_add.grid(row=4, column=2)

button_clr.grid(row=5, column=0, columnspan=4)
button_eqs.grid(row=6, column=0, columnspan=4)

root.mainloop()
