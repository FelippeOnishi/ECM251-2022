from types import prepare_class
import streamlit as st

st.title("Carrinho: ")


# st.text_input(
#         label = "Informar CEP:"
#     )

# st.text_input(
#         label = "Informar cupom:"
#     )

# st.text(
#     "O valor do frete é: R$ " + "50,00"
# )

Payment = st.selectbox(
    "Forma de pagamento",
    ("Pix", "Boleto", "Cartão de crédito/débito", "PayPal"))

total = 250
Total_value = st.metric(      
        label = "Total da Compra",
        value = f"R$: {total}",
        )   


st.sidebar.title("Navegação")
st.sidebar.image("assets./FotoDePerfil.png")
st.sidebar.write("Felippe Onishi") # Nome conta
st.sidebar.write("Saldo na conta: R$ 125,50") # Saldo Conta
st.sidebar.button(
    label = "Produtos",
    help = "Clique para ver os produtos"
)
st.sidebar.button(
    label = "Carrinho",
    help = "Clique para ver o seu carrinho"
)
