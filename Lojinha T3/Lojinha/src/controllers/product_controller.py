from models.product_model import Product

class ProductController():
    def __init__(self) -> None:
        self.products = [
            Product("Miojo","Comidas","Comidinha rapida","10,00","assets./miojo.png"),
            Product("Monster","Comidas","Melhor energético","15,00","assets./MosterMango.png"),
            Product("Starbucks","Comidas","Bebida quente para dias frios","20,00","assets./Starbucks.png"),
            Product("IPhone 14 Pro Max","Eletronicos","IPhone mais tecnologico","15000,00","assets./IPhone14ProMax.png"),
            Product("Samsung S22 Ultra", "Eletronicos","Samsung mais poderoso","8000,00","assets./S22Ultra.png"),
            Product("RTX4090 Aorus","Eletronicos","Placa de video do tamanho de um tijolo","15000,00","assets./RTX4090Aorus.png"),
    ]