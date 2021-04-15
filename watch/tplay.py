import tkinter as tk
from tkinter import ttk
import time

WIDTH_MIN, HEIGHT_MIN = 600, 400



class MTimer:
    """"""
    def __init__(self):
        self._start_time = None

        def start(self):
            """Start a new timer"""
#            if self._start_time is not None:
            self._start_time = time.perf_counter()

        def stop(self):
            """Stop the timer, and report the elapsed time"""
#            if self._start_time is None:
            elapsed_time = time.perf_counter() - self._start_time
            self._start_time = None

   def progress_bar(self, frame, orient='horizontal', namber=0):

        self.frame = frame
        self.orient = orient
        self.color0 = 'snow'
        self.color1 = 'black'
        self.namber = namber

        self.style.configure('Bottom0.Horizontal.TProgressbar', background=self.color0)
        self.style.configure('Top1.Horizontal.TProgressbar', background=self.color1)
        self.style.configure('Right0.Vertical.TProgressbar', background=self.color0)
        self.style.configure('Right1.Vertical.TProgressbar', background=self.color1)
        self.style.configure('Left0.Vertical.TProgressbar', background=self.color0)
        self.style.configure('Left1.Vertical.TProgressbar', background=self.color1)

        if self.orient == 'horizontal':
            if self.frame is self.bottom_edge:
                self.time_move1 = ttk.Progressbar(frame, length=int(0.5 * WIDTH_MIN), orient=self.orient, maximum=30,
                                                  style='Top1.Horizontal.TProgressbar')
                self.time_move1.pack(anchor='center')
            else:
                self.time_move0 = ttk.Progressbar(frame, length=int(0.5 * WIDTH_MIN), orient=self.orient, maximum=30,
                                                  style='Bottom0.Horizontal.TProgressbar')
                self.time_move0.pack(anchor='center')
        else:
            if not self.namber:
                self.time_game1 = ttk.Progressbar(frame, length=int(0.45 * HEIGHT_MIN), orient=self.orient, maximum=20,
                                                  style='Left1.Vertical.TProgressbar')
                self.time_game1.pack(expand=True, anchor='s')

                self.time_game0 = ttk.Progressbar(frame, length=int(0.45 * HEIGHT_MIN), orient=self.orient, maximum=20,
                                                  style='Left0.Vertical.TProgressbar')
                self.time_game0.pack(expand=True, anchor='n')

            else:
                self.discarded_chips1 = ttk.Progressbar(frame, length=int(0.45 * HEIGHT_MIN), orient=self.orient,
                                                        maximum=15, style='Right1.Vertical.TProgressbar')
                self.discarded_chips1.pack(expand=True, anchor='n')

                self.discarded_chips0 = ttk.Progressbar(frame, length=int(0.45 * HEIGHT_MIN), orient=self.orient,
                                                        maximum=15, style='Right0.Vertical.TProgressbar')
                self.discarded_chips0.pack(expand=True, anchor='s')

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