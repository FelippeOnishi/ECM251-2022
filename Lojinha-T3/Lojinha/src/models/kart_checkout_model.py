from models.product_model import Product
class Carrinho():
    def __init__(self) -> None:
        self._products = []

    def total_value(self):
        total = 0.0
        for product in self._products:
            total += product.get_price()
        return total

    def fretecalc(self):
        preco = 0
        

    def kart_size(self):
        return len(self._products)

    def add2kart(self,product):
        self._products.append(product)

    def rem2kart(self,product):
        self._products.remove(product)
    
    def getTotal(self,product):
        return self._total