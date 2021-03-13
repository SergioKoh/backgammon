import tkinter as tk
from tkinter import ttk
from _collections import deque

WIDTH, HEIGHT = 1200, 800

"""The initial position of the chips on the board.
    Numbers greater > 0 show the location and the number of chips of 1 player by points.
    Numbers greater < 0 show the location and the number of chips of 2 player by points.
    0 in the list indicates that the position is empty.
    [-2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, -5, 5, 0, 0, 0, -3, 0, 0, 0, 0, 2]
"""

location_chips = [-2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, -5, 5, 0, 0, 0, -3, 0, -5, 0, 0, 0, 0, 2]


class FCanvas(tk.Canvas):
    """"""

    def __init__(self, master, width, height):
        super().__init__(master, bg='Moccasin')
        self.master = master
        self.width = width
        self.height = height
        self.wt = self.width // 2
        self.ht = int(self.height * 3 / 4)


    def change_resize(self, event):
        pass

    def draw_top(self, position, quantity):
        """"""
        if not position % 2:
            self.create_polygon((0, 0), (self.wt, self.ht), (self.wt + self.wt, 0),
                            fill='orange', outline='black')
        else:
            self.create_polygon((0, 0), (self.wt, 1.1*self.ht), (self.wt + self.wt, 0),
                                fill='sienna', outline='black')
        if not quantity:
            pass
        elif quantity > 0:
            chip_color = 'white'
        else:
            chip_color = 'black'

    def draw_botton(self, position, quantity=0):
        """"""
        if not position % 2:
            self.create_polygon((0, 1.1*self.height), (self.wt, 1.1*self.height - 1.1*self.ht),\
                                (self.wt + self.wt, 1.1*self.height), fill='orange', outline='black')
        else:
            self.create_polygon((0, 1.1*self.height), (self.wt, 1.1*self.height - self.ht),\
                                (self.wt + self.wt, 1.1*self.height), fill='sienna', outline='black')
        if not quantity:
            pass
        elif quantity > 0:
            chip_color = 'white'
        else:
            chip_color = 'black'



def canvases_init(frame0, frame1, width, height):
    """Sorts the array and loads the frames with canvases"""
    stack0 = deque()
    stack1 = deque()

    frames = []
    f1 = f0 = 0
    for f in frame1.frames:
        if f1 < 6:
            stack1.appendleft(f)
        else:
            stack1.append(f)
        f1 += 1
    for fr in frame0.frames:
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


    canvases = []

    for fr in frames:
        canvas = FCanvas(fr, width, height)
        canvas.pack(expand=True, fill=tk.BOTH)
        canvases.append(canvas)

    position = 0
    for canvas in canvases:
        if position < 12:
            canvas.draw_botton(position, 0)
        else:
            canvas.draw_top(position, 0)
        position += 1
