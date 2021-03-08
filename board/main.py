import tkinter as tk
from tkinter import ttk

WIDTH, HEIGHT = 1200, 800
WIDTH_MIN, HEIGHT_MIN = 400, 250


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
        x = (self.winfo_screenwidth() - w) // 2
        y = (self.winfo_screenheight() - h) // 2
        return x, y


    def draw_board(self, width, height):
        """"""

        self.style = ttk.Style()
        self.style.configure('TFrame', borderwidth=3, relief=tk.RAISED, background='SaddleBrown')
        self.frame1 = ttk.Frame(self, style='TFrame')
        self.frame1.pack(fill=tk.BOTH, expand=1)
        self.frame2 = ttk.Frame(self, style='TFrame', height=int(0.8 * height))
        self.frame2.pack(fill=tk.BOTH, expand=1)
        self.frame3 = ttk.Frame(self, style='TFrame')
        self.frame3.pack(fill=tk.BOTH, expand=1)

    def change(self, event):
        """"""
        pass


if __name__ == '__main__':
    window = Window(WIDTH, HEIGHT)
    width = WIDTH
    height = HEIGHT
    window.draw_board(width, height)
    window.bind('<Configure>', window.change)
    window.mainloop()
