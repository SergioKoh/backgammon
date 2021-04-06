import tkinter as tk
from tkinter import ttk



class STmove():
    def __init__(self, player):
        self.player = player
        self.style = ttk.Style()
        self.color0 = 'snow'
        self.color1 = 'black'
        if self.player:
            self.style.configure('Top1.Horizontal.TProgressbar', background=self.color1)
        else:
            self.style.configure('Bottom0.Horizontal.TProgressbar', background=self.color0)
