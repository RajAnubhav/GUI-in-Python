# frames in tkinter
from tkinter import *
from PIL import Image, ImageTk

root  = Tk()
root.geometry("600x400")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)
f2 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l1 = Label(f1, text="Project Tkinter - VS Code")
l1.pack()

l2 = Label(f2, text="Welcome to Python GUI", font="Helvetica 16 bold", fg="red")
l2.pack()
root.mainloop()