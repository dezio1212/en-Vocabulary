import streamlit as st
import requests
import random

# List kata contoh (bisa diganti dengan kata acak dari sumber lain)
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

st.set_page_config(page_title="Vocabulary App", layout="centered")
st.title("📘 Vocabulary Builder")

if st.button("🎲 Get Random Word"):
    random_word = random.choice(sample_words)
    result = get_definition(random_word)

    if "error" in result:
        st.error(result["error"])
    else:
        st.subheader(f"{result['word']} {result['phonetic']}")
        st.write(f"**Part of Speech:** {result['part_of_speech']}")
        st.write(f"**Definition:** {result['definition']}")
        if result["example"]:
            st.caption(f"_Example_: {result['example']}")
else:
    st.info("Klik tombol di atas untuk melihat kosakata acak.")
