import streamlit as st
from PIL import Image

prozis_icon = Image.open("./images/p_logo.ico")

pages = {
    "Gestor de Stock": [
        st.Page("page_1.py", title="Pagina 1", icon="🌐"),
        st.Page("page_2.py", title="Pagina 2", icon="⚙️"),
        st.Page("page_3.py", title="Pagina 3", icon="❔"),
    ],
}


st.set_page_config(page_icon=prozis_icon,layout="wide")
pg = st.navigation(pages)
pg.run()