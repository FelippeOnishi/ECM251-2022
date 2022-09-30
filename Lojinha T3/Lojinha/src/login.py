from turtle import width
import streamlit as st

with st.container():
    st.image(
        "assets./FotoDePerfil.png"
        )


    st.text_input(
        label = "Nome de usuário"
    )

    st.text_input(
        label = "Senha"
    )

    cadastro, login = st.columns(2)
    with cadastro:
        st.button(
            label = "Cadastre-se",
            help = "Clique aqui para realizar um novo cadastro",
            kwargs={
                'clicked_button_ix': 1, 'n_buttons': 3
            },
            ## Configurar para ir para tela de cadastro
        )

    with login:
        st.button(
            label = "Login",
            help = "Clique aqui para realizar o login",
            kwargs={
                'clicked_button_ix': 1, 'n_buttons': 3
            },
        )


