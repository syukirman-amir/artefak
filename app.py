import streamlit as st
import json
import prettymapp

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

    # Menghitung titik tengah dari batas koordinat (xmin, xmax, ymin, ymax)
    lat = (selected["ymin"] + selected["ymax"]) / 2  # Rata-rata latitude
    lon = (selected["xmin"] + selected["xmax"]) / 2  # Rata-rata longitude

    # Menggunakan Prettymaps untuk membuat peta
    ax = prettymapp.plot(
        (lat, lon),
        zoom=15,
        style='carto-positron',  # Gaya peta, bisa diganti dengan gaya lain
    )

    # Menampilkan peta di Streamlit
    st.pyplot(ax)
