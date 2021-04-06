import tkinter as tk
from tkinter import ttk



class SBoard():
    def __init__(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')  # if these themes("vista" and "xpnative") are installed on the computer,
        # the progress bar color does not change, remains green.
        self.style.configure('Board.TFrame', borderwidth=3, relief=tk.RAISED, background='SaddleBrown')