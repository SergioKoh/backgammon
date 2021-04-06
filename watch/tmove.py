import tkinter as tk
from tkinter import ttk
import time


class Tmove:
    """"""
    def __init__(self, player, frame, style, WIDTH_MIN, T_MOVE):
        self.frame = frame
        self.style = style
        self.player = player
        self.min, self.max = T_MOVE
        self.time_per_move = ttk.Progressbar(frame, length=WIDTH_MIN, orient='horizontal', maximum=self.max,
                                                  style=self.style)
        self.time_per_move.pack(anchor='center')



    def setting_progress_bar(self, options):
        """"""
        self.options = options
        self.time_move1['value'] = self.options['time_move']
        self.time_move0['value'] = self.options['time_move']
        self.time_game1['value'] = self.options['time_game']
        self.time_game0['value'] = self.options['time_game']

        self.style.configure('Bottom0.Horizontal.TProgressbar', background=self.options['color_0'])
        self.style.configure('Top1.Horizontal.TProgressbar', background=self.options['color_1'])
        self.style.configure('Right0.Vertical.TProgressbar', background=self.options['color_0'])
        self.style.configure('Right1.Vertical.TProgressbar', background=self.options['color_1'])
        self.style.configure('Left0.Vertical.TProgressbar', background=self.options['color_0'])
        self.style.configure('Left1.Vertical.TProgressbar', background=self.options['color_1'])