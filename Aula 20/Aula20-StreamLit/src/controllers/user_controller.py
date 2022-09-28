from models.user import User

class UserController():
    def __init__(self) -> None:
        # Carrega os dados dos usuarios
        self.users = [
            User(name="Joao",password="arroz",email="joao@gmail.com"),
            User(name="Joao2",password="arroz2",email="joao@hotmail.com"),
            User(name="Tais",password="petacular",email="tais_@gmail.com"),
            ]
