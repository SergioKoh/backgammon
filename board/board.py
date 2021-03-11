import tkinter as tk
from tkinter import ttk
import time


import main

WIDTH, HEIGHT = 1200, 800
WIDTH_MIN, HEIGHT_MIN = 600, 400



class WFrame(ttk.Frame):
    """Container for
    """

    def __init__(self, master, width, height):
        super().__init__(master)
        self.master = master
        self.style = ttk.Style()
        self.style.configure('TFrame', borderwidth=3, relief=tk.RAISED, background='SaddleBrown')
        self.height = height
        self.width = width
        self.width0 = int(0.017 * self.width)
        self.width1 = int(0.466 * self.width)
        self.width2 = int(0.017 * self.width)
        self.width3 = int(0.017 * self.width)
        self.width4 = int(0.466 * self.width)
        self.width5 = width - self.width0 - self.width1 - self.width2 - self.width3 - self.width4

        self.frame0 = ttk.Frame(self, style='TFrame', width=self.width0, height=self.height)
        self.frame1 = ttk.Frame(self, style='TFrame', width=self.width1, height=self.height)
        self.frame2 = ttk.Frame(self, style='TFrame', width=self.width2, height=self.height)
        self.frame3 = ttk.Frame(self, style='TFrame', width=self.width3, height=self.height)
        self.frame4 = ttk.Frame(self, style='TFrame', width=self.width4, height=self.height)
        self.frame5 = ttk.Frame(self, style='TFrame', width=self.width5, height=self.height)

        self.frame0.grid(column=0, row=0, sticky="nsew")
        self.frame1.grid(column=1, row=0, sticky="nsew")
        self.frame2.grid(column=2, row=0, sticky="nsew")
        self.frame3.grid(column=3, row=0, sticky="nsew")
        self.frame4.grid(column=4, row=0, sticky="nsew")
        self.frame5.grid(column=5, row=0, sticky="nsew")

        tk.Grid.rowconfigure(self, index=0, weight=1)
        tk.Grid.columnconfigure(self, index=1, weight=1)
        tk.Grid.columnconfigure(self, index=4, weight=1)

        self.orient = 'vertical'
        Window.progress_bar(self.master, self.frame5, self.orient)



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
        self.height0 = self.height2 = int(0.05 * self.height)
        self.height1 = self.height - self.height0 - self.height2


        self.frame0 = ttk.Frame(self, style='TFrame', width=self.width)
        self.frame1 = WFrame(self, width=self.width, height=self.height1)
        self.frame2 = ttk.Frame(self, style='TFrame', width=self.width)

        self.frame0.grid(column=0, row=0, sticky="nsew")
        self.frame1.grid(column=0, row=1, sticky="nsew")
        self.frame2.grid(column=0, row=2, sticky="nsew")


        tk.Grid.columnconfigure(self, index=0, weight=1)
        tk.Grid.rowconfigure(self, index=1, weight=1)

        self.orient = 'horizontal'
        self.progress_bar(self.frame0, self.orient)
        self.progress_bar(self.frame2, self.orient)


    def progress_bar(self, frame, orient):
        """"""
#        self.style.theme_use('default')
        self.frame = frame
        self.orient = orient
        if self.orient == 'horizontal':
            self.style.configure("black.Horizontal.TProgressbar", background='red')
            self.bar_hor = ttk.Progressbar(frame, length=int(0.5 * WIDTH_MIN), orient='horizontal', style='black.Horizontal.TProgressbar')
            self.bar_hor['value'] = 50
            self.bar_hor.pack(anchor="center")
        else:
            self.style.configure("black.Vertical.TProgressbar", background='red')
            self.ver_anchor = "n"
            for i in range(2):
                self.bar_ver = ttk.Progressbar(frame, length=int(0.45 * HEIGHT_MIN), orient='vertical', style="black.Vertical.TProgressbar")
                self.bar_ver['value'] = 50
                self.bar_ver.pack(expand=True, anchor=self.ver_anchor)
                self.ver_anchor = "s"



