import streamlit as st
import pandas as pd
from controller.page_1_c import *

df = pd.DataFrame(["No data"])

st.header("Pagina 1")
st.divider()

query_exemplo = """SELECT * FROM assembly.program
ORDER BY id ASC """


query = st.text_area("Inserir a query desejada", value = query_exemplo)
conn = st.connection("postgresql", type="sql") 
df = conn.query(query, ttl="10m") 


if st.button("Enviar Query"):
  conn = st.connection("postgresql", type="sql") 
  df = conn.query(query, ttl="10m") 


if not df.empty:
  st.data_editor(df, use_container_width=True)