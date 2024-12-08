import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Peta Sejarah Kelurahan")

# Pilihan kelurahan
kelurahan = st.selectbox("Pilih Kelurahan", ["Kelurahan Salero", "Kelurahan Ternate"])

# Menampilkan deskripsi kelurahan
if kelurahan == "Kelurahan Salero":
    st.subheader("Sejarah Kelurahan Salero")
    st.write("Kelurahan Salero terletak di Kota Ternate, Maluku Utara.")
    st.write("Ini adalah contoh kelurahan dengan data geoJSON yang digunakan untuk menampilkan peta.")

    # Membaca file GeoJSON untuk Kelurahan Salero
    gdf = gpd.read_file('kelurahan_salero.geojson')

    # Membuat plot peta menggunakan Matplotlib
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax, color='lightblue', edgecolor='black')

    # Menambahkan pengaturan tampilan pada peta
    ax.set_title('Peta Kelurahan Salero', fontsize=16)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    # Menampilkan peta di Streamlit
    st.pyplot(fig)

elif kelurahan == "Kelurahan Ternate":
    st.subheader("Sejarah Kelurahan Ternate")
    st.write("Kelurahan Ternate terletak di Kota Ternate, Maluku Utara.")
    st.write("Ini adalah contoh kelurahan lainnya.")

    # Placeholder untuk peta kelurahan lainnya (misalnya, bisa menggunakan GeoJSON lain)
    st.write("Peta Kelurahan Ternate akan ditampilkan di sini.")

