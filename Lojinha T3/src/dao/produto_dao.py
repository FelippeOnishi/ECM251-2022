import sqlite3
from src.models.produto import Produto

class ProdutoDAO:
    
    _instance = None

    def __init__(self) -> None:
        self._connect()


    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = ProdutoDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect("./databases/sqlite.db", check_same_thread = False)
        print("Banco de dados conectado")

    # Funcao pegar todos os produtos
    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(""""
        SELECT * FROM Produto;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Produto(id=resultado[0],name=resultado[1],price=resultado[2],imagem=resultado[3]))
        self.cursor.close()
        return resultados

    # Funcao inserir produto
    def inserir_produto(self, produto):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                INSERT INTO Produto(id,name,price,imagem)
                VALUES({produto.id},'{produto.name}','{produto.price}','{produto.imagem}');
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    # Funcao pegar produto ID
    def pegar_produto(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Produto
            WHERE id = '{id}';
        """)
        produto = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            produto = Produto(id=resultado[0], name=resultado[1], category=resultado[2], description=resultado[3], image=resultado[4], price=resultado[5])
        self.cursor.close()
        return produto

    # Funcao atualizar produto
    def atualizar_produto(self, produto):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Produto SET
                name = '{produto.name}',
                price = {produto.price},
                image = '{produto.image}',
                WHERE id = {produto.id};
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    # Funcao deletar produto
    def deletar_produto(self, id):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Produto
                WHERE id = {id};
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    # Funcao procurar produto por nome
    def search_all_for_name(self,name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Produto
            WHERE nome LIKE '{name}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Produto(id=resultado[0],name=resultado[1],price=resultado[2],imagem=resultado[3]))
        self.cursor.close()
        return resultados