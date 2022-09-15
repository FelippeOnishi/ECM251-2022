import streamlit as st


st.title("Produtos: ")
page1, page2 = st.tabs(["Página 1","Página 2"])

with page1:
    product1, product2, product3 = st.columns(3)

    
    with product1:

        st.image(
            "assets./Produto1.png",
        )
        st.write("Valor: R$ 50,00")
        st.button(
            label = "Produto 1",
            help = "Clique aqui para mais informações"
        )
        

    with product2:
        st.image(
            "assets./Produto1.png",
        )
        st.write("Valor: R$ 50,00")
        st.button(
            label = "Produto 2",
            help = "Clique aqui para mais informações"
        )

    with product3:
        st.image(
            "assets./Produto1.png",
        )
        st.write("Valor: R$ 50,00")
        st.button(
            label = "Produto 3",
            help = "Clique aqui para mais informações"
        )

    product4, product5, product6 = st.columns(3)

    with product4:
        st.image(
            "assets./Produto1.png",
        )
        st.write("Valor: R$ 50,00")
        st.button(
            label = "Produto 4",
            help = "Clique aqui para mais informações"
        )

    with product5:
        st.image(
            "assets./Produto1.png",
        )
        st.write("Valor: R$ 50,00")
        st.button(
            label = "Produto 5",
            help = "Clique aqui para mais informações"
        )

    with product6:
        st.image(
            "assets./Produto1.png",
        )
        st.write("Valor: R$ 50,00")
        st.button(
            label = "Produto 6",
            help = "Clique aqui para mais informações"
        )

with page2:

    product7, product8, product9 = st.columns(3)

    
    with product7:

        st.image(
            "assets./Produto1.png",
        )
        st.write("Valor: R$ 50,00")
        st.button(
            label = "Produto 7",
            help = "Clique aqui para mais informações"
        )
        

    with product8:
        st.image(
            "assets./Produto1.png",
        )
        st.write("Valor: R$ 50,00")
        st.button(
            label = "Produto 8",
            help = "Clique aqui para mais informações"
        )

    with product9:
        st.image(
            "assets./Produto1.png",
        )
        st.write("Valor: R$ 50,00")
        st.button(
            label = "Produto 9",
            help = "Clique aqui para mais informações"
        )

    product10, product11, product12 = st.columns(3)

    with product10:
        st.image(
            "assets./Produto1.png",
        )
        st.write("Valor: R$ 50,00")
        st.button(
            label = "Produto 10",
            help = "Clique aqui para mais informações"
        )

    with product11:
        st.image(
            "assets./Produto1.png",
        )
        st.write("Valor: R$ 50,00")
        st.button(
            label = "Produto 11",
            help = "Clique aqui para mais informações"
        )

    with product12:
        st.image(
            "assets./Produto1.png",
        )
        st.write("Valor: R$ 50,00")
        st.button(
            label = "Produto 12",
            help = "Clique aqui para mais informações"
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

