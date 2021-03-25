import tkinter as tk
from tkinter import ttk

import board.fields as bf

WIDTH, HEIGHT = 1200, 800
WIDTH_MIN, HEIGHT_MIN = 600, 400


class HFrame(ttk.Frame):
    """Breaking the bar and board fields into frames."""

    def __init__(self, master, width, height):
        super().__init__(master)
        self.master = master
        self.style = ttk.Style()
        if width is master.width1_2:
            self.style.configure('Board.TFrame', borderwidth=1, relief=tk.RAISED, background='SaddleBrown')
            self.height = height // 9
            self.width = width
            self.bar_frames = []

            for i in range(5):
                if i == 0 or i == 4:
                    f = ttk.Frame(self, style='Board.TFrame', width=self.width, height=3*self.height)
                    f.grid(column=0, row=i, sticky='nsew')
                    tk.Grid.rowconfigure(self, index=i, weight=1)
                    self.bar_frames.append(f)
                else:
                    f = ttk.Frame(self, style='Board.TFrame', width=self.width, height=self.height)
                    f.grid(column=0, row=i, sticky='nsew')
                    tk.Grid.rowconfigure(self, index=i)
                    self.bar_frames.append(f)
            tk.Grid.columnconfigure(self, index=0, weight=1)
        else:
            self.style.configure('Field.TFrame', borderwidth=1, relief=tk.GROOVE, background="Moccasin")
            self.height = height // 2
            self.width = width // 6

            self.field_frames = []

            for j in range(2):
                for i in range(6):
                    f = ttk.Frame(self, style='Field.TFrame', width=self.width, height=self.height)
                    f.grid(column=i, row=j, sticky='nsew')
                    tk.Grid.columnconfigure(self, index=i, weight=1)
                    self.field_frames.append(f)
                    if not i:
                        tk.Grid.rowconfigure(self, index=j, weight=1)


class WFrame(ttk.Frame):
    """Vertical breakdown of the board into frames."""

    def __init__(self, master, width, height):
        super().__init__(master)
        self.master = master
        self.style = ttk.Style()
        self.style.configure('Board.TFrame', borderwidth=3, relief=tk.RAISED, background='SaddleBrown')
        self.height1 = height
        self.width1 = width
        self.width1_0 = int(0.017 * self.width1)
        self.width1_1 = int(0.449 * self.width1)
        self.width1_2 = int(0.068 * self.width1)
        self.width1_3 = int(0.449 * self.width1)
        self.width1_4 = self.width1 - self.width1_0 - self.width1_1 - self.width1_2 - self.width1_3

        self.frame1_0 = ttk.Frame(self, style='Board.TFrame', width=self.width1_0, height=self.height1)
        self.frame1_1 = HFrame(self, width=self.width1_1, height=self.height1)
        self.frame1_2 = HFrame(self, width=self.width1_2, height=self.height1)
        self.frame1_3 = HFrame(self, width=self.width1_3, height=self.height1)
        self.frame1_4 = ttk.Frame(self, style='Board.TFrame', width=self.width1_4, height=self.height1)
        self.frames = (self.frame1_0, self.frame1_1, self.frame1_2, self.frame1_3, self.frame1_4)

        i = 0
        for f in self.frames:
            f.grid(column=i, row=0, sticky='nsew')
            i += 1

        tk.Grid.rowconfigure(self, index=0, weight=1)
        tk.Grid.columnconfigure(self, index=1, weight=1)
        tk.Grid.columnconfigure(self, index=3, weight=1)

        self.orient = 'vertical'
        self.namber = 0
        Board.progress_bar(self.master, self.frame1_0, self.orient, self.namber)
        self.namber = 1
        Board.progress_bar(self.master, self.frame1_4, self.orient, self.namber)
        Board.bar(self.master, self.frame1_2)



