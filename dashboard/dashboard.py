import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Bike Sharing", layout="wide")

# Load datasets
try:
    day_df = pd.read_csv('./data/day.csv')
    hour_df = pd.read_csv('./data/hour.csv')
    st.write("Data berhasil dimuat.")
except FileNotFoundError:
    st.error("File tidak ditemukan. Pastikan 'day.csv' dan 'hour.csv' ada di path yang benar.")
    st.stop()

# Display some sample data
st.write("Contoh data dari 'day.csv':")
st.write("Contoh data dari 'hour.csv':")
st.write(day_df.sample(5))
st.write(hour_df.sample(5))

# Visualization: Total Daily Rentals vs Temperature
st.write("### Total Penyewaan Harian vs Suhu")
st.write("Insight: Ada korelasi positif antara suhu yang lebih hangat dan peningkatan penyewaan sepeda.")
plt.figure(figsize=(10, 6))
sns.scatterplot(x=day_df['temp'], y=day_df['cnt'], hue=day_df['weathersit'], palette='coolwarm')
plt.title('Total Penyewaan Harian vs Suhu')
plt.xlabel('Suhu Ternormalisasi')
plt.ylabel('Total Penyewaan (cnt)')
plt.legend(title='Situasi Cuaca', loc='upper left')
st.pyplot(plt)

# Visualization: Hourly Rental Trend Throughout the Day
st.write("### Tren Penyewaan Sepeda per Jam")
st.write("Insight: Penyewaan sepeda cenderung lebih tinggi pada pagi dan sore hari, sesuai dengan waktu perjalanan kerja.")
plt.figure(figsize=(10, 6))
sns.lineplot(x=hour_df['hr'], y=hour_df['cnt'], ci=None)
plt.title('Tren Penyewaan Sepeda per Jam')
plt.xlabel('Jam dalam Sehari')
plt.ylabel('Total Penyewaan (cnt)')
plt.xticks(range(0, 24))
plt.grid(True)
st.pyplot(plt)

# Penyewaan berdasarkan hari kerja dan hari libur
st.write("### Penyewaan Berdasarkan Hari Kerja dan Libur")
weekday_holiday_df = day_df.groupby(['weekday', 'holiday']).agg({'cnt': 'mean'}).reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='weekday', y='cnt', hue='holiday', data=weekday_holiday_df, palette='Set2')
plt.title('Rata-rata Penyewaan Berdasarkan Hari Kerja dan Status Libur')
plt.xlabel('Hari dalam Minggu (0=Minggu, 6=Sabtu)')
plt.ylabel('Rata-rata Penyewaan (cnt)')
plt.legend(title='Libur', labels=['Tidak', 'Ya'])
plt.grid(True)
st.pyplot(plt)

# Penyewaan berdasarkan musim
st.write("### Penyewaan Berdasarkan Musim")
st.write("Insight: Penyewaan sepeda bervariasi tergantung musim, menunjukkan pengaruh cuaca pada penggunaan sepeda.")
season_df = day_df.groupby('season').agg({'cnt': 'mean'}).reset_index()
season_map = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
season_df['season'] = season_df['season'].map(season_map)
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=season_df, palette='viridis')
plt.title('Rata-rata Penyewaan Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Penyewaan (cnt)')
plt.grid(True)
st.pyplot(plt)
