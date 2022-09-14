from cmath import e
import streamlit as st

main, info, cadastro = st.tabs(["Home","Info","Cadastro"])
with main:
    st.title("Ola Mundo Streamlit!😂👌")
    st.write("Teste teste!")
    st.markdown("## Subtitulo de **Seção**")
    st.code(
        """ 
        def somar(a,b)
            return a + b
    val1 = 10
    val2 = 12
    print(somar(val1,val2))    
        """,
        language = 'python'
    )

    st.code(
        """ 
    python -m streamlit run arquivo.py
        """,
        language = 'bash'
    )

    st.metric(
        label = "Total da Compra (R$): ",
        value = 105.92
    )
with info:
    def fui_apertado():
        print("Click!")

    def somar_dois(v1,v2):
        resultado = v1+v2
        st.session_state["Resultado"] = resultado

    numero1 = st.number_input(
        label = "Valor 1:",
        min_value = 0,
        max_value = 100,
    )

    numero2 = st.number_input(
        label = "Valor 2:",
        min_value = 0,
        max_value = 100,
    )


    st.button(
        label = "Clique aqui!",
        help = "Clique para ver os produtos!",
        on_click = somar_dois,
        kwargs = {"v1":numero1 , "v2":numero2}
    )

    if "Resultado" in st.session_state:
        st.metric(
            label = "Resultado ",
            value = st.session_state["Resultado"]
    )
    else:
        st.write("Nenhum calculo foi realizado!")

with cadastro:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(
            image = "assets./RushLoading.png",
            caption = "RUSHPKRL",
        )

    with col2:
        st.image(
            "https://images3.alphacoders.com/576/576239.jpg",
            caption = "Nissan R34",
        )

    with col3:
        st.image(
            image = "assets./m4.jpg",
            caption = "BMW M4",
        )

st.sidebar.title("Navegação")
