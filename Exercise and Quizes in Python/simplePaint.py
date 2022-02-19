from cgitb import text
from distutils import command
from fileinput import filename
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename
from tkinter.messagebox import askokcancel
from turtle import color
from tkinter import ttk
import os
import os.path

root = Tk()
root.geometry("720x440")

def openNewFile():
    pass

def save_file():
    pass

def saveFileAs():
    f = asksaveasfilename(initialdir="Untitled.dir", defaultextension=".dir", filetypes=[("2D - PNG", "*.png")])
    
    filename =  f
    root.title(f"{filename}")

def eraser(self, event):
    self.activate_button(self.eraser_button, eraser_mode=True)

def open_file():
    f = askopenfilename(initialfile="", defaultextension=".png", filetypes=[("2D - PNG", "*.png")])


def exit_file():
    f = messagebox.askyesno("Save As" ,"Do you want to save the file ? ")
    if(f==1):
        if os.path.isfile(f"{filename}.jpg"):
            return 0
        else:
            saveFileAs()

# def use_eraser(self):
#     self.active

def paint(event):
    x1, y1 = (event.x-1), (event.y-1)
    x2, y2 = (event.x+2), (event.y+2)
    color = "black"
    
    # displaying the mouse movement inside canvas
    p1.create_oval(x1, y1, x2, y2, fill=color, outline=color)

m = Menu(root, tearoff=0)

# making the menus in the popup
m.add_command(label="Eraser")
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

root.bind("<Button-3>", mouse_click)
'''This is for the menu bar'''
menuBar = Menu(root)
file = Menu(root, tearoff=0, bg="#3B3C36", fg="white")
menuBar.add_cascade(label="File", menu=file)
file.add_command(label="New File", command=openNewFile)
file.add_command(label="New Folder", command=openNewFile)
file.add_separator()
file.add_command(label="Open File", command=open_file)
file.add_separator()
file.add_command(label="Save File", command=save_file)
file.add_command(label="Save As...", command=saveFileAs)
file.add_separator()
file.add_command(label="Exit", command=exit_file)

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


# this section is for the paint or main window
# def tab1():
p1 = Canvas(root, bg="white", width=720, height=400)
p1.bind("<B1-Motion>", paint)
p1.pack()
root.configure(bg="#007FFF")

label1 = Label(root, text="Designed at AR Labs", pady=10, bg="#007FFF", fg="White", font="Courier 13 bold").pack()
# this is for the menu-bar
root.config(menu=m)
root.config(menu=menuBar)

root.mainloop()