# Proyek Analisis Data - E-Commerce Dataset

## Deskripsi Proyek

Proyek ini bertujuan untuk melakukan analisis data terhadap dataset e-commerce tahun 2018 guna menjawab beberapa pertanyaan bisnis terkait distribusi penjual dan karakteristik produk.  

Analisis dilakukan menggunakan Python (Pandas, NumPy, Matplotlib, Seaborn) dan hasil visualisasi disajikan dalam bentuk dashboard interaktif menggunakan Streamlit.

---

## Struktur Project

```
├── dashboard.py
├── Proyek_Analisis_Data.ipynb
├── data/
│   └── (file dataset .csv)
├── requirements.txt
└── README.md
```

---

## Business Questions

1. Bagaimana distribusi penjual per negara bagian pada tahun 2018?
2. Bagaimana karakteristik berat produk berdasarkan kategori pada tahun 2018?

---

## Tools dan Library

- Python 
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Streamlit  

---




### 1. Buat Virtual Environment (Opsional)

```
python -m venv venv
```

Aktifkan environment:

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

---

### 2. Install Dependencies

Jika tersedia file requirements.txt:

```
pip install -r requirements.txt
```

Jika belum tersedia, install manual:

```
pip install pandas numpy matplotlib seaborn streamlit
```

---

### 3. Menjalankan Notebook (Opsional)

Untuk melihat proses analisis data:

```
jupyter notebook
```

Buka file:
```
Proyek_Analisis_Data.ipynb
```

---

### 4. Menjalankan Dashboard Streamlit

Pastikan berada di folder utama project, lalu jalankan:

```
streamlit run dashboard.py
```

Dashboard akan terbuka otomatis di browser pada alamat:

```
http://localhost:8501
```

---

## Fitur Dashboard

- Filter berdasarkan kategori produk
- Filter berdasarkan state seller
- Visualisasi distribusi penjual
- Visualisasi rata-rata berat produk per kategori
- Ringkasan metrik utama (total produk, jumlah kategori, jumlah seller)

---

## Insight Utama

- Distribusi penjual pada tahun 2018 sangat terkonsentrasi di wilayah tenggara Brasil, terutama São Paulo.
- Produk dengan berat tinggi hanya menyumbang sebagian kecil dari total produk, namun memiliki implikasi besar terhadap biaya logistik.

---

## Author

T. Armel Fahlevi
