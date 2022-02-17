# this is an excerise on newspaper reading article
from email.mime import image
from tkinter import *
from PIL import Image, ImageTk
root = Tk()

root.geometry("600x500")
root.minsize(600, 500)
# root.maxsize(600, 500)

head = Label(text="THE TIMES OF INDIA", pady=50, fg="white", font="Times 30 bold")
head.pack(side=TOP)

time = Label(text="SOMEDAY, SOMEWHERE in SOMEWHERE", padx=370, bg="yellow", fg="black", font="Times 10")
time.pack(side=TOP)

img0Load = ImageTk.PhotoImage(Image.open("pic1.jpg"))
img0Render = Label(image=img0Load)
img0Render.pack(anchor=NW)

with open ("0.txt") as f:
    content0 = f.read()
content0Read = Label(text=content0, bg= "white", fg= "black", font="TimesNewRoman 5", relief=GROOVE)
content0Read.pack(anchor=NW)
canvas = Canvas(root, width=300, height=300)
canvas.create_image(20, 20, anchor=NW, image=img0Load)
root.mainloop()