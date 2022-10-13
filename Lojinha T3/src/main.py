import pickle
from pathlib import Path
from unicodedata import name

import streamlit as st 
import streamlit_authenticator as sauth
from src.controllers.carrinho_controller import CarrinhoController

from src.controllers.user_controller import UserController
from src.controllers.produto_controller import ProdutoController
import hashing

st.set_page_config(page_title="Lojinha",
 page_icon="https://w7.pngwing.com/pngs/328/211/png-transparent-store-art-illustration-angle-area-house-shop-angle-rectangle-shopping.png", 
 layout="wide")


names = UserController.get_names(UserController())
usernames = UserController.get_usernames(UserController())


try:
    file_path = Path(__file__).parent / "hashed_pw.pkl"
    file_path.open("rb")
except:
    hashing

with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = sauth.Authenticate(names, usernames, hashed_passwords,
    "Lojinha", "abcdef", cookie_expiry_days=7)


name, authentication_status, username = authenticator.login("Login", "main")
if authentication_status == False:
    st.error("Usuário e/ou senha inválido")
    st.session_state["Carrinho"] = CarrinhoController()

if authentication_status == None:
    st.warning("Digite seu usuário e senha")
    
    st.session_state["Carrinho"] = CarrinhoController()

if authentication_status:
    authenticator.logout("Sair")
    st.sidebar.markdown("***")
    st.sidebar.title(f"**Felippe's Store**")
    st.sidebar.markdown("***")
    st.sidebar.title(f"Bem vindo: *{name}*")

    
    tab1, tab2,tab3= st.tabs(["Alimentos", "Eletronicos","Carrinho"])

    with tab1: 
            st.title("Alimentos")
            st.markdown("***")
            st.text("")
            col1,col2 = st.columns(2,gap="large")

    with col1:
        index = 0
        Produto = ProdutoController.get_produto(ProdutoController(),index)
        c = st.container()
        c.markdown(f"## {Produto.get_name()}")
        c.image(f"{Produto.get_imagem()}", width = 300)
        c.markdown(f"## R${Produto.get_price()}")
        quantity0 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto, args = (Produto, quantity0))
    with col2:
        index = 1
        Produto = ProdutoController.get_produto(ProdutoController(),index)
        c = st.container()
        c.markdown(f"## {Produto.get_name()}")
        c.image(f"{Produto.get_imagem()}", width = 300)
        c.markdown(f"## R${Produto.get_price()}")
        quantity1 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto, args = (Produto, quantity1))
    with col1:
        index = 2
        Produto = ProdutoController.get_produto(ProdutoController(),index)
        c = st.container()
        c.markdown(f"## {Produto.get_name()}")
        c.image(f"{Produto.get_imagem()}", width = 300)
        c.markdown(f"## R${Produto.get_price()}")
        quantity2 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto, args = (Produto, quantity2))
    with col2:
        index = 3
        Produto = ProdutoController.get_produto(ProdutoController(),index)
        c = st.container()
        c.markdown(f"## {Produto.get_name()}")
        c.image(f"{Produto.get_imagem()}", width = 300)
        c.markdown(f"## R${Produto.get_price()}")
        quantity3 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto, args = (Produto, quantity3))

    with tab2: 
            st.title("Eletronicos")
            st.markdown("***")
            st.text("")
            col1,col2 = st.columns(2,gap="large")
    with col1:
        index = 4
        Produto = ProdutoController.get_produto(ProdutoController(),index)
        c = st.container()
        c.markdown(f"## {Produto.get_name()}")
        c.image(f"{Produto.get_imagem()}", width = 300)
        c.markdown(f"## R${Produto.get_price()}")
        quantity4 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto, args = (Produto, quantity4))

    with col2:
        index = 5
        Produto = ProdutoController.get_produto(ProdutoController(),index)
        c = st.container()
        c.markdown(f"## {Produto.get_name()}")
        c.image(f"{Produto.get_imagem()}", width = 300)
        c.markdown(f"## R${Produto.get_price()}")
        quantity5 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto, args = (Produto, quantity5))
    with col1:
        index = 6
        Produto = ProdutoController.get_produto(ProdutoController(),index)
        c = st.container()
        c.markdown(f"## {Produto.get_name()}")
        c.image(f"{Produto.get_imagem()}", width = 300)
        c.markdown(f"## R${Produto.get_price()}")
        quantity6 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto, args = (Produto, quantity6))
    with col2:
        index = 7
        Produto = ProdutoController.get_produto(ProdutoController(),index)
        c = st.container()
        c.markdown(f"## {Produto.get_name()}")
        c.image(f"{Produto.get_imagem()}", width = 300)
        c.markdown(f"## R${Produto.get_price()}")
        quantity7 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto, args = (Produto, quantity7))
    

    def novo_carrinho():
        st.session_state["Carrinho"] = CarrinhoController()

    with tab3:
            st.title("Carrinho")

            st.markdown("***")

            col1, col2, col3,col4 = st.columns(4,gap="large")
            col1.markdown("### Produtos")
            col2.markdown("### Preço")
            col3.markdown("### Quantidade")
        
            
            
            
            product_qtt = []
            product_names = []
            product_prices = []
            for produquantity in st.session_state["Carrinho"].get_carrinho().get_produto():
                product_names.append(produquantity[0].get_name())
                product_prices.append(produquantity[0].get_price())
                product_qtt.append(produquantity[1])
                    
            with col1:
                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### {product_names[i]}")
            with col2:
                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### R${product_prices[i]}")
            with col3:
                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### {product_qtt[i]}")
            with col4:
                c.button(label = f"Limpar carrinho", key = 1405, on_click= novo_carrinho)


            st.markdown("***")
            valor_total = st.session_state["Carrinho"].get_preco_total()
            st.markdown(f"## Total: ${valor_total:.3f}")
            option = st.selectbox(
            "Qual forma de pagamento?",
            ("Pix", "Boleto", "Cartão de crédito/débito", "PayPal"))
            st.write("Forma de pagamento selecionada:", option)
            c1 = st.container()
            c1.button(label = f"Efetuar Pagamento", key = 145, on_click= novo_carrinho)
            st.markdown("***")
                        