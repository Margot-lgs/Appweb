import streamlit as st

st.title("Dall-e 3")

st.write("Ceci est un exercice")

user_input = st.text_input ("Tapez votre texte : ")
st.write(user_input)

st.sidebar.write("Veuillez entrer la clé Open AI")
user_input = st.sidebar.text_input ("Clé Open AI: ")
st.write(user_input)

client = OpenAI(api_key=OpenAIKEY)

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

st.image()
