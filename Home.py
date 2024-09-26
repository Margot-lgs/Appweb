import streamlit as st

# Titre
st.title("Mon formulaire")

# Texte
st.write("Ceci est un formulaire de contact")

# Champ de saisi
user_input = st.text_input ("Tapez votre texte : ")

st.write(user_input)

# Image
st.image("https://tse3.mm.bing.net/th?id=OIP.Fzx8LSN_XuDpC_-Hw1mu6QHaKa&pid=Api")

# Vidéo
st.video

# Sidebar
st.sidebar.title("Margot Langlais")
