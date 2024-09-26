import streamlit as st
# from openia import OpenAI

st.title("Dall-e 3")

st.write("Ceci est un exercice")

user_input = st.text_input ("Tapez votre texte : ")
st.write(user_input)

st.sidebar.write("Veuillez entrer la clé Open AI")
key_input = st.sidebar.text_input ("Clé Open AI: ")
st.write(key_input)

client = OpenAI(api_key= key_input,
               )

prompt = "une petite loutre entourée de coquillage"

image = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = image.data[0].url
print(image_url)

st.image(image.data[0].url)
