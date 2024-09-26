from openia import OpenAI

import streamlit as st

st.title("Dall-e 3")
st.write("Ceci est un exercice")

st.sidebar.write("Veuillez entrer la clé Open AI")
key_input = st.sidebar.text_input ("Clé Open AI: ")

client = OpenAI(
  api_key= key_input,
)

user_input = st.text_input("Tapez votre texte :")

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

st.image(image_url)
