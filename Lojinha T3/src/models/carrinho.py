class Carrinho():
    def __init__(self):
        self._produto=[]
        
    def get_produto(self):
        return self._produto

    def __str__(self):
        return self._produto