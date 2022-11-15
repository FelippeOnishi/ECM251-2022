
from src.models.produto import Produto
from src.dao.produto_dao import ProdutoDAO

class ProdutoController():
    def __init__(self) -> None:
        pass

    def pegar_produto(self, id) -> Produto:
            produto = ProdutoDAO.get_instance().pegar_produto(id)
            return produto

    def inserir_produto(self, produto) -> bool:
        try:
            ProdutoDAO.get_instance().inserir_produto(produto)
        except:
            return False
        return True

    def pegar_todos_produtos(self) -> list[Produto]:
        products = ProdutoDAO.get_instance().get_all()
        return products
    
    def atualizar_produto(self, produto) -> bool:
        return ProdutoDAO.get_instance().atualizar_produto(produto)

    def deletar_produto(self, id) -> bool:
        return ProdutoDAO.get_instance().deletar_item(id)

    def buscar_todos_produtos_name(self, name) -> list[Produto]:
        produtos = ProdutoDAO.get_instance().search_all_for_name(name)
        return produtos

