import tkinter as tk
from tkinter import ttk


class Option:
    def __init__(self, master, text, from_to):
        self.frame = master
        self.text = text
        self.from_, self.to = from_to

        self.style = ttk.Style()
        self.style.configure('Sun.Horizontal.TScale', borderwidth=3, relief=tk.SUNKEN, padding=6,
                             background='Moccasin')
        self.style.configure('Sun.TLabel', font=('segoe print', 14), borderwidth=3, relief=tk.SUNKEN, padding=3,
                             background='Moccasin')
        self.varl = tk.IntVar()

        self.label = ttk.Label(self.frame, text=self.text, style='Sun.TLabel')
        self.label_var = ttk.Label(self.frame, text=self.from_, textvariable=self.varl, style='Sun.TLabel')
        self.scale = ttk.Scale(self.frame, from_=self.from_, to=self.to, orient=tk.HORIZONTAL,
                               style='Sun.Horizontal.TScale', length=280, command=self.change)

        self.label.grid(column=0, row=0, sticky='w', padx=10, pady=10)
        self.label_var.grid(column=1, row=0, sticky='e', padx=10, pady=10)
        self.scale.grid(column=0, row=1, columnspan=2, sticky='nsew', padx=10, pady=10)

    def change(self, val):
        """"""
        v = int(float(val))
        self.varl.set(v)


class OToplevel(tk.Toplevel):
    """"""
    def __init__(self, w, h):
        super().__init__()
        self.width = w
        self.height = h
        self.title("Option")
        x, y = self.center_screen(w, h)
        self.geometry(f'{w}x{h}+{x}+{y}')
        self.resizable(False, False)
        self.lift(self.master)
        self.draw_option()

    def center_screen(self, w, h):
        """Centering the toplevel."""
        x = abs((self.winfo_screenwidth() - w)) // 2
        y = abs((self.winfo_screenheight() - h)) // 2
        return x, y



    def draw_option(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Option.TFrame', relief=tk.RAISED, background='SaddleBrown')
        self.width_frame = self.width // 2
        self.height_frame = self.height // 4

        self.list_text = ('time per move(sec.)', 'time per game(min)', 'bet size', 'match up to points',
                           '1 players piece color', '2 players piece color', 'Doubling cube')
        self.from_to = ((10, 30), (1, 20), (1, 100), (1, 15), (1, 10), (1, 10), (1, 2))
        self.options = []
        self.frames = []
        for i in range(2):
            for j in range(4):
                self.frame = ttk.Frame(self, style='Option.TFrame', width=self.width_frame, height=self.height_frame)
                self.frame.grid(column=i, row=j, sticky='nsew')
                if i == 0 and j < 4:
                    self.option = Option(self.frame, self.list_text[j], self.from_to[j])
                    self.options.append(self.option)
                if i == 1 and j < 3:
                    self.option = Option(self.frame, self.list_text[j+4], self.from_to[j+4])
                    self.options.append(self.option)
                else:pass
                self.frames.append(self.frame)





