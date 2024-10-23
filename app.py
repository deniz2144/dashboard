import streamlit as st
import pandas as pd
import numpy as np

st.title('Basit Konut Fiyatları Dashboard')

# Veriyi Oluşturma
data = pd.DataFrame({
    'fiyat': np.random.randint(200000, 800000, 100),
    'oda sayısı': np.random.randint(1, 5, 100),
    'mahalle': np.random.choice(['A', 'B', 'C', 'D'], 100)
})

# Mahalleleri Sidebar'dan Seçme
mahalleler = data['mahalle'].unique()
secilen_mahalle = st.sidebar.selectbox("Mahalle Seçin", mahalleler)

# Oda Sayısı Filtreleme
oda_sayilari = sorted(data['oda sayısı'].unique())
secilen_oda_sayisi = st.sidebar.selectbox("Oda Sayısını Seçin", oda_sayilari)

# Seçilen Mahalle ve Oda Sayısına Göre Filtreleme
filtrelenmis_veri = data[(data['mahalle'] == secilen_mahalle) & (data['oda sayısı'] == secilen_oda_sayisi)]
st.write(f"Seçilen Mahalle: {secilen_mahalle}, Oda Sayısı: {secilen_oda_sayisi}")
st.write(filtrelenmis_veri)

# İstatistik Bilgileri Gösterme
st.subheader("İstatistikler")
st.write(f"Minimum Fiyat: {filtrelenmis_veri['fiyat'].min()}")
st.write(f"Maksimum Fiyat: {filtrelenmis_veri['fiyat'].max()}")
st.write(f"Ortalama Fiyat: {filtrelenmis_veri['fiyat'].mean()}")

# Bar Grafik Çizdirme
st.subheader("Fiyat Dağılımı (Bar Grafik)")
st.bar_chart(filtrelenmis_veri['fiyat'])

# Scatter Plot ile Fiyat ve Oda Sayısı İlişkisi
st.subheader("Fiyat ve Oda Sayısı İlişkisi (Scatter Plot)")
st.scatter_chart(filtrelenmis_veri[['oda sayısı', 'fiyat']])
