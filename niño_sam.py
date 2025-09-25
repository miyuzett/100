

import streamlit as st #importe streamlit a python y lo achique por comodidad

dio , so = st.columns(2) # cree 2 columnas para organizacion

so.header("entrevista al niño sam:", divider= True) # titulo
so.badge("que dira?",color="blue") # suspenso con un badge 


dio.image("ChatGPT Image 4 sept 2025, 15_55_24.png")#imagen importada desde chatgpt de la pelicula del niño sam
so.write("el niño sam se rie de los comentarios de la gente y se burla de ellos en television en vivo :eyes:")#contexto de la historia con un write para escribir, el resto de aqui es con write use un icono de la pagina que mando el mister y aqui empieza la entrevista
so.write("**estrevistador**: que te parecen los comentarios de tus fans asustados por tu pelicula?")
so.write("niño sam: para todos los que comentaron, NO ESTOY MUERTO jajajaja, tomenlo como otra de mis simples y divertidas bromas")
so.write("**entrevistador**: porque estabas en el medio de una isla desierta?")
so.write("niño sam: porque queria volver a el lugar donde di mis primeros pasos jijijiji") 
dio.write("**entrevistador**: porque no comentaste nada en tus redes cuando empezaron a comentar cosas sobre ti?")
dio.write("niño sam: porque no pense que se saldria de control, supuse que era una broma mas de mis fans")
dio.write("**entrevistador**: es cierto que estuviste confabulando con Azharx para que tu publico pensara que estabas muerto?")
dio.write("niño sam: quien es Azharx???")
so.image("yoyoo.png")#imagen sacada de google que la puse en la carpeta para que funcionara
