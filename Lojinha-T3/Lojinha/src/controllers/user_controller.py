from models.user_model import User

class UserController():
    def __init__(self) -> None:
        self.users = [
            User(name= "Felippe",email= "felippe.onishi@gmail.com",username="Feppo", password = "123321", cash_credits = 250),
            User(name= "Lucas",email= "Lucas@hotmail.com",username="Luscazi", password = "2424", cash_credits = 10),
            User(name= "Caio",email= "Caio@maua.com",username="Caio", password = "000111222", cash_credits = 100),
            User(name= "Carol",email= "Carol@gmail.com",username="Carol", password = "Carol123", cash_credits = 75),
            User(name= "Ahmad",email= "Ahmad@maua.br",username="Ahmad", password = "Arabe123", cash_credits = 125),
        ]
        
    def userValid(self,user):
        return user in self.users

    def userLogin(self,username, password):
        user_check = User(username = username, password = password)
        for user in self.users:
            if user.username == user_check.username and user.password == user_check.password:
                return True
        return False