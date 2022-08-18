class Item():
    def __init__(self, preco, nome, descricao = None):
        self._nome = nome
        self._preco = preco
        self._descicao = descricao

    # getters
    def get_nome(self):
        return self._nome

    def get_preco(self):
        return self._preco

    def get_descicao(self):
        return self._descicao

    #toString
    def __str__(self) -> str:
        return f'Nome: {self._nome} Preço: R${self._preco}'
        

