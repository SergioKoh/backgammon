import tkinter as tk
from _collections import deque

BAR_WIDTH = 60

class Fields(tk.Canvas):
    """Passed canvas for each position."""
    def __init__(self, master):
        tk.Canvas.__init__(self, master)
        self.master = master
        self.configure(borderwidth=1, relief=tk.GROOVE, background="Moccasin")
        self.pack(fill="both", expand=True)
        self.bind("<Configure>", self.change_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()
        self.points = []

    def change_resize(self, event):
        """Resizing the canvas content resizing the main window."""
        wscale = (event.width - BAR_WIDTH) / (self.width - BAR_WIDTH)
        hscale = event.height / self.height
        self.width = event.width
        self.height = event.height
        self.scale('house', BAR_WIDTH, 0, wscale, hscale)
        self.scale('yard', 0, 0, wscale, hscale)
        self.draw_triangle()
        self.draw_bar(event)

    def draw_triangle(self):
        """"""
        if not self.points:
            w_field = (self.width - BAR_WIDTH - 3) / 2
            h_field = self.height / 2
            w_triangle = w_field / 6
            y0_0, y0_1 = self.height, 0
            x0_0, x0_1 = self.width, self.width - w_field - BAR_WIDTH
            x0_2, x0_3 = 0,  w_field + BAR_WIDTH
            tag0, tag1 = 'house', 'yard'
            k_h0, k_h1 = 1.1, 1 / 1.1
            k_h0_even, k_h1_even = 1.2, 1 / 1.2
            X0Y0 = ((x0_0, y0_0, k_h0, k_h0_even, tag0), (x0_1, y0_0, k_h0, k_h0_even, tag1),
                    (x0_2, y0_1, k_h1, k_h1_even, tag1), (x0_3, y0_1, k_h1, k_h1_even, tag0))
            for x00, y0, k_h, k_h_even, tag in X0Y0:
                y2 = y0
                for i in range(6):
                    if i % 2:
                        fill = 'sienna'
                        y1 = k_h_even * h_field
                    else:
                        y1 = k_h * h_field
                        fill = 'orange'
                    k = 1 if y0 else -1
                    x0 = x00 - k * i * w_triangle
                    x1 = x0 - k * w_triangle / 2
                    x2 = x0 - k * w_triangle

                    point = self.create_polygon(x0, y0, x1, y1, x2, y2, fill=fill, tag=tag)
                    self.points.append(point)

    def draw_bar(self, event=False):
        """"""
        x0 = (self.width - BAR_WIDTH) / 2
        y0 = 0
        x1 = (self.width + BAR_WIDTH) / 2
        y1 = self.height
        if not event:
            self.bar = self.create_rectangle(x0, y0, x1, y1, fill='SaddleBrown', outline='white',
                                         width=3, activedash=(5, 4), tag='bar')
        else:
            self.coords(self.bar, x0, y0, x1, y1)

    def draw_fields(self):
        pass
#    return points
