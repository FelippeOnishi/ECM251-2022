import streamlit as st



st.text_input(
        label = "Nome de usuário"
    )

st.text_input(
        label = "Email"
    )

st.text_input(
        label = "Senha"
    )

st.text_input(
        label = "Confirmação Senha"
    )

st.file_uploader("Escolher foto de perfil")

st.button(
    label = "Cadastre-se",
    help = "Clique aqui para realizar um novo cadastro",
    ## Configurar para ir para tela de cadastro
)