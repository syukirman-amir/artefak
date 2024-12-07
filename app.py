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

# Membuat peta dengan Folium, menggunakan koordinat xmin, xmax, ymin, ymax untuk set zoom dan area peta
m = folium.Map(
    location=[(selected["ymin"] + selected["ymax"]) / 2, (selected["xmin"] + selected["xmax"]) / 2],
    zoom_start=15
)

# Menambahkan marker untuk kelurahan yang dipilih
folium.Marker(
    location=[selected["y"], selected["x"]],
    popup=f"<b>{selected['kelurahan']}</b><br>{selected['tahun']} - {selected['peristiwa']}<br>{selected['deskripsi']}<br><br>{selected['sejarah_lokal']}",
).add_to(m)

# Menambahkan batas area kelurahan menggunakan polygon
folium.Rectangle(
    bounds=[(selected["ymin"], selected["xmin"]), (selected["ymax"], selected["xmax"])],
    color="blue", weight=2, fill=True, fill_opacity=0.1
).add_to(m)

# Menampilkan peta
st_folium(m, width=700, height=500)
