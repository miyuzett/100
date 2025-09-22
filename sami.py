
import streamlit as st

st.set_page_config(
    page_title="La escalofriante muerte del niño sam",
    page_icon=":worried:", 
    layout="centered",
)



pg = st.navigation(["Noticias_not.py","muy_serio.py", "muerte.py", "la_verdad.py"])
pg.run()
