import ttkbootstrap as ttk
from tkinter import PhotoImage


class login():
    def __init__(self) -> None:
        self.janela_login = ttk.Window(
            title = "Login",
            size = (1440,1024),
            position = (100,100),
            minsize = (600,300),
            maxsize = (1800,900),
            alpha = 1.0,
        ) 
        self.janela_login.configure(bg='#F1E9DA')
        # self.janela_login.iconphoto(False,PhotoImage(file='../../images/FotoDePerfil.png'))
        self.janela_login.mainloop()




