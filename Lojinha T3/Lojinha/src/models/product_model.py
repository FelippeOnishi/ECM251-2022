class Product():
    def __init__(self,name, tag, description, price, picture) -> None:
        self.name = name
        self.tag = tag 
        self.description = description
        self.price = price
        self.picture = picture

    def __str__(self) -> str:
        return f"Product(Produto: {self.name}, Tipo: {self.tag}, Descrição: {self.description}, Preço: {self.price})"
    
    def get_name(self):
        return self._name

    def get_tag(self):
        return self._tag

    def get_description(self):
        return self._description
    
    def get_price(self):
        return self._price
    
    def get_picture(self):
        return self._picture