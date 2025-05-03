# 📘 English Vocabulary + Indonesian Translation App

A personal vocabulary learning web app built with **Python** and **Streamlit**, designed to look up English word definitions and translate them to **Bahasa Indonesia** using the **Google Cloud Translate API**. It also includes authentication and quota-aware API usage.

---

## ✨ Fitur Utama

* 🔍 Cari definisi kata berbahasa Inggris
* 📖 Tampilkan pengucapan, jenis kata, dan contoh kalimat
* 🌐 Terjemahkan definisi ke Bahasa Indonesia secara manual (on demand)
* 🔒 Akses terbatas: hanya pengguna dengan password yang bisa menggunakan aplikasi
* 💸 Bebas biaya: menggunakan layanan gratis dari DictionaryAPI dan Google Translate API (dengan kontrol billing)
* 🚀 Dideploy secara gratis di [Streamlit Cloud](https://streamlit.io/cloud)

---

## 🧰 Teknologi yang Digunakan

| Komponen               | Deskripsi                                                              |
| ---------------------- | ---------------------------------------------------------------------- |
| `Python`               | Bahasa utama                                                           |
| `Streamlit`            | Framework untuk membuat web app berbasis Python                        |
| `dictionaryapi.dev`    | API bebas untuk mendapatkan definisi dan contoh kata                   |
| `Google Translate API` | API resmi dari Google Cloud untuk menerjemahkan teks (en → id)         |
| `Session State`        | Menyimpan status dan hasil agar tidak hilang saat tombol ditekan       |
| `Secrets.toml`         | Menyimpan password dan API key secara aman (tidak di-commit ke GitHub) |

---

## 🚧 Struktur Folder

```
📁 en-vocabulary-app/
│
├── .streamlit/
│   └── secrets.toml          # Menyimpan API key dan password (jangan commit)
│
├── app.py                    # File utama aplikasi Streamlit
├── requirements.txt          # Daftar dependency untuk deploy
└── README.md                 # Dokumentasi proyek
```

---

## 🔐 Keamanan & Akses

* **Login**: Aplikasi hanya bisa diakses dengan password pribadi
* **API Key**: Disimpan secara aman di `secrets.toml` atau dashboard Streamlit Cloud
* **Quota**: Google Translate API dibatasi 10.000 karakter/hari untuk menghindari biaya

---

## 📦 Instalasi Lokal

1. **Clone repo**

   ```bash
   git clone https://github.com/username/en-vocabulary-app.git
   cd en-vocabulary-app
   ```

2. **Buat virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # atau .\venv\Scripts\activate di Windows
   ```

3. **Install dependency**

   ```bash
   pip install -r requirements.txt
   ```

4. **Buat secrets**

   ```toml
   # .streamlit/secrets.toml
   google_api_key = "YOUR_GOOGLE_API_KEY"
   app_password = "YOUR_APP_PASSWORD"
   ```

5. **Jalankan aplikasi**

   ```bash
   streamlit run app.py
   ```

---

## ☁️ Deploy ke Streamlit Cloud

1. Push ke GitHub
2. Masuk ke [streamlit.io/cloud](https://streamlit.io/cloud)
3. Klik **“New app”** → pilih repo kamu
4. Tambahkan Secrets:

   * `google_api_key`
   * `app_password`
5. Jalankan dan bagikan link ke dirimu sendiri

---

## 📊 Kendali Biaya Google Cloud

* Buat **Budget Alert** \$0.5 agar tidak terlampaui
* Batasi quota `Translation API` ke max 10.000 karakter/hari
* Pantau di [Google Cloud Billing](https://console.cloud.google.com/billing)

---

## 📑 Contoh Penggunaan

![Demo](https://github.com/username/en-vocabulary-app/assets/demo.gif)
*Tulis link demo atau upload GIF jika tersedia*

---

## 📌 Catatan

* Project ini cocok sebagai latihan kombinasi frontend-backend ringan dengan API
* Dapat dikembangkan menjadi:

  * Aplikasi pencatat kosakata
  * Bookmark kata yang dipelajari
  * Tambah history pencarian

---

## 📚 Lisensi

GNU GENERAL PUBLIC LICENSE — Silakan gunakan dan modifikasi untuk pembelajaran pribadi

---

### 🚀 Status: **Selesai & Berfungsi**
