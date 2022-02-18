from ast import Expression
from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

root = Tk()
root.title("Calculator")
root.geometry("305x380")
root.maxsize(305, 380)
root.minsize(305, 380)

entry= ""

def press(num):
    global entry
    entry = entry + str(num)
    valValue.set(entry)

valValue = StringVar()
valEntry = Entry(root, textvariable=valValue)

valEntry.grid(columnspan=4, ipadx=80)
def addition():
    pass

def subtraction():
    pass

def multiplication():
    pass

def division():
    pass

def C():
    pass

def AC():
    global entry
    entry = ""
    valValue.set("")

b1 = Button(root, text="AC", command=lambda: press(AC)).grid(row=6, column=0)
ttk.Button(root, text="C", command=lambda: press(C)).grid(row=6, column=1)
ttk.Button(root, text="%").grid(row=6, column=2)
ttk.Button(root, text="/").grid(row=6, column=3)

ttk.Button(root, text="7").grid(row=7, column=0)
ttk.Button(root, text="8").grid(row=7, column=1)
ttk.Button(root, text="9").grid(row=7, column=2)
ttk.Button(root, text="*").grid(row=7, column=3)

ttk.Button(root, text="4").grid(row=8, column=0)
ttk.Button(root, text="5").grid(row=8, column=1)
ttk.Button(root, text="6").grid(row=8, column=2)
ttk.Button(root, text="-").grid(row=8, column=3)

ttk.Button(root, text="1").grid(row=9, column=0)
ttk.Button(root, text="2").grid(row=9, column=1)
ttk.Button(root, text="3").grid(row=9, column=2)
ttk.Button(root, text="+").grid(row=9, column=3)

ttk.Button(root, text="Exit", command=root.destroy).grid(row=10,column=0)
ttk.Button(root, text="0", command=press(0)).grid(row=10, column=1)
ttk.Button(root, text=".").grid(row=10,column=2)
ttk.Button(root, text="=").grid(row=10, column=3)



root.mainloop()