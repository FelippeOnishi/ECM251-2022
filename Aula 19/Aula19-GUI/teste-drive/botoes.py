import ttkbootstrap as ttk
from ttkbootstrap.constants import *
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

def acao_botao():
    print("Careca!")

# Criando um botão
ttk.Button(
    base,
    text="Ola Mundo!",
    bootstyle = "default",
    command = acao_botao
).pack(side = LEFT, padx = 10, pady = 5)

# Criando um segundo botão
bot2 = ttk.Button(
    base,
    text = "Segundo botão",
    bootstyle = (DANGER,OUTLINE),
    command = acao_botao
).pack(side = LEFT, padx = 20, pady = 20)

# Ponto de entrada da interface
base.mainloop()
