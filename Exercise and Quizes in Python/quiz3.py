# make a form for dance class

from distutils import command
from tkinter import *

root = Tk()
root.title("Quiz 4")
root.geometry("600x400")



def getVals():
    file = open("Exercise and Quizes in Python/Sample.txt", "a")
    file.writelines(f"UserName : {userVal.get()}\tPassWord : {passVal.get()}\n")
    exit()

l1 = Label(root, text="Welcome to the Dance Class", font="ComicSans 12 bold").grid(row=0, column=8)
user = Label(root, text="UserName : ").grid(row=1)
password = Label(root, text="Password : ").grid(row=2)

userVal = StringVar()
passVal = StringVar()


userEntry = Entry(root, textvariable=userVal).grid(row=1, column=1)
passEntry = Entry(root, textvariable=passVal).grid(row=2, column=1)

Button(root, text="Sign in", command=getVals).grid(row=3, column=2)


root.mainloop()