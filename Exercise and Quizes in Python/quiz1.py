from tkinter import *
from PIL import ImageTk, Image
root = Tk()
canvas = Canvas(root, width=570, height=440).pack()
img = ImageTk.PhotoImage(Image.open("E:\Coding\Python GUI\Exercise and Quizes in Python\pic1.jpg"))


root.mainloop()
