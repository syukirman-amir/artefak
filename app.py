import streamlit as st
import json
import prettymaps
import matplotlib.pyplot as plt
import numpy as np

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

    # Membuat peta menggunakan Prettymaps
    lat = (selected["ymin"] + selected["ymax"]) / 2  # Rata-rata latitude
    lon = (selected["xmin"] + selected["xmax"]) / 2  # Rata-rata longitude

    # Gunakan Prettymaps untuk membuat peta
    ax = prettymaps.plot(
        (lat, lon),
        zoom=15,
        style='carto-positron',  # Gaya peta, Anda bisa menggantinya dengan gaya lain
        bgcolor='white',  # Latar belakang peta
        markers=[(lat, lon)],
        figsize=(10, 10)
    )

    # Menampilkan peta di Streamlit menggunakan matplotlib
    st.pyplot(ax)
