import ttkbootstrap as ttk
from tkinter import PhotoImage

base = ttk.Window(
    title = "Minha GUI Maua",
    size = (1024,400),
    position = (100,100),
    minsize = (600,300),
    maxsize = (1800,900),
    alpha = 1.0,
)    

base.iconphoto(False,PhotoImage(file='Calculator.png'))
base.mainloop()