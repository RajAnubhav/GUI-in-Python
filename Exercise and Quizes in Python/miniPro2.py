# QR Code generator
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from PIL import Image, ImageTk
import qrcode
import cv2

root = Tk()
root.geometry("720x440")
root.title("QR code Generator")
root.configure(bg="#3B3C36")

# create Panedwindow
pandedwindow = ttk.PanedWindow(root, orient=HORIZONTAL)
pandedwindow.pack(fill=BOTH, expand=TRUE)

# create frames
frame1 = ttk.Frame(pandedwindow, width=100, height=440, relief=SUNKEN)
frame2 = ttk.Frame(pandedwindow, width=610, height=440, relief=SUNKEN)
pandedwindow.add(frame1, weight=1)
pandedwindow.add(frame2, weight=4)

'''This section will contain the menu functions'''
def openNewFile():
    pass

'''this is for the mouse-click popup'''
# making the menus in the popup
m = Menu(root, tearoff=0)
m.add_command(label="Copy")
m.add_command(label="Cut")
m.add_command(label="Paste")
m.add_separator()
m.add_command(label="Edit")
m.add_command(label="Rename")
m.add_separator()
m.add_command(label="Redo")
m.add_command(label="Undo")

def mouse_click(event):
    m.tk_popup(event.x_root, event.y_root)

'''This is for the menu bar'''
menuBar = Menu(root)
file = Menu(root, tearoff=0, bg="#3B3C36", fg="white")
menuBar.add_cascade(label="File", menu=file)
file.add_command(label="New File", command=openNewFile)
file.add_command(label="New Folder", command=openNewFile)
file.add_separator()
file.add_command(label="Open File", command=openNewFile)
file.add_command(label="Open Folder", command=openNewFile)
file.add_separator()
file.add_command(label="Save File", command=openNewFile)
file.add_command(label="Save Folder", command=openNewFile)
file.add_separator()
file.add_command(label="Exit", command=exit)

'''this is for edit section of the menu bar'''
# this will contain the undo, redo, copy, cut and paste option
edit = Menu(root, tearoff=0, bg="#3B3C36", fg="white")
menuBar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Undo", command=None)
edit.add_command(label="Redo", command=None)
edit.add_separator()
edit.add_command(label="Copy", command=None)
edit.add_command(label="Cut", command=None)
edit.add_command(label="Paste", command=None)

'''this is for the Views section of the menu bar'''
# this will contain settings, command palette, appearance, theme
view = Menu(root, tearoff=0, bg="#3B3C36", fg="white")
menuBar.add_cascade(label="View", menu=view)
view.add_command(label="Settings", command=openNewFile)
view.add_separator()
view.add_command(label="Command Palette...", command=None)
view.add_separator()
# appearance and theme will contain the submenus
view.add_command(label="Appearance", command=None)
view.add_command(label="Theme", command=None)

'''This will contain the Help section in the menu bar'''
help1 = Menu(root, tearoff=0, bg="#3B3C36", fg="white")
menuBar.add_cascade(label="Help", menu=help1)
help1.add_command(label="Get Started", command=None)
help1.add_command(label="Show All Commands", command=None)
help1.add_command(label="Documentation", command=None)
help1.add_command(label="Relase Notes", command=None)
help1.add_separator()
help1.add_command(label="Tips and Tricks", command=None)
help1.add_command(label="Keyboard Shortcut Referance", command=None)
help1.add_separator()
help1.add_command(label="Report Issue", command=None)
help1.add_command(label="View License", command=None)
help1.add_command(label="Privacy Statement", command=None)
help1.add_separator()
help1.add_command(label="Check for Updates...", command=None)
help1.add_separator()
help1.add_command(label="About", command=None)

'''this is to add the tabs in the window'''
tabs= ttk.Notebook(frame2)
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)

tabs.add(tab1, text="Get Started")
tabs.add(tab2, text="Tab 2")
tabs.pack(expand=1, fill=BOTH)
# coding for the tab1
# label = Label(text="QR Code Generator", font="Courier 23 bold", pady=40, fg="Black", background="light pink").pack(fill= BOTH)
ttk.Label(tab1, text="This is tab one").pack()
ttk.Label(tab2, text="This is tab two").pack()

footer = Label(pandedwindow, text="Developed by Anubhav", background="#007FFF", fg="white", pady=5, font="Courier 13").pack(side=BOTTOM,fill=BOTH)
# for displaying Menus
root.config(menu=menuBar)

'''this is for the pop-up on right-click'''
root.bind("<Button-3>", mouse_click)

'''for taking the input from the user  '''

root.mainloop()