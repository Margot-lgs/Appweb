import streamlit as st

st.title("Dall-e 3")

st.write("Ecrivez ce que vous voulez")

user_input = st.text_input ("Tapez votre texte : ")

st.write(user_input)
