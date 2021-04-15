import tkinter as tk
from tkinter import ttk



class BStyle():
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.style = ttk.Style(self.master)
        self.style.theme_use('clam')  # if these themes("vista" and "xpnative") are installed on the computer,
        # the progress bar color does not change, remains green.
        self.style.configure('Board.TFrame', borderwidth=3, relief=tk.RAISED, background='SaddleBrown')
        self.style.configure('Field.TFrame', borderwidth=1, relief=tk.GROOVE, background="Moccasin")
