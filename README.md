# Bike Sharing Data Analysis

Proyek ini bertujuan untuk menganalisis data penggunaan layanan Bike Sharing menggunakan Python. Analisis mencakup pembersihan data (data wrangling), eksplorasi, visualisasi, serta pembuatan dashboard interaktif menggunakan Streamlit.

## Struktur Folder

```plaintext
submission/
│── dashboard/
│   ├── dashboard.py          # Script untuk dashboard Streamlit
│   ├── main_data.csv         # Data utama untuk analisis
│
│── data/
│   ├── day.csv               # Data harian Bike Sharing
│   ├── hour.csv              # Data per jam Bike Sharing
│
│── notebook.ipynb            # Notebook Jupyter untuk analisis data
│── requirements.txt          # Daftar dependensi untuk menjalankan proyek
```

## Cara Menggunakan

### 1. Instalasi Dependensi
Sebelum menjalankan proyek, pastikan Anda telah menginstal dependensi yang dibutuhkan. Anda bisa menginstalnya dengan perintah berikut:

```sh
pip install -r requirements.txt
```

### 2. Menjalankan Jupyter Notebook
Untuk melakukan eksplorasi data secara interaktif, jalankan Jupyter Notebook dengan perintah:

```sh
jupyter notebook
```

Lalu buka file `notebook.ipynb` untuk melihat proses analisis dari data wrangling hingga kesimpulan.

### 3. Menjalankan Dashboard dengan Streamlit
Untuk melihat dashboard interaktif, jalankan perintah berikut:

```sh
streamlit run dashboard/dashboard.py
```

Setelah itu, buka browser dan akses **http://localhost:8501** untuk melihat dashboard.



