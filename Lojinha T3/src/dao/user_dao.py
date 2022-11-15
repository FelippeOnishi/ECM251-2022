import sqlite3
from src.models.user import User

class UserDAO:
    
    _instance = None

    def __init__(self) -> None:
        self._connect()


    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = UserDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect("./databases/sqlite.db", check_same_thread = False)
        print("Banco de dados conectado")


    # Funcao pegar usuario por username
    def pegar_user(self, username):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM User
            WHERE username = '{username}';
        """)
        user = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            user = User(username=resultado[0], password=resultado[1], name=resultado[2], email=resultado[3])
        self.cursor.close()
        return user


    # Funcao inserir usuarios
    def inserir_user(self, user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                INSERT INTO User (username, password, name, email)
                VALUES('{user.username}', '{user.password}', '{user.name}', '{user.email}');
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True


    # Funcao pegar todos usuarios
    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM User;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(username=resultado[0], password=resultado[1], name=resultado[2], email=resultado[3]))
        self.cursor.close()
        return resultados
        

    # Funcao atualizar usuario
    def atualizar_user(self, user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE User SET
                password = '{user.password}'
                email = '{user.email}',
                name = '{user.name}'
                WHERE username = '{user.username}';
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    # Funcao deletar usuario
    def deletar_user(self, username):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM User 
                WHERE username = '{username}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    # Funcao procurar usuario por nome
    def search_all_for_name(self,name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM User
            WHERE name LIKE '{name}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(username=resultado[0], password=resultado[1], name=resultado[2], email=resultado[3]))
        self.cursor.close()
        return resultados
