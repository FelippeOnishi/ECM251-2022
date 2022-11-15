class Produto():
    def __init__(self, id, name, price, imagem):
        self._id = id
        self._name = name
        self._price = price
        self._imagem = imagem

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_imagem(self):
        return self._imagem

    def __str__(self):
        return f'Produto(_name:{self._name}, _price:{self._price}, _url:{self._imagem})'