import tkinter as tk
from tkinter import ttk

import fields


WIDTH, HEIGHT = 1200, 800
WIDTH_MIN, HEIGHT_MIN = 600, 400


class VFrame(ttk.Frame):
    """Chip position container"""
    def __init__(self, master, width, height):
        super().__init__(master)
        self.master = master
        self.style = ttk.Style()
        self.style.configure('Field.TFrame', borderwidth=1, relief=tk.GROOVE, background="Moccasin")
        self.height = height // 2
        self.width = width // 6

        self.frames = []

        for j in range(2):
            for i in range(6):
                f = ttk.Frame(self, style='Field.TFrame', width=self.width, height=self.height)
                f.grid(column=i, row=j, sticky='nsew')
                tk.Grid.columnconfigure(self, index=i, weight=1)
                self.frames.append(f)
                if not i:
                    tk.Grid.rowconfigure(self, index=j, weight=1)




class WFrame(ttk.Frame):
    """Container for fields."""
    def __init__(self, master, width, height):
        super().__init__(master)
        self.master = master
        self.style = ttk.Style()
        self.style.configure('Board.TFrame', borderwidth=3, relief=tk.RAISED, background='SaddleBrown')
        self.height = height
        self.width = width
        self.width0 = int(0.017 * self.width)
        self.width1 = int(0.466 * self.width)
        self.width2 = int(0.034 * self.width)
        self.width3 = int(0.466 * self.width)
        self.width4 = width - self.width0 - self.width1 - self.width2 - self.width3 - self.width3

        self.frame0 = ttk.Frame(self, style='Board.TFrame', width=self.width0, height=self.height)
        self.frame1 = VFrame(self, width=self.width1, height=self.height)
        self.frame2 = ttk.Frame(self, style='Board.TFrame', width=self.width2, height=self.height)
        self.frame3 = VFrame(self, width=self.width3, height=self.height)
        self.frame4 = ttk.Frame(self, style='Board.TFrame', width=self.width3, height=self.height)
        self.frames = (self.frame0, self.frame1, self.frame2, self.frame3, self.frame4)

        i = 0
        for f in self.frames:
            f.grid(column=i, row=0, sticky='nsew')
            i += 1

        tk.Grid.rowconfigure(self, index=0, weight=1)
        tk.Grid.columnconfigure(self, index=1, weight=1)
        tk.Grid.columnconfigure(self, index=3, weight=1)

        self.orient = 'vertical'
        Window.progress_bar(self.master, self.frame4, self.orient)
        fields.canvases_init(self.frame1, self.frame3, self.frame1.width, self.frame1.height)


class Window(tk.Tk):
    """Window initialization."""
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
        """Board broken with frames into table cells."""
        self.style = ttk.Style()
        self.style.theme_use('clam')  # if these themes("vista" and "xpnative") are installed on the computer,
                                      # the progress bar color does not change, remains green.
        self.style.configure('Board.TFrame', borderwidth=3, relief=tk.RAISED, background='SaddleBrown')
        self.width = w
        self.height = h
        self.height0 = self.height2 = int(0.05 * self.height)
        self.height1 = self.height - self.height0 - self.height2

        self.frame0 = ttk.Frame(self, style='Board.TFrame', width=self.width)
        self.frame1 = WFrame(self, width=self.width, height=self.height1)
        self.frame2 = ttk.Frame(self, style='Board.TFrame', width=self.width)

        self.frame0.grid(column=0, row=0, sticky='nsew')
        self.frame1.grid(column=0, row=1, sticky='nsew')
        self.frame2.grid(column=0, row=2, sticky='nsew')

        tk.Grid.columnconfigure(self, index=0, weight=1)
        tk.Grid.rowconfigure(self, index=1, weight=1)

        self.progress_bar(self.frame0)
        self.progress_bar(self.frame2)

    def progress_bar(self, frame, orient='horizontal', color0='snow', color1='black'):
        """Two Progress bars, upper and lower, show the allotted time per move.
            The two right ones show the number of pieces removed from the board.
        """
        self.frame = frame
        self.orient = orient
        self.color0 = color0
        self.color1 = color1
        if self.orient == 'horizontal':
            if self.frame is self.frame0:
                self.style.configure('Color0.Horizontal.TProgressbar', background=self.color0)
                self.horbar_color0 = ttk.Progressbar(frame, length=int(0.5 * WIDTH_MIN), orient=self.orient,
                                                     style='Color0.Horizontal.TProgressbar')
                self.horbar_color0['value'] = 50
                self.horbar_color0.pack(anchor='center')
            else:
                self.style.configure('Color1.Horizontal.TProgressbar', background=self.color1)
                self.horbar_color1 = ttk.Progressbar(frame, length=int(0.5 * WIDTH_MIN), orient=self.orient,
                                                     style='Color1.Horizontal.TProgressbar')
                self.horbar_color1['value'] = 50
                self.horbar_color1.pack(anchor='center')
        else:
            self.style.configure('Color0.Vertical.TProgressbar', background=self.color0)
            self.verbar_color0 = ttk.Progressbar(frame, length=int(0.45 * HEIGHT_MIN), orient=self.orient,
                                                 style='Color0.Vertical.TProgressbar')
            self.verbar_color0['value'] = 50
            self.verbar_color0.pack(expand=True, anchor='n')

            self.color = 'black'
            self.style.configure('Color1.Vertical.TProgressbar', background=self.color1)
            self.verbar_color1 = ttk.Progressbar(frame, length=int(0.45 * HEIGHT_MIN), orient=self.orient,
                                                 style='Color1.Vertical.TProgressbar')
            self.verbar_color1['value'] = 50
            self.verbar_color1.pack(expand=True, anchor='s')
