<<<<<<< HEAD
from tkinter import *

# Create object for splash window
splash_root = Tk()

# Adjust size
splash_root.geometry("200x215")

# set label
splash_label = Label(splash_root, text="Screen1", font=18)
splash_label.pack()

# main window function
def main():
    # destroy the splash window
    splash_root.destroy()

    # creating the object of the main window
    root = Tk()

    # adjusting the size of the main window
    root.geometry("200x215")

# set the interval and calling the main function
splash_root.after(1000, main)

# execute tkinter
mainloop()
=======
from tkinter import *

# Create object for splash window
splash_root = Tk()

# Adjust size
splash_root.geometry("200x215")

# set label
splash_label = Label(splash_root, text="Screen1", font=18)
splash_label.pack()

# main window function
def main():
    # destroy the splash window
    splash_root.destroy()

    # creating the object of the main window
    root = Tk()

    # adjusting the size of the main window
    root.geometry("200x215")

# set the interval and calling the main function
splash_root.after(3000, main)

# execute tkinter
mainloop()
>>>>>>> 8506ab370b07818efee725a90e806c0aede97115
