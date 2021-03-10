import tkinter as tk
from tkinter import ttk


import board


WIDTH, HEIGHT = 1200, 800
WIDTH_MIN, HEIGHT_MIN = 600, 400





if __name__ == '__main__':
    """"""
    window = board.Window(WIDTH, HEIGHT)
    board.Window.draw_board(window)
    window.mainloop()
