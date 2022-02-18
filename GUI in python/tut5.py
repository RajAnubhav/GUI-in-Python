# Grids in Python GUI

from cgitb import text
from tkinter import *

root = Tk()
root.title("Program 5")
root.geometry("500x300")

def getVals():
    print(f"UserName : {userValue.get()}")
    print(f"Password : {passValue.get()}")
    exit()

user = Label(root, text="Username : ")
password = Label(root, text="Password : ")
user.grid(row=3, column=0)
password.grid(row=4, column=0 )


# for the inputs
userValue = StringVar()
passValue = StringVar()

userEntry = Entry(root, textvariable= userValue).grid(row=3, column=1)
passEntry = Entry(root, textvariable= passValue).grid(row=4, column=1)

Button(root, text="Sign in", command=getVals).grid(row=5, column=1)


root.mainloop()