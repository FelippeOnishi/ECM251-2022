class Arvore:
    def __init__(self,nome) -> None:
        self.nome = nome
    def Ola(self):
        return f'Ola eu sou {self.nome}'

class Alface:
    def __init__(self,nome) -> None:
        self.nome = nome
    def Ola(self):
        return f'Fala Ae! Eu sou o {self.nome}'


if __name__ == "__main__":
    print('Olá')