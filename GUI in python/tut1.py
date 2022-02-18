
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from turtle import color
n1_root = Tk()  # we make Tk class ki ek object bnate hai

# gui logic
n1_root.geometry("550x400")
n1_root.minsize(550, 400)

# for label
var = Label(text="Hello world", background="blue")
var.pack()

photo = ImageTk.PhotoImage(Image.open("pic1.jpg"))
PhotoImage = Label(image=photo)
PhotoImage.pack()

n1_root.mainloop() 