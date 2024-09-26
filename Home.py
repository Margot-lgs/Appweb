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

# Sidebar
st.sidebar.title("Margot Langlais")

# Vidéo dans la sidebar
st.sidebar.video("https://www.youtube.com/watch?v=p0irVKBrUZU")

# Select bare
student_grad = st.selectbox("Selectionnez votre niveau d'étude", ["Bac", "Bac +2", "Bac +5"])

# Select slider
age = st.select_slider("Quel est votre âge ?", range(0,99))

if age >= 18: 
  st.write("Vous êtes majeur")
else:
  st.write("Vous êtes mineur")
