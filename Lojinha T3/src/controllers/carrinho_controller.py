from src.models.carrinho import Carrinho

class CarrinhoController():
    def __init__(self):
        self._carrinho = Carrinho()

    def get_carrinho(self):
        return self._carrinho

    def add_produto(self,Produto,quantity):
        for i in range(len(self.get_carrinho().get_produto())):
            if self._carrinho.get_produto()[i][0].get_name() == Produto.get_name():
                self._carrinho.get_produto()[i][1] += quantity
                return
        self._carrinho._produto.append([Produto,quantity])

    def get_preco_total(self):
        total = 0
        for items in self._carrinho.get_produto():
            total += items[0].get_price() * items[1]
        return total