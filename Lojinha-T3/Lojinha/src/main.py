from models.product_model import Product
from models.kart_checkout_model import Carrinho

import streamlit as st

if "Carrinho" not in st.session_state:
    st.session_state["carrinho"] = Carrinho()
if "Produtos" not in st.session_state:
    st.session_state["Produtos"] = [Product("Miojo","Comidas","Comidinha rapida","10,00","assets./miojo.png"),
            Product("Monster","Comidas","Melhor energético","15,00","assets./MosterMango.png"),
            Product("Starbucks","Comidas","Bebida quente para dias frios","20,00","assets./Starbucks.png"),
            Product("IPhone 14 Pro Max","Eletronicos","IPhone mais tecnologico","15000,00","assets./IPhone14ProMax.png"),
            Product("Samsung S22 Ultra", "Eletronicos","Samsung mais poderoso","8000,00","assets./S22Ultra.png"),
            Product("RTX4090 Aorus","Eletronicos","Placa de video do tamanho de um tijolo","15000,00","assets./RTX4090Aorus.png")]


# def password_check():
#     def password_try():
#         if(
#             st.session_state["username"] in 
#         )