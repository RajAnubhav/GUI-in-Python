from tkinter import *

root = Tk()
root.title("Keyboard input")
root.geometry("500x440")

def kbr_click(event):
    pass

# we use .bind(event, action)
'''
list of events
<Button-1> - left mouse click
<Button-2> - middle mouse click
<Button-3> - right mouse click
<key> - to get the event from click : event.char should be passed here
'''
root.mainloop()