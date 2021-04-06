import tkinter as tk
from _collections import deque


WIDTH, HEIGHT = 1200, 800
WIDTH_MIN, HEIGHT_MIN = 600, 400


class Point(tk.Canvas):
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

def points_init(frame0, frame1, width, height):
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

    points = []
    position = 0
    for fr in frames:
        point = Point(fr, width, height, position)
        point.pack(expand=True, fill=tk.BOTH)
        if position >= 12:  # drawing triangles based on position
            if not position % 2:
                point.create_polygon((0, 0), (point.wt, point.ht), (point.wt + point.wt, 0),
                                     fill='orange', outline='black', tag='cp')
            else:
                point.create_polygon((0, 0), (point.wt, 1.1 * point.ht), (point.wt + point.wt, 0),
                                     fill='sienna', outline='black', tag='cp')
        else:
            if not position % 2:
                point.create_polygon((0, point.height), (point.wt, point.height - point.ht),
                                     (point.wt + point.wt, point.height), fill='orange', outline='black', tag='cp')
            else:
                point.create_polygon((0, point.height), (point.wt, 1.1 * point.height - point.ht),
                                     (point.wt + point.wt, point.height), fill='sienna', outline='black', tag='cp')

        points.append(point)
        position += 1
    return points
