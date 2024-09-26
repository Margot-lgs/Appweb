from openai import OpenAI

import streamlit as st

st.title("Dall-e 3")
st.write("Ceci est un exercice")

# 1. Champ de saisie
user_input = st.text_input("Tapez votre texte :")

# 2. Champ de saisie dans la sidebar (pour la clé OpenAI)
st.sidebar.write("Veuillez entrer la clé Open AI")
key_input = st.sidebar.text_input ("Clé Open AI: ")

# 3. Intéraction avec OpenAI
client = OpenAI(
  api_key= key_input,
)

if user_input != "" :
  prompt = user_input
  image = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)
image_url = image.data[0].url

# 4. Affichage de l'image
st.image(image_url)
