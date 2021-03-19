import tkinter as tk
from tkinter import ttk
from _collections import deque

import optlev
import board
import main


WIDTH, HEIGHT = 1200, 800
WIDTH_MIN, HEIGHT_MIN = 600, 400

"""The initial position of the chips on the board.
    Numbers greater > 0 show the location and the number of chips of 1 player by points.
    Numbers greater < 0 show the location and the number of chips of 2 player by points.
    0 in the list indicates that the position is empty.
    [-2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, -5, 5, 0, 0, 0, -3, 0, 0, 0, 0, 2]
"""

location_chips = deque([-2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, -5, 5, 0, 0, 0, -3, 0, -5, 0, 0, 0, 0, 2])


class FCanvas(tk.Canvas):
    """Passed canvas for each position."""
    def __init__(self, master, width, height, position):
        super().__init__(master, bg='Moccasin')
        self.master = master
        self.width = width
        self.height = height
        self.wt = self.width // 2
        self.ht = int(self.height * 3 / 4)
        self.position = position
        self.bind("<Configure>", self.change_resize)
        self.height = self.master.winfo_reqheight()
        self.width = self.master.winfo_reqwidth()

    def change_resize(self, event):
        """Resizing the canvas content resizing the main window."""
        wscale = event.width / self.width
        hscale = event.height / self.height
        self.width = event.width
        self.height = event.height
        self.scale("all", 0, 0, wscale, hscale)

    def draw_chips(self, quantity, color_0='snow', color_1='black'):
        """Initial drawing of the position of the chips."""
        if quantity > 0:
            self.chip_color = color_0
            self.tag = 'c0'
        if quantity < 0:
            self.chip_color = color_1
            self.tag = 'c1'

        x0 = 0.15 * self.width
        x1 = 0.85 * self.width
        for i in range(abs(quantity)):
            if self.position < 12:
                y0 = self.height - 0.7 * self.width - i * 0.7 * self.width
                y1 = self.height - i * 0.7 * self.width
            else:
                y0 = i * 0.7 * self.width
                y1 = 0.7 * self.width + i * 0.7 * self.width
            self.create_oval(x0, y0, x1, y1, fill=self.chip_color, tag=self.tag)



def canvases_init(frame0, frame1, width, height):
    """Sorts the array and loads the frames with canvases.
       Canvases are placed from the bottom-right corner of the screen counterclockwise.
    """
    stack0 = deque()
    stack1 = deque()
    frames = []
    f1 = f0 = 0
    for f in frame1.field_frames:
        if f1 < 6:
            stack1.appendleft(f)
        else:
            stack1.append(f)
        f1 += 1
    for fr in frame0.field_frames:
        if f0 < 6:
            stack0.appendleft(fr)
            frames.append(stack1.pop())
        else:
            stack0.append(fr)
        f0 += 1
    for _ in range(12):
        frames.append(stack0.pop())
    for _ in range(6):
        frames.append(stack1.pop())

    global canvases
    canvases = []
    position = 0
    for fr in frames:
        canvas = FCanvas(fr, width, height, position)
        canvas.pack(expand=True, fill=tk.BOTH)
        if position >= 12:  # drawing triangles based on position
            if not position % 2:
                canvas.create_polygon((0, 0), (canvas.wt, canvas.ht), (canvas.wt + canvas.wt, 0),
                                      fill='orange', outline='black', tag='cp')
            else:
                canvas.create_polygon((0, 0), (canvas.wt, 1.1 * canvas.ht), (canvas.wt + canvas.wt, 0),
                                      fill='sienna', outline='black', tag='cp')
        else:
            if not position % 2:
                canvas.create_polygon((0, canvas.height), (canvas.wt, canvas.height - canvas.ht),
                                      (canvas.wt + canvas.wt, canvas.height), fill='orange', outline='black', tag='cp')
            else:
                canvas.create_polygon((0, canvas.height), (canvas.wt, 1.1 * canvas.height - canvas.ht),
                                      (canvas.wt + canvas.wt, canvas.height), fill='sienna', outline='black', tag='cp')
        canvas.draw_chips(location_chips[position])
        canvases.append(canvas)
        position += 1

def color_chips(option):
    """"""
    for canvas in canvases:
        canvas.itemconfig('c0', fill=option.dict_options['color_0'])
        canvas.itemconfig('c1', fill=option.dict_options['color_1'])
