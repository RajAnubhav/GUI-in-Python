from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
# root.title("Menu Demonstration")

# Adding File Menu and commands
root.geometry("500x400")
menuBar = Menu(root)
file = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=file)
file.add_command(label="New File", command=None)
file.add_command(label="Open", command=None)
file.add_command(label="Save", command=None)
file.add_separator()
file.add_command(label="Exit", command=root.destroy)

# Adding Edit Menu and commands
edit = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut", command=None)
edit.add_command(label="Copy", command=None)
edit.add_command(label="Paste", command=None)
edit.add_command(label="Select All", command=None)
edit.add_separator()
edit.add_command(label="Find...", command=None)
edit.add_command(label="Find again", command=None)

# Adding Help Menu
help_ = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=help_)
help_.add_command(label="Help", command=None)
help_.add_command(label="Tk Help", command=None)
help_.add_command(label="Demo", command=None)
help_.add_separator()
help_.add_command(label="About Tk", command=None)

# display Menu
root.config(menu = menuBar)
root.mainloop()