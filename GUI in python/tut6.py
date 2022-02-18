# Travel using checkbuttons and entry widget

from msilib.schema import CheckBox
from tkinter import *

root = Tk()
root.geometry("500x300")

def getVals():
    print("It works")

# heading
Label(root, text="Welcome to Anubhav Travels", font="comicsansms 18 bold", pady=15).grid(row=0, column=3)

# getting the label
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentMode = Label(root, text="PaymentMode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentMode.grid(row=5, column=2)

nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emergencyValue = StringVar()
paymentModeValue = StringVar()
foodServiceValue = IntVar()

nameEntry = Entry(root, textvariable=nameValue)
phoneEntry = Entry(root, textvariable=phoneValue)
genderEntry = Entry(root, textvariable=genderValue)
emergencyEntry = Entry(root, textvariable=emergencyValue)
paymentModeEntry = Entry(root, textvariable=paymentModeValue)

nameEntry.grid(row=1, column=3)
phoneEntry.grid(row=2, column=3)
genderEntry.grid(row=3, column=3)
emergencyEntry.grid(row=4, column=3)
paymentModeEntry.grid(row=5, column=3)

# checkBox
foodServiceValue = Checkbutton(text="Want to pre-book your meals", variable=foodServiceValue).grid(row=6, column=3)

# button
Button(text="Submit to Anubhav Travels", command=getVals).grid(row=7, column=3)
root.mainloop()