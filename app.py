import streamlit as st
import folium
import json
from streamlit_folium import st_folium

# Membaca data dari file JSON
with open('data_sejarah.json', 'r') as f:
    data = json.load(f)

# Judul aplikasi
st.title("Peta Sejarah Kota Ternate - Maluku Utara")

# Dropdown untuk memilih kelurahan
kelurahan = st.selectbox("Pilih Kelurahan", [item["kelurahan"] for item in data])

# Menampilkan detail peristiwa
selected = next((item for item in data if item["kelurahan"] == kelurahan), None)
if selected:
    st.subheader(f"Sejarah {selected['kelurahan']}")
    st.write(f"Tahun: {selected['tahun']}")
    st.write(f"Peristiwa: {selected['peristiwa']}")
    st.write(f"Deskripsi: {selected['deskripsi']}")
    st.write(f"Sejarah Lokal: {selected['sejarah_lokal']}")

# Membuat peta dengan Folium
m = folium.Map(location=[-0.7833, 127.3633], zoom_start=12)

# Menambahkan marker untuk setiap kelurahan
for item in data:
    folium.Marker(
        location=[item["lat"], item["lon"]],
        popup=f"<b>{item['kelurahan']}</b><br>{item['tahun']} - {item['peristiwa']}<br>{item['deskripsi']}<br><br>{item['sejarah_lokal']}",
    ).add_to(m)

# Menampilkan peta
st_folium(m, width=700, height=500)
