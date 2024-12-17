import streamlit as st

pages = {
    "Configurações": [
        st.Page("page_1.py", title="Login", icon="🔥"),
        st.Page("page_2.py", title="Pagina 2", icon="🔥"),
        st.Page("page_3.py", title="Pagina 3", icon="🔥"),
    ],
}


st.set_page_config(layout="wide")
pg = st.navigation(pages)
pg.run()