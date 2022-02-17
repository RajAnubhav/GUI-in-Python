from tkinter import *
from tkinter.ttk import *

master = Tk()
master.geometry("400x300")


def openNewWindow():
    # Toplevel object which will be treated as a new Window
    newWindow = Toplevel(master)
    newWindow.title("New Window")
    newWindow.geometry("400x300")
    Label(newWindow, text="This is the new Window").pack()

label = Label(master, text="This is the main window").pack(pady=10)

btn = Button(master, text="Click to Open the New Window", command=openNewWindow).pack(pady=10)
master.mainloop()