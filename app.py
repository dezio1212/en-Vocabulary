import streamlit as st
import requests
import random

# Sample word list
sample_words = ["run", "think", "book", "create", "brilliant"]

# Google Translate API
def translate_to_indonesian(text, api_key):
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        "q": text,
        "source": "en",
        "target": "id",
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    if "data" in data:
        return data["data"]["translations"][0]["translatedText"]
    else:
        return f"Error: {data.get('error', {}).get('message', 'Terjadi kesalahan')}"

# Definition API
def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        data = response.json()
        if isinstance(data, list):
            entry = data[0]
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
                "example": example
            }
        else:
            return {"error": data.get("message", "Tidak ditemukan")}
    except Exception as e:
        return {"error": str(e)}

# Streamlit UI
st.set_page_config(page_title="Vocabulary + Translate", layout="centered")
st.title("📘 Vocabulary + Indonesian Translation")

# Get API Key from secrets
api_key = st.secrets.get("google_api_key", "YOUR_API_KEY")  # ganti dengan key kamu jika lokal

# Input
st.subheader("🔍 Cari kata")
word_input = st.text_input("Masukkan kata (Bahasa Inggris):")

if st.button("Cari"):
    if word_input.strip():
        result = get_definition(word_input.strip())

        if "error" in result:
            st.error(result["error"])
        else:
            st.success(f"📖 Definisi untuk: {result['word']}")
            st.write(f"**Pengucapan:** {result['phonetic']}")
            st.write(f"**Jenis Kata:** {result['part_of_speech']}")
            st.write(f"**Arti (EN):** {result['definition']}")

            # Translate to Indonesian
            translation = translate_to_indonesian(result["definition"], api_key)
            st.write(f"**Arti (ID):** {translation}")

            if result["example"]:
                st.caption(f"_Contoh penggunaan_: {result['example']}")
    else:
        st.warning("Masukkan kata terlebih dahulu.")

# Random word button
st.markdown("---")
if st.button("🎲 Kata acak"):
    random_word = random.choice(sample_words)
    st.info(f"Mengambil kata acak: **{random_word}**")
    result = get_definition(random_word)
    if "error" in result:
        st.error(result["error"])
    else:
        st.success(f"📖 Definisi untuk: {result['word']}")
        st.write(f"**Pengucapan:** {result['phonetic']}")
        st.write(f"**Jenis Kata:** {result['part_of_speech']}")
        st.write(f"**Arti (EN):** {result['definition']}")

        translation = translate_to_indonesian(result["definition"], api_key)
        st.write(f"**Arti (ID):** {translation}")

        if result["example"]:
            st.caption(f"_Contoh penggunaan_: {result['example']}")
