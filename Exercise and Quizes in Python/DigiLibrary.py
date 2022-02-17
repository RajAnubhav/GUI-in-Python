from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk

root = Tk()
root.title("Digital Library")
root.minsize(680, 450)

word = Label(text="WELCOME TO THE DIGITAL LIBRARY", font="Times 30 bold", fg="white", bg="#A1CAF1")
word.pack(side=TOP, anchor=NW)

time = Label(text="""Welcome to the Digital Library,
an initiative by students of SIT""", padx=370, bg="#F0FFFF")
time.pack(side=TOP)
root.mainloop()