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
