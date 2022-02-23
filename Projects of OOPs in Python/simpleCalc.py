from symtable import Symbol
import tkinter as tk
from tkinter import *

LIGHT_GRAY = "grey"
LABEL_COLOR = "black"
DIGIT_FONT_STYTLE = ("Arial", 30, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 20, "bold")

class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("275x367")
        self.root.resizable(0, 0)
        self.root.title("Calculator")
        self.displayFrame = self.createDisplayFrame()

        self.totalExpression= "0"
        self.currentExpression= "0"

        self.totalLabel, self.Label = self.createDisplayLabels()

        self.digits={
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), ".":(4,1)
            }
        self.operations = {"/":"\u00F7", "-":"-", "+":"+"}
        self.buttonFrame = self.createButtonFrame()
        self.createDigitButton()
        self.createOperaterButton()
        self.createClearButton()
        self.createEqualsButton()

    def createDigitButton(self):
        for digit, gridValue in self.digits.items():
            button = tk.Button(self.buttonFrame, text=str(digit), bg="white", fg=LABEL_COLOR, font=DIGIT_FONT_STYTLE, borderwidth=0).grid(row=gridValue[0], column=gridValue[1], sticky=tk.NSEW)

    def createDisplayLabels(self):
        totalLabel = tk.Label(self.displayFrame, text=self.totalExpression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, font= SMALL_FONT_STYLE, padx=24)
        totalLabel.pack(expand=True, fill=BOTH)

        label =tk.Label(self.displayFrame, text=self.currentExpression, anchor=E, bg=LIGHT_GRAY, fg=LABEL_COLOR, font= LARGE_FONT_STYLE, padx=24)
        label.pack(expand=True, fill=BOTH)

        return totalLabel, label

    def createDisplayFrame(self):
        frame = tk.Frame(self.root, height=200, bg=LIGHT_GRAY)
        frame.pack(expand=TRUE, fill=BOTH)
        return frame

    def createButtonFrame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=TRUE, fill=BOTH)
        return frame
    def createOperaterButton(self):
        i=0
        for opertor, symbols in self.operations.items():
            button = tk.Button(self.buttonFrame, text=symbols, font="Arial 20", fg="black", borderwidth=0).grid(row=i, column=4, sticky=NSEW)
            i+=1
    
    def createClearButton(self):
        button = Button(self.buttonFrame, text="C",  bg="white", fg="black", font="Arial 20 bold", borderwidth=0).grid(row=2, column=4, sticky=NSEW)

    def createEqualsButton(self):
        button = Button(self.buttonFrame, text="=",  bg="white", fg="black", font="Arial 20 bold", borderwidth=0).grid(row=3, column=4, sticky=NSEW)

    def run(self):
        self.root.mainloop()



if __name__ =="__main__":
    clac = Calculator()
    clac.run()