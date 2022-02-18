# make 4 buttons in GUI and print the outputs

from tkinter import *

root = Tk()
root.title("Sample Program")
root.geometry("500x300")

def exitPro():
    print("Exiting the Program... (Command No. 1)")
    exit()

def printPro():
    print("Hello Print Pro is being envoked (Command No. 2)")

def displayPro():
    print("Printing the value... (Command No. 3)")

def returnPro():
    print("Returning the value... (Command No. 4)")

frame = Frame(root, borderwidth=3)
frame.pack()

b1 = Button(frame, text="Exit", bg="grey", fg="white", command=exitPro)
b1.pack(side=LEFT, anchor=NW)
b2 = Button(frame, text="Display", bg="grey", fg="white", command=displayPro)
b2.pack(side=LEFT, anchor=NW)
b3 = Button(frame, text="Return", bg="grey", fg="white", command=returnPro)
b3.pack(side=LEFT, anchor=NW)
b4 = Button(frame, text="Print", bg="grey", fg="white", command=printPro)
b4.pack(side=LEFT, anchor=NW)

root.mainloop()