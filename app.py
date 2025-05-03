import streamlit as st
import requests

st.set_page_config(page_title="en-Vocabulary App", layout="centered")

st.title("📘 en-Vocabulary App")

def get_word():
    try:
        # API 
        API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/<word>"
        response = requests.get(API_URL)
        data = response.json

        word = data["word"]
        meaning = data["meaning"]
        example = data.get("example", "")

        return word, meaning, example
    except Exception as e:
        return None, f"Error: {e}", ""
    
if st.button("🎲 Get New Word"):
    word, meaning, example = get_word()
    if word:
        st.subheader(word)
        st.write(f"**Meaning:** {meaning}")
        if example:
            st.caption(f"_Example_: {example}")
    else:
        st.error(meaning)
else:
    st.info("Klik tombol di atas untuk melihat kosakata baru.")