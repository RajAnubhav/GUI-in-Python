# this is the program for the paned window in tkinter

from cgitb import text
from tkinter import *
from tkinter import ttk

from numpy import true_divide

root = Tk()
root.geometry("720x440")
ttk.Label(root, text="Separating widget").pack()

# create Panedwindow
pandedwindow = ttk.PanedWindow(root, orient=HORIZONTAL)
pandedwindow.pack(fill=BOTH, expand=TRUE)

# create frames
frame1 = ttk.Frame(pandedwindow, width=100, height=440, relief=SUNKEN)
frame2 = ttk.Frame(pandedwindow, width=610, height=440, relief=SUNKEN)
pandedwindow.add(frame1, weight=1)
pandedwindow.add(frame2, weight=4)
root.mainloop()