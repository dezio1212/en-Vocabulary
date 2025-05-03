import streamlit as st
import requests
import random

# 🔑 API Key Google Translate dari Secrets
api_key = st.secrets.get("google_api_key", "YOUR_API_KEY")
correct_password = st.secrets.get("app_password", "MY_SECRET_PASSWORD")

st.title("🔒 Akses Terbatas")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    password = st.text_input("Masukkan password:", type="password")
    if st.button("Masuk"):
        if password == correct_password:
            st.session_state["authenticated"] = True
            st.success("Akses diberikan!")
        else:
            st.error("Password salah.")
    st.stop()

# Setelah ini isi app normal kamu
st.success("Selamat datang! Kamu bisa menggunakan aplikasi ini.")

# 🧠 Fungsi ambil definisi dari DictionaryAPI.dev
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

# 🌐 Fungsi translate menggunakan Google Translate API
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

# 🖥️ UI Streamlit
st.set_page_config(page_title="Vocabulary App", layout="centered")
st.title("📘 Vocabulary + Indonesian Translation")

# Input kata dari user
st.subheader("🔍 Cari kata")
word_input = st.text_input("Masukkan kata (Bahasa Inggris):")

# --- Cari kata ---
if st.button("Cari"):
    if word_input.strip():
        result = get_definition(word_input.strip())
        if "error" in result:
            st.session_state["result"] = None
            st.error(result["error"])
        else:
            st.session_state["result"] = result
            st.session_state["translate"] = False  # reset status translate
    else:
        st.warning("Masukkan kata terlebih dahulu.")

# --- Tampilkan hasil definisi jika ada ---
if "result" in st.session_state and st.session_state["result"]:
    result = st.session_state["result"]
    st.success(f"📖 Definisi untuk: {result['word']}")
    st.write(f"**Pengucapan:** {result['phonetic']}")
    st.write(f"**Jenis Kata:** {result['part_of_speech']}")
    st.write(f"**Arti (EN):** {result['definition']}")
    if result["example"]:
        st.caption(f"_Contoh penggunaan_: {result['example']}")

    # --- Tombol terjemahan manual ---
    st.markdown("### 🇮🇩 Terjemahan ke Bahasa Indonesia")
    if st.button("Terjemahkan ke Bahasa Indonesia"):
        st.session_state["translate"] = True

    if st.session_state.get("translate"):
        translation = translate_to_indonesian(result["definition"], api_key)
        st.write(f"**Arti (ID):** {translation}")

    else:
        st.warning("Masukkan kata terlebih dahulu.")

# Pilih kata acak
sample_words = ["run", "think", "book", "create", "brilliant"]
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
        if result["example"]:
            st.caption(f"_Contoh penggunaan_: {result['example']}")

        st.markdown("### 🇮🇩 Terjemahan ke Bahasa Indonesia")
        if st.button("Terjemahkan kata acak"):
            translation = translate_to_indonesian(result["definition"], api_key)
            st.write(f"**Arti (ID):** {translation}")
