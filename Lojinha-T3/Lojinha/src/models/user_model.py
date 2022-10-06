class User():
    def __init__(self, name, email, username, password, cash_credits):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.cash_credits = cash_credits

    def __str__(self) -> str:
        return f"User(Nome: {self.name}, EMail: {self.email}, Username: {self.username}, Senha: {self.password}, Creditos: {self.cash_credits})"