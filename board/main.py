import tkinter as tk
from tkinter import ttk


import board
import optlev

WIDTH, HEIGHT = 1200, 800
WIDTH_MIN, HEIGHT_MIN = 600, 400





if __name__ == '__main__':
    """"""
    window = board.Window(WIDTH, HEIGHT)
    option = optlev.OToplevel(window, WIDTH_MIN, HEIGHT_MIN)
    window.mainloop()
