import streamlit as st
from PIL import Image
from streamlit import session_state as ss

if 'user_id' not in ss:
    ss.user_id = None

pages = {
    "Gestão de Componentes": [
        st.Page("page_1.py", title="Pesquisar", icon="🌐"),
        st.Page("page_2.py", title="Adicionar", icon="⚙️"),
    ],
    "Gestão de Cotações": [
        st.Page("page_3.py", title="Pesquisar", icon="🌐"),
        st.Page("page_4.py", title="Adicionar", icon="⚙️"),
    ],
}

st.set_page_config(page_icon=Image.open("./images/p_logo.ico"),layout="wide")

if ss.user_id is None:
    col1,col2,col3 = st.columns(3)
    with col2:
        st.subheader("Página de login")
        st.divider()
        user_input = st.text_input("Username")
        password_input = st.text_input("Password", type="password")
        st.divider()
        if st.button("LOGIN", use_container_width=True, type="primary", key = "botao_login"):
            # Vai ler da BD a tabela do login e vai comparar se existe na tabela. Se sim, muda uma flag para nao fazer login de novo.
            if ss.botao_login:
                ss.user_id = user_input
            st.rerun()

else:
    pg = st.navigation(pages)
    pg.run()