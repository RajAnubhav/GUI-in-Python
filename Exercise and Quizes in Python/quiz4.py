from distutils import command
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x400")

def entryText(user):
    file = open("Sample.txt", "a")
    file.writelines(user)

def displayText():
    global entry
    string= f"{entry.get()}, you are succefully logged in"
    label.configure(text=string)
    
    entryText(string)

l1 = Label(root, text="UserName : ").pack()

entry= Entry(root, width=40)
entry.pack()

ttk.Button(root, text="Okay", width=20, command=displayText).pack()

label= Label(root, text="", font="Courier 12 bold")
label.pack()

root.mainloop()