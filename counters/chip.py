import tkinter as tk
from tkinter import ttk
from random import randint
from _collections import deque




"""The initial position of the chips on the board.
    Numbers greater > 0 show the location and the number of chips of 1 player by points.
    Numbers greater < 0 show the location and the number of chips of 2 player by points.
    0 in the list indicates that the position is empty.
    [-2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, -5, 5, 0, 0, 0, -3, 0, 0, 0, 0, 2]
"""


class Counters:
    """"""

    def __init__(self, nickname):
        self.nickname = nickname
        if not self.nickname:
            self.color = 'snow'
            self.sum = 15
            self.k = 1
            self.tag = 'c0'
        else:
            self.color = 'black'
            self.sum = -15
            self.k = -1
            self.tag = 'c1'


    def random_chips(self, location_chips):
        s = 0
        while s != self.k * 15:
            a = self.k * randint(1, 5)
            i = randint(0, 23)
            if not location_chips[i]:
                s += a
                b = self.k * (self.k*15 - s)
                if b >= 0:
                    location_chips[i] = a
                else:
                    a = a + self.k * b
                    location_chips[i] = a
                    s = self.k * 15

    def draw_chips(self, points, location_chips):
        """Initial drawing of the position of the chips."""
        self.points = points
        i = 0
        for point in self.points:
            if self.k * location_chips[i] > 0:
                for n in range(abs(location_chips[i])):
                    x0 = 0.05 * point.width
                    x1 = 0.95 * point.width
                    if point.position < 12:
                        y0 = point.height - 0.8 * point.width - n * 0.8 * point.width
                        y1 = point.height - n * 0.8 * point.width
                    else:
                        y0 = n * 0.8 * point.width
                        y1 = 0.8 * point.width + n * 0.8 * point.width
                    point.create_oval(x0, y0, x1, y1, fill=self.color, tag=self.tag)
            i += 1

"""
    def color_chips(option):
        """"""
        for point in points:
            point.itemconfig('c0', fill=option.dict_options['color_0'])
            point.itemconfig('c1', fill=option.dict_options['color_1'])

#    def knock_chip(self):
#        \"""A chip knocks someone else's chip into the bar\"""
"""
