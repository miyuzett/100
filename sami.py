
import streamlit as st

st.set_page_config(
    page_title="terror",
    page_icon=":worried:", 
    layout="centered",
)



pg = st.navigation(["pagina principal.py","Noticias_not.py","muy_serio.py", "muerte.py", "niño_sam.py" , "la_verdad.py" ])
pg.run()
