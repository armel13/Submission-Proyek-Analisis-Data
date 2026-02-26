import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import KBinsDiscretizer

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

@st.cache_data
def load_data():
    products = pd.read_csv('products_dataset.csv')
    sellers = pd.read_csv('sellers_dataset.csv')

    products = products.dropna(subset=['product_category_name']).copy()
    products = products.dropna(subset=['product_weight_g']).copy()

    return products, sellers

products, sellers = load_data()

st.title("E-Commerce Public Dashboard")
st.markdown("Dashboard interaktif analisis produk dan penjual dari Brazilian E-Commerce Dataset (Olist).")

# Sidebar
st.sidebar.header("Filter Data")

selected_category = st.sidebar.selectbox(
    "Pilih Kategori Produk",
    options=['Semua'] + sorted(products['product_category_name'].unique().tolist())
)

if selected_category != 'Semua':
    filtered_products = products[products['product_category_name'] == selected_category]
else:
    filtered_products = products

# Metric Summary
col_m1, col_m2, col_m3 = st.columns(3)

col_m1.metric("Total Produk", f"{len(filtered_products):,}")
col_m2.metric("Rata-rata Berat (g)", f"{filtered_products['product_weight_g'].mean():,.0f}")
col_m3.metric("Jumlah Kategori", f"{filtered_products['product_category_name'].nunique()}")

st.markdown("---")

# Visualisasi utama
col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribusi Berat Produk")
    fig, ax = plt.subplots(figsize=(8,4))
    sns.histplot(filtered_products['product_weight_g'], bins=50, kde=True, ax=ax)
    ax.set_xlabel("Berat (gram)")
    ax.set_ylabel("Frekuensi")
    st.pyplot(fig)

with col2:
    st.subheader("10 Kategori Produk Teratas")
    top_cats = filtered_products['product_category_name'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(8,4))
    sns.barplot(x=top_cats.values, y=top_cats.index, palette='viridis', ax=ax)
    ax.set_xlabel("Jumlah Produk")
    st.pyplot(fig)

# Analisis Seller
st.subheader("Sebaran Penjual per Negara Bagian")

state_counts = sellers['seller_state'].value_counts()
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=state_counts.index, y=state_counts.values, palette='rocket', ax=ax)
ax.set_xlabel("State")
ax.set_ylabel("Jumlah Penjual")
st.pyplot(fig)

# Rata-rata Berat
st.subheader("Rata-rata Berat per Kategori (Top 10)")

avg_weight = (
    filtered_products
    .groupby('product_category_name')['product_weight_g']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=avg_weight.values, y=avg_weight.index, palette='magma', ax=ax)
ax.set_xlabel("Rata-rata Berat (gram)")
st.pyplot(fig)

# Proporsi Kategori Berat
st.subheader("Proporsi Kategori Berat (Ringan/Sedang/Berat)")

products_bin = filtered_products.copy()

kbin = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='quantile')
products_bin['weight_bin'] = kbin.fit_transform(products_bin[['product_weight_g']]).astype(int)

bin_labels = {0: 'Ringan', 1: 'Sedang', 2: 'Berat'}
products_bin['weight_category'] = products_bin['weight_bin'].map(bin_labels)

weight_prop = products_bin['weight_category'].value_counts(normalize=True) * 100

fig, ax = plt.subplots()
ax.pie(weight_prop, labels=weight_prop.index, autopct='%1.1f%%', startangle=90)
ax.set_title("Proporsi Kategori Berat")
st.pyplot(fig)

st.caption("Data: Brazilian E-Commerce Public Dataset by Olist.")