class Board(tk.Tk):
    """Board initialization."""

    def __init__(self, w, h):
        super().__init__()
        self.title("Backgammon")
        self.width = w
        self.height = h
        x, y = self.center_screen(w, h)
        self.geometry(f'{w}x{h}+{x}+{y}')
        self.resizable(True, True)
        self.minsize(WIDTH_MIN, HEIGHT_MIN)
        self.draw_board()

    def center_screen(self, w, h):
        """Centering the window."""
        x = abs((self.winfo_screenwidth() - w)) // 2
        y = abs((self.winfo_screenheight() - h)) // 2
        return x, y

    def draw_board(self):
        """Board broken with frames into table cells."""
        self.style = ttk.Style()
        self.style.theme_use('clam')  # if these themes("vista" and "xpnative") are installed on the computer,
        # the progress bar color does not change, remains green.
        self.style.configure('Board.TFrame', borderwidth=3, relief=tk.RAISED, background='SaddleBrown')

        self.height0 = self.height2 = int(0.05 * self.height)
        self.height1 = self.height - self.height0 - self.height2

        self.frame0 = ttk.Frame(self, style='Board.TFrame', width=self.width)
        self.frame1 = WFrame(self, width=self.width, height=self.height1)
        self.frame2 = ttk.Frame(self, style='Board.TFrame', width=self.width)

        self.frame0.grid(column=0, row=0, sticky='nsew')
        self.frame1.grid(column=0, row=1, sticky='nsew')
        self.frame2.grid(column=0, row=2, sticky='nsew')

        tk.Grid.columnconfigure(self, index=0, weight=1)
        tk.Grid.rowconfigure(self, index=1, weight=1)

        self.progress_bar(self.frame0)
        self.progress_bar(self.frame2)
        self.points = bf.points_init(self.frame1.frame1_1, self.frame1.frame1_3,
                                     self.frame1.frame1_1.width, self.frame1.frame1_1.height)
        return self.points

    def progress_bar(self, frame, orient='horizontal', namber=0):
        """Two Progress bars, upper and lower, show the allotted time per move.
            The two right ones show the number of pieces removed from the board.
        """
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
            if self.frame is self.frame0:
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

    def bar(self, frame):
        """"""
        self.bar = frame
        self.bars = self.bar.bar_frames

        self.style.configure('Bar.TLabel', font=('vineta bt', 30), relief=tk.RAISED, background='SaddleBrown',
                             borderwidth=3, anchor=tk.CENTER, width=2)
        self.style.configure('P0.Bar.TLabel', foreground='snow')

        self.bar_1 = tk.Canvas(self.bars[0], width=self.bar.width, height=3 * self.bar.height, bg='SaddleBrown')
        self.point_1 = ttk.Label(self.bars[1], text='00', style='Bar.TLabel')
        self.doubling_cube = tk.Canvas(self.bars[2], width=self.bar.width, height=self.bar.height, bg='SaddleBrown')
        self.point_0 = ttk.Label(self.bars[3], text='00', style='P0.Bar.TLabel')
        self.bar_0 = tk.Canvas(self.bars[4], width=self.bar.width, height=3 * self.bar.height, bg='SaddleBrown')

        self.bar_1.pack(expand=True, fill=tk.BOTH)
        self.point_1.pack(expand=True, fill=tk.BOTH)
        self.doubling_cube.pack(expand=True, fill=tk.BOTH)
        self.point_0.pack(expand=True, fill=tk.BOTH)
        self.bar_0.pack(expand=True, fill=tk.BOTH)

        self.cube = self.doubling_cube.create_rectangle(3, 3, self.bar.width, self.bar.height, fill='orange',
                                                       outline='SaddleBrown', width=3, activedash=(5, 4))
        self.cube_digit = self.doubling_cube.create_text(self.bar.width // 2, self.bar.height // 2, text="64",
                                                         justify=tk.CENTER, font=('French Script MT', 60, 'bold'))

    def setting_bar(self):
        """"""
        self.style.configure('Bar.TLabel', foreground=self.options['color_1'])
        self.style.configure('P0.Bar.TLabel', foreground=self.options['color_0'])
        if self.options['doubling_cube'] == 'no':
            self.doubling_cube.itemconfig(self.cube_digit, state=tk.HIDDEN)
        else:
            self.doubling_cube.itemconfig(self.cube_digit, state=tk.NORMAL)
