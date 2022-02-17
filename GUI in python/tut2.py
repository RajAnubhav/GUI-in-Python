from calendar import c
from tkinter import *
from turtle import bgpic
root = Tk()
root.geometry("744x533")
root.title("Digital Library")

# Important Label Options
'''
text = adds the text
bd = background
fg = foreground
font = sets the font
font=("commicsansms", 10, "bold") # this is a tuple
font= "commicsansms 10 bold" # this is a string
padx = x padding
pady = y padding
relief = border styling = SUNKEN, RAISED, GROOVE, RIDGE
'''

title_label = Label(text='''
The National Digital library of India is a project under Ministry of Education,
\nGovernment of India. The objective is to collect and collate metadata and
\nprovide full text index from several national and international digital 
\nlibraries, as well as other relevant sources It is a digital repository 
\ncontaining textbooks, articles, videos, audio books, lectures, simulations, 
\nfiction and all other kinds of learning media. The NDLI provides free of cost
\naccess to many books in the Indian languages and English.''', 
bg="light pink", padx=23, pady=23, font="commicsansms 10 bold", 
borderwidth=3, relief=SUNKEN)


'''
Important Pack options
side = top, bottom, left, right
anchor = nw

fill, padx, pady
'''
# title_label.pack(side="top",anchor="se", fill="both")

title_label.pack()

root.mainloop()