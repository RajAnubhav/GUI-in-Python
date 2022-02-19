from asyncio import events
from distutils import command
from sqlite3 import Rows
from tkinter import *
from tkinter import ttk

from numpy import delete
root = Tk()
root.title("Calculator")
root.geometry("320x500")

e= Entry(root, width=30)
e.grid(row=0, column=0, columnspan=5, padx=20, pady=50)

# Functions 

def addBtn(num):
    current= e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(num))


def clearBtn():
    e.delete(0, END)


# Define and put buttons on the screen 

b1 = Button(root, text="1", padx=30, pady=23, command= lambda:addBtn(1)).grid(row=4, column=0)
b2 = Button(root, text="2", padx=30, pady=20, command= lambda:addBtn(2)).grid(row=4, column=1)
b3 = Button(root, text="3", padx=30, pady=20, command= lambda:addBtn(3)).grid(row=4, column=2)
b4 = Button(root, text="4", padx=30, pady=20, command= lambda:addBtn(4)).grid(row=3, column=0)
b5 = Button(root, text="5", padx=30, pady=20, command= lambda:addBtn(5)).grid(row=3, column=1)
b6 = Button(root, text="6", padx=30, pady=20, command= lambda:addBtn(6)).grid(row=3, column=2)
b7 = Button(root, text="7", padx=30, pady=20, command= lambda:addBtn(7)).grid(row=2, column=0)
b8 = Button(root, text="8", padx=30, pady=20, command= lambda:addBtn(8)).grid(row=2, column=1)
b9 = Button(root, text="9", padx=30, pady=20, command= lambda:addBtn(9)).grid(row=2, column=2)
b10 = Button(root, text="+/-", padx=25, pady=20, command= lambda:addBtn("-")).grid(row=5, column=0)
b11 = Button(root, text="0", padx=29, pady=20, command= lambda:addBtn(0)).grid(row=5, column=1)
b12 = Button(root, text=".", padx=31, pady=20, command= lambda:addBtn(".")).grid(row=5, column=2)
b13 = Button(root, text="%", padx=29, pady=20, command= lambda:addBtn("%")).grid(row=1, column=0)
b14 = Button(root, text="CE", padx=27, pady=20, command= clearBtn).grid(row=1, column=1)
b15 = Button(root, text="*", padx=29, pady=20, command= addBtn).grid(row=1, column=2)
b16 = Button(root, text="=", padx= 19, pady=20, height=6, command= lambda:addBtn("=")).grid(row=3, column=4, rowspan=5)
b17 = Button(root, text="+", padx=19, pady=23, command= lambda:addBtn("+")).grid(row=2, column=4)
b17 = Button(root, text="-", padx=20, pady=23, command= lambda:addBtn("-")).grid(row=1, column=4)

root.mainloop()