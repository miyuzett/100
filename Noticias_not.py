import streamlit as st

st.set_page_config( page_title="ATENCION: Noticia")
st.title("Hoy Noticias Not presenta:")
st.header("El niño sam..." , divider=True)
st.write("este es un sitio serio...")
st.badge("MUY SERIO!!!",color="orange")
st.write("En la noticia del dia de hoy nos adentraremos en la vida de este pobre diablo que a atormentado a todos con sus travesuras",":japanese_ogre:")


lol , mundo = st.columns(2)

mundo.image("Captura de pantalla 2025-08-04 155837 (2).png")
lol.write("El niño sam es una estrella del internet que alcanzo su fama en twitch al decir su famosa frase **-carambolas y relampiños dorados-**")
lol.write("Es conocido por sus chistosos clips de twitch en los cuales juega videojuegos de terror o con tematica oscura, los cuales causaron risa hasta el mas amargado")

lol.video("videoplayback.mp4")
lol.write("**uno de sus videos mas virales de su canal sam100pro**")

