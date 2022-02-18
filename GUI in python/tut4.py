# buttons in GUI

from cgitb import text
from tkinter import *
from turtle import right
root = Tk()

root.geometry("600x400")

# we can execute command also using functions
def select_btn():
    print("Hello select button")

def print_btn():
    print("Hello print button")

def exit_btn():
    print("Hello exit button")

frame = Frame(root, borderwidth=6, relief=FLAT)
frame.pack(side=LEFT, anchor=NE)

b1 = Button(frame, fg="orange", text="Select", bg="grey", command=select_btn)
b1.pack(side=LEFT)
# command needs the function name and not function with return type

b3 = Button(frame, fg="white", text="Exit", bg="grey", command=exit_btn)
b3.pack(side=LEFT)

b2 = Button(frame, fg="green", text="Print", bg="grey", command=print_btn)
b2.pack(side=LEFT)

root.mainloop()