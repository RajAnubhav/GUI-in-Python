from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x480")

def closeAllTabs():
    tab1.destroy()
    tab1.pack()

'''how to add popup from mouse'''
m = Menu(root, tearoff=0)
m.add_command(label="Cut")
m.add_command(label="Copy")
m.add_command(label="Paste")
m.add_separator()
m.add_command(label="Rename")
m.add_command(label="Close Current Tab")
m.add_command(label="Close All Tabs", command=closeAllTabs)

def mouse_click(event):
    m.tk_popup(event.x_root, event.y_root)

tabs = ttk.Notebook(root)
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tabs.add(tab1, text="Get Started    x")
tabs.add(tab2, text="Tab2   x")
tabs.pack(expand=1, fill=BOTH)

ttk.Label(tab1, text="Tab1").pack()
ttk.Label(tab2, text="Tab2").pack()

root.bind("<Button-3>", mouse_click)
root.mainloop()