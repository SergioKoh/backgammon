

import tkinter as tk
from tkinter import ttk


BAR_WIDTH = 60

class Board(tk.Tk):
    """Board initialization."""

    def __init__(self, w_min, h_min):
        super().__init__()
        self.title("Backgammon")
        self.resizable(True, True)
        self.minsize(w_min, h_min)
        self.state("zoomed")


    def draw_board(self, board_style):
        """Board broken with frames into table cells."""
        self.style = board_style
        self.bottom_edge = ttk.Frame(self, style='Board.TFrame')
        self.left_edge = ttk.Frame(self, style='Board.TFrame')
        self.playing_field = ttk.Frame(self)
        self.right_edge = ttk.Frame(self, style='Board.TFrame')
        self.top_edge = ttk.Frame(self, style='Board.TFrame')

        opts = {'ipadx': 10, 'ipady': 10}

        self.bottom_edge.pack(fill="x", side="bottom", expand=False, **opts)
        self.top_edge.pack(fill="x", expand=False, **opts)
        self.left_edge.pack(side="left", fill="y", expand=False, **opts)
        self.playing_field.pack(side="left", fill="both", expand=True, **opts)
        self.right_edge.pack(side="left", fill="y", expand=False, **opts)


        return self.playing_field
