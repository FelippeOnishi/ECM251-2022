import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

class MinhaUI():
    def _construir_base(self):
        janela = ttk.Window(
            title="Minha GUI Mauá",
            size= (1024,400),
            position= (100,100),
            minsize= (600,300),
            maxsize= (1800,900),
            alpha=1.0
        )
        janela.iconphoto(False, PhotoImage(file='Calculator.png'))
        return janela

    def __criar_botao(self,texto,acao):
        return ttk.Button(
            self.base,
            text="ACAO",
            bootstyle=(DEFAULT),
            command=acao
        )

    def __criar_texto(self, guardar):
        return ttk.Entry(
            self.base,
            textvariable=guardar
        )

    def __init__(self) -> None:
        self.base = self._construir_base()
        #Cria um botão
        self.bot = self.__criar_botao(texto="Ação", acao = self.mostrar_texto)
        self.bot.grid(row = 3, column = 2, padx = 5, pady = 5)
        self.valor_digitado = ""
        self.text = self.__criar_texto(guardar = self.valor_digitado)
        self.text.grid (row = 2, column = 1, padx = 5, pady = 5)
        self.base.mainloop()

    def mostrar_texto(self):
        print("Valor digitado: ", self.text.get())
        

# Funcao so para compreender o conceito de invocar por endereco
def mostrar_nome(nome):
        print(nome)

if __name__ == "__main__":
    f = mostrar_nome
    f("Felippe")

    app = MinhaUI()
    app.run()
