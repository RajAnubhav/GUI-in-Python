from tkinter import *
root = Tk()
m= Menu(root, tearoff=0)
m.add_command(label="Cut")
m.add_command(label="Copy")
m.add_command(label="Paste")
m.add_command(label="Reload")
m.add_separator()
m.add_command(label="Rename")

def do_popup(event):
    m.tk_popup(event.x_root, event.y_root)

root.bind("<Button-3>", do_popup)  # <Button-3> is for the right-click of the mouse
root.mainloop()