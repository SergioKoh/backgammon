from tkinter import *

root = Tk()
root.geometry('150x150')

Label(bg='white').place(x=10, y=10,
                    width=50, height=30)
Label(bg='green').place(x=10, y=50,
                    relwidth=0.3, relheight=0.15)

root.mainloop()
