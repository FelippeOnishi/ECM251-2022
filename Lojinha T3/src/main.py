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
 page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEaTQkx1Tmb5nzAOohGbC42CSN748eFtReMA&usqp=CAU")


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
    "Lojinha", "abcdef", cookie_expiry_days=14)


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
        st.markdown(f"## {Produto.get_name()}")
        st.image(f"{Produto.get_imagem()}", width = 300)
        st.markdown(f"## R${Produto.get_price()}")
        st.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto)
    with col2:
        index = 1
        Produto = ProdutoController.get_produto(ProdutoController(),index)
        st.markdown(f"## {Produto.get_name()}")
        st.image(f"{Produto.get_imagem()}", width = 300)
        st.markdown(f"## R${Produto.get_price()}")
        st.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto)
    with col1:
        index = 2
        Produto = ProdutoController.get_produto(ProdutoController(),index)
        st.markdown(f"## {Produto.get_name()}")
        st.image(f"{Produto.get_imagem()}", width = 300)
        st.markdown(f"## R${Produto.get_price()}")
        st.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto)
    with col2:
        index = 3
        Produto = ProdutoController.get_produto(ProdutoController(),index)  
        st.markdown(f"## {Produto.get_name()}")
        st.image(f"{Produto.get_imagem()}", width = 300)
        st.markdown(f"## R${Produto.get_price()}")
        st.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto)

    with tab2: 
            st.title("Eletronicos")
            st.markdown("***")
            st.text("")
            col1,col2 = st.columns(2,gap="large")
    with col1:
        index = 4
        Produto = ProdutoController.get_produto(ProdutoController(),index)
        st.markdown(f"## {Produto.get_name()}")
        st.image(f"{Produto.get_imagem()}", width = 300)
        st.markdown(f"## R${Produto.get_price()}")
        st.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto)

    with col2:
        index = 5
        Produto = ProdutoController.get_produto(ProdutoController(),index)     
        st.markdown(f"## {Produto.get_name()}")
        st.image(f"{Produto.get_imagem()}", width = 300)
        st.markdown(f"## R${Produto.get_price()}")
        st.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto)
    with col1:
        index = 6
        Produto = ProdutoController.get_produto(ProdutoController(),index)       
        st.markdown(f"## {Produto.get_name()}")
        st.image(f"{Produto.get_imagem()}", width = 300)
        st.markdown(f"## R${Produto.get_price()}")
        st.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto)
    with col2:
        index = 7
        Produto = ProdutoController.get_produto(ProdutoController(),index)
        st.markdown(f"## {Produto.get_name()}")
        st.image(f"{Produto.get_imagem()}", width = 300)
        st.markdown(f"## R${Produto.get_price()}")
        st.button(label = f"Adicionar ao carrinho", key = index, on_click= st.session_state["Carrinho"].add_produto)
    

    def novo_carrinho():
        st.session_state["Carrinho"] = CarrinhoController()

    with tab3:
            st.title("Carrinho")

            st.markdown("***")

            col1, col2, col3,col4 = st.columns(4,gap="large")
            col1.markdown("### Produtos")
            col2.markdown("### Preço")
            col3.markdown("### Quantidade")
        
            
            
            
            produto_quantidade = []
            produto_nome = []
            produto_preco = []
            for produquantity in st.session_state["Carrinho"].get_carrinho().get_produto():
                produto_nome.append(produquantity[0].get_name())
                produto_preco.append(produquantity[0].get_price())
                produto_quantidade.append(produquantity[1])
                    
            with col1:
                
                for i in range(len(produto_nome)):
                    st.markdown(f"#### {produto_nome[i]}")
            with col2:
                
                for i in range(len(produto_nome)):
                    st.markdown(f"#### R${produto_preco[i]}")
            with col3:
                
                for i in range(len(produto_nome)):
                    st.markdown(f"#### {produto_quantidade[i]}")
            with col4:
                st.button(label = f"Limpar carrinho", key = 1405, on_click= novo_carrinho)


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
                        