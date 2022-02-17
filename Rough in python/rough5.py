import tkinter as tk
from tkinter import ttk

class Myapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = ttk.Frame(self, borderwidth=10, relief="sunken", width=200, height=100)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # for F in (HomePage, PageOne):
        #     frame = F(container, self)
        #     self.frames[F] = frame
        #     frame.grid(row=0, column=0, sticky="N,S,E,W")
        # self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# class HomePage(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text="HomePage")
#         label.pack()
#         button1 = ttk.Button(self, text="Quit",
#                             command=lambda: quit())
#         button1.pack()
#         button2 = ttk.Button(self, text="Call Function in the other page/class to show the label",
#                             command=lambda: PageOne.function()) # this is to do it from an other class. I can't do this
#         button2.pack()
#         button3 = ttk.Button(self, text="Page One",
#                             command=lambda: controller.show_frame(PageOne))
#         button3.pack()


# class PageOne(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text="PageOne")
#         label.pack()
#         button1 = ttk.Button(self, text="Quit",
#                             command=lambda: quit())
#         button1.pack()
#         button2 = ttk.Button(self, text="Call Function, in local it works..",
#                             command=lambda: self.function())#this is to do it in local
#         button2.pack()
#         button3 = ttk.Button(self, text="HomePage",
#                             command=lambda: controller.show_frame(HomePage))
#         button3.pack()

#     def function(self):
#         label1 = ttk.Label(self, text="It Worked!")
#         label1.pack()


app = Myapp()
app.mainloop()