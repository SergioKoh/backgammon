import tkinter as tk
from tkinter import ttk


class Option:
    """Game option selection"""
    def __init__(self, master, text, from_to):
        self.frame = master
        self.text = text
        self.from_, self.to = from_to
        self.v = self.from_

        self.style = ttk.Style()
        self.style.configure('Sun.Horizontal.TScale', relief=tk.SUNKEN, background='Moccasin')
        self.style.configure('Sl.Sun.Horizontal.TScale', sliderlength=140)
        self.style.configure('Sun.TLabel', font=('segoe print', 14), relief=tk.SUNKEN, background='Moccasin')
        self.style.configure('C.Sun.TLabel', background='black', foreground='white', anchor=tk.LEFT, width=6)
        self.style.configure('Co.Sun.TLabel', background='white', anchor=tk.LEFT, width=6)

        self.variable_text = tk.StringVar()
        if self.to == 2:
            self.variable_text.set('no')
            self.scale = ttk.Scale(self.frame, from_=self.from_, to=self.to, orient=tk.HORIZONTAL,
                                   style='Sl.Sun.Horizontal.TScale', length=280, command=self.change)
        else:
            self.variable_text.set(self.from_)
            self.scale = ttk.Scale(self.frame, from_=self.from_, to=self.to, orient=tk.HORIZONTAL,
                                   style='Sun.Horizontal.TScale', length=280, command=self.change)

        if self.text == '1 player piece':
            self.variable_text.set('black')
            self.label_color = ttk.Label(self.frame, textvariable=self.variable_text, style='C.Sun.TLabel')
        elif self.text == '2 player piece':
            self.variable_text.set('white')
            self.label_color = ttk.Label(self.frame, textvariable=self.variable_text, style='Co.Sun.TLabel')
        else:
            self.label_color = ttk.Label(self.frame, textvariable=self.variable_text, style='Sun.TLabel')

        self.label = ttk.Label(self.frame, text=self.text, style='Sun.TLabel')

        self.label.grid(column=0, row=0, sticky='w', padx=10, pady=10)
        self.label_color.grid(column=1, row=0, sticky='e', padx=10, pady=10)
        self.scale.grid(column=0, row=1, columnspan=2, sticky='nsew', padx=10, pady=10)

    def change(self, value_scale):
        """Changing options."""
        self.colors_1 = ('black', 'purple', 'yellow', 'green', 'aqua')
        self.colors_2 = ('white', 'gray', 'maroon',  'olive', 'blue')

        self.value_scale = value_scale
        if self.v != int(float(self.value_scale)):  # to remove instability with frequent changes to the style configuration
            self.v = int(float(self.value_scale))
            if self.from_:
                self.variable_text.set(self.v)
            elif self.to == 2 and self.v >= 1:
                self.variable_text.set('yes')
            elif self.to == 2 and self.v < 1:
                self.variable_text.set('no')
            elif self.text == '1 player piece':
                self.bg = self.colors_1[self.v]
                self.variable_text.set(self.bg)
                if self.bg == 'black':
                    self.style.configure('C.Sun.TLabel', background=self.bg, foreground='white')
                else:
                    self.style.configure('C.Sun.TLabel', background=self.bg, foreground='black')
            elif self.text == '2 player piece':
                self.bg = self.colors_2[self.v]
                self.variable_text.set(self.bg)
                self.style.configure('Co.Sun.TLabel', background=self.bg, foreground='black')


class OToplevel(tk.Toplevel):
    """Creating a dialog box for setting options."""
    def __init__(self, master, w, h):
        super().__init__()
        self.master = master
        self.width = w
        self.height = h
        self.title("Option")
        x, y = self.center_screen(w, h)
        self.geometry(f'{w}x{h}+{x}+{y}')
        self.resizable(False, False)
        self.lift(self.master)
        self.protocol("WM_DELETE_WINDOW", master.destroy)
        self.splitting_segments()

    def center_screen(self, w, h):
        """Centering the toplevel."""
        x = abs((self.winfo_screenwidth() - w)) // 2
        y = abs((self.winfo_screenheight() - h)) // 2
        return x, y

    def splitting_segments(self):
        """Splitting a dialog box into segments"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Option.TFrame', relief=tk.RAISED, background='SaddleBrown')
        self.style.configure('TButton', relief=tk.SUNKEN, font=('segoe print', 14), background='orange')
        self.style.map('TButton', background=[('active', 'Moccasin')])

        self.width_frame = self.width // 2
        self.height_frame = self.height // 4

        self.list_text = ('time per move(sec)', 'time per game(min)', 'bet size', 'match up to points',
                           '1 player piece', '2 player piece', 'Doubling cube')
        self.from_to = ((10, 30), (1, 20), (1, 100), (1, 15), (0, 4), (0, 4), (0, 2))
        self.options = []
        self.frames = []
        for i in range(2):
            self.columnconfigure(i, weight=1)
            for j in range(4):
                self.rowconfigure(j, weight=1)
                self.frame = ttk.Frame(self, style='Option.TFrame', width=self.width_frame, height=self.height_frame)
                self.frame.grid(column=i, row=j, sticky='nsew')
                if i == 0 and j < 4:
                    self.option = Option(self.frame, self.list_text[j], self.from_to[j])
                    self.options.append(self.option)
                if i == 1 and j < 3:
                    self.option = Option(self.frame, self.list_text[j+4], self.from_to[j+4])
                    self.options.append(self.option)
                else:
                    self.button = ttk.Button(self.frame, text="PLAY", style='TButton', command=self.start)
                    self.button.grid(sticky='e', padx=20, pady=25, ipadx=15)
                self.frames.append(self.frame)

    def start(self):
        """Closing the dialog window on creating a dictionary of options"""
        self.destroy()
        self.master.lift()
        self.state_options = []
        self.keys_option = ('time_move', 'time_game', 'bet_size', 'match_to_points',
                            'color_1', 'color_2', 'doubling_cube')
        i = 0
        for option in self.options:
            self.state_option = option.variable_text.get()
            self.state_options.append(self.state_option)
            i += 1
        self.dict_options = dict(zip(self.keys_option, self.state_options))





