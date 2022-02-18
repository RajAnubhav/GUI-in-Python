# from importlib.metadata import entry_points
# from tkinter import *
# from turtle import width
# from PIL import ImageTk, Image
# from tkinter import ttk

# root = Tk()


# def displayImage():
#     """This is for displaying the image"""
#     title = input("Enter the title of the window: ")
#     root.title(f"{title}")
#     root.geometry("575x440")

#     canvas = Canvas(root, width=600, height=600)
#     canvas.pack()
#     img = ImageTk.PhotoImage(Image.open("pic1.jpg"))
#     canvas.create_image(20, 20, anchor=NW, image=img)


# def displayText():
#     global entry
#     string = entry.get()
#     label.configure(text=string)


# label = Label(root, text="", font="Courier 22 bold")
# label.pack()

# displayImage()
# displayText()

# # Create a Button to validate Entry Widget
# ttk.Button(root, text="Enter", width=20, command=displayText).pack(pady=20)

# root.mainloop()


from importlib.metadata import entry_points
from tkinter import *
from tkinter import ttk
from venv import EnvBuilder

win = Tk()
win.geometry("750x250")
def displayText():
    global entry
    string= entry.get()
    label.configure(text=string)

label = Label(win, text="", font="Courier 22 bold")
label.pack()

entry= Entry(win, width=40)
entry.focus_set()
entry.pack()

ttk.Button(win, text="Okay", width=20, command= displayText).pack(pady=20)
win.mainloop()