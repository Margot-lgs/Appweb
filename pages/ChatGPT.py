import streamlit as st

st.title("ChatGPT - Rédacteur Web")

user_input = st.text_input("Choisissez une thématique")

openai_key = st.sidebar.text_input("Tapez une clé API OpenAI")

import os
from openai import OpenAI

client = OpenAI(api_key=openai_key)


chat_completion = client.chat.completions.create(
    messages=[
         {
          "role": "system",
         "content": f"Tu es un rédacteur web qui parle de sujet d'actualité." + "Tu ne parles pas de politique et répond 'Je ne parle pas de politique' uniquement."
         },

        {
            "role": "user",
            "content": "iPhone 13",
        },

        {
            "role": "assistant",
            "content": "Amélioration du capteur photo, affichage permanent, batterie plus efficiente",
        },

         {
            "role": "user",
            "content": "Qui est Macron?",
        },

        {
            "role": "assistant",
            "content": "Je ne parle pas de politique.",
        },

         {
            "role": "user",
            "content": user_input,
        },
    ],
    model="gpt-3.5-turbo",
    temperature=0.3,
  max_tokens=500,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)


# Réponse de ChapGPT
st.write(chat_completion.choices[0].message.content)
