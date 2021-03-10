import tkinter as tk
from tkinter import ttk


WIDTH, HEIGHT = 1200, 800
WIDTH_MIN, HEIGHT_MIN = 600, 400



class WFrame(ttk.Frame):
    """Container for
    """

    def __init__(self, master, style, width, height):
        super().__init__(master)
        self.master = master
        self.style = style
        self.height = height
        self.width = width
        self.width1 = int(0.067 * width)
        self.width2 = int(0.366 * width)
        self.width3 = int(0.067 * width)
        self.width4 = int(0.067 * width)
        self.width5 = int(0.366 * width)
        self.width6 = int(0.067 * width)

        self.frame1 = ttk.Frame(self, style='TFrame', width=self.width1, height=self.height)
        self.frame2 = ttk.Frame(self, style='TFrame', width=self.width2, height=self.height)
        self.frame3 = ttk.Frame(self, style='TFrame', width=self.width3, height=self.height)
        self.frame4 = ttk.Frame(self, style='TFrame', width=self.width4, height=self.height)
        self.frame5 = ttk.Frame(self, style='TFrame', width=self.width5, height=self.height)
        self.frame6 = ttk.Frame(self, style='TFrame', width=self.width6, height=self.height)
        """
        self.frame1.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)
        self.frame2.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)
        self.frame3.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)
        self.frame4.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)
        self.frame5.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)
        self.frame6.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)

        """
        self.frame1.place(relx=0.0,  rely=0.05, relwidth=0.067, relheight=0.9)
        self.frame2.place(relx=0.067, rely=0.05, relwidth=0.366, relheight=0.9)
        self.frame3.place(relx=0.433, rely=0.05, relwidth=0.067, relheight=0.9)
        self.frame4.place(relx=0.5, rely=0.05, relwidth=0.067, relheight=0.9)
        self.frame5.place(relx=0.567, rely=0.05, relwidth=0.366, relheight=0.9)
        self.frame6.place(relx=0.0933, rely=0.05, relwidth=0.067, relheight=0.9)


class Window(tk.Tk):
    """Displaying objects on the canvas"""

    def __init__(self, w, h):
        super().__init__()
        self.title("Backgammon")
        x, y = self.center_screen(w, h)
        self.geometry(f'{w}x{h}+{x}+{y}')
        self.resizable(True, True)
        self.minsize(WIDTH_MIN, HEIGHT_MIN)

    def center_screen(self, w, h):
        """Centering the window."""
        x = abs((self.winfo_screenwidth() - w)) // 2
        y = abs((self.winfo_screenheight() - h)) // 2
        return x, y

    def draw_board(self, w=WIDTH, h=HEIGHT):
        """"""
        self.style = ttk.Style()
        self.style.configure('TFrame', borderwidth=3, relief=tk.RAISED, background='SaddleBrown')
        self.width = w
        self.height = h
        self.height1 = self.height3 = int(0.05 * self.height)
        self.height2 = self.height - self.height1 - self.height3

        self.frame1 = ttk.Frame(self, style='TFrame', width=self.width, height=self.height1)
        self.frame2 = WFrame(self, style='TFrame', width=self.width, height=self.height2)
        self.frame3 = ttk.Frame(self, style='TFrame', width=self.width, height=self.height3)

        self.frame1.place(rely=0.00, relheight=0.05)
        self.frame2.place(rely=0.05, relheight=0.9)
        self.frame3.place(rely=0.95, relheight=0.05)

