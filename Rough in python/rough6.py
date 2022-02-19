from tkinter import *

class Paint:


    def __init__(self):
        self.root = Tk()
        self.root.title("Paint")
        self.root.iconbitmap("E:/Coding/Python GUI/myqr.png")
        self.root.geometry("540x480")
        self.root.resizable(0, 0)

        self.display_frame = self.create_display_frame()
        self.paint_screen = self.create_paint_screen()
        self.p1 = Canvas(self.root, bg="white", width=520, height=480)

    def create_display_frame(self):
        frame = Frame(self.root, height=50, bg="light blue").pack(expand=TRUE, fill=BOTH)
        
    def create_paint_screen(self, event):
        x1, y1 = (event.x-1), (event.y-1)
        x2, y2 = (event.x+3), (event.y+3)
        color= "black"
        self.p1.create_oval(x1, y1, x2, y2, fill=color, outline=color)

    # def pen_control(self):
    #     self.p1.bind("<Button-1>", self.paint_screen)
    #     self.p1.pack()
    #     self.root.configure(bg="#007FFF")


    def run(self):
        self.root.mainloop()

pt = Paint()
p1 = Canvas(pt.root, bg="white", width=540, height=480)
p1.bind("<Button-1>", pt.create_mouse_control)
p1.pack()
pt.root.configure(bg="#007FFF")
pt.pen_control()


pt.run()