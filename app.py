import streamlit as st
import requests
import random

# Daftar kata contoh (bisa diganti)
sample_words = ["apple", "run", "beautiful", "strategy", "think", "language", "honest", "develop", "jump", "inspire"]

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        data = response.json()

        if isinstance(data, list):
            entry = data[0]
            word = entry["word"]
            phonetic = entry.get("phonetic", "")
            meaning_data = entry["meanings"][0]
            part_of_speech = meaning_data["partOfSpeech"]
            definition = meaning_data["definitions"][0]["definition"]
            example = meaning_data["definitions"][0].get("example", "")

            return {
                "word": word,
                "phonetic": phonetic,
                "part_of_speech": part_of_speech,
                "definition": definition,
                "example": example,
            }
        else:
            return {"error": data.get("message", "Word not found")}
    except Exception as e:
        return {"error": str(e)}

# Streamlit UI
st.set_page_config(page_title="Vocabulary App", layout="centered")
st.title("📘 Vocabulary Builder")

# Section 1: Cari kata sendiri
st.subheader("🔍 Cari definisi kata")
user_input = st.text_input("Masukkan kata dalam bahasa Inggris:")

if st.button("Cari"):
    if user_input.strip() == "":
        st.warning("Masukkan kata terlebih dahulu.")
    else:
        result = get_definition(user_input.strip())
        if "error" in result:
            st.error(result["error"])
        else:
            st.success(f"📖 Definisi untuk '{result['word']}'")
            st.write(f"**Pengucapan:** {result['phonetic']}")
            st.write(f"**Jenis Kata:** {result['part_of_speech']}")
            st.write(f"**Arti:** {result['definition']}")
            if result["example"]:
                st.caption(f"_Contoh penggunaan_: {result['example']}")

# Section 2: Dapatkan kata acak
st.markdown("---")
st.subheader("🎲 Atau dapatkan kata acak")

if st.button("Kata Acak"):
    random_word = random.choice(sample_words)
    result = get_definition(random_word)

    if "error" in result:
        st.error(result["error"])
    else:
        st.success(f"📖 Definisi untuk '{result['word']}'")
        st.write(f"**Pengucapan:** {result['phonetic']}")
        st.write(f"**Jenis Kata:** {result['part_of_speech']}")
        st.write(f"**Arti:** {result['definition']}")
        if result["example"]:
            st.caption(f"_Contoh penggunaan_: {result['example']}")
