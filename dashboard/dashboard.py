import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Bike Sharing", layout="wide")

# Load datasets
try:
    day_df = pd.read_csv('./data/day.csv')
    hour_df = pd.read_csv('./data/hour.csv')
    st.write("Data loaded successfully.")
except FileNotFoundError:
    st.error("File not found. Please make sure 'day.csv' and 'hour.csv' are in the correct path.")
    st.stop()

# Display some sample data
st.write("Sample data from 'day.csv':")
st.write(day_df.sample(5))

# Visualization
st.write("### Total Daily Rentals vs Temperature")
plt.figure(figsize=(10, 6))
sns.scatterplot(x=day_df['temp'], y=day_df['cnt'], hue=day_df['weathersit'], palette='coolwarm')
plt.title('Total Daily Rentals vs Temperature')
plt.xlabel('Normalized Temperature')
plt.ylabel('Total Rentals (cnt)')
plt.legend(title='Weather Situation', loc='upper left')
st.pyplot(plt)

st.write("### Hourly Rental Trend Throughout the Day")
plt.figure(figsize=(10, 6))
sns.lineplot(x=hour_df['hr'], y=hour_df['cnt'], ci=None)
plt.title('Hourly Rental Trend Throughout the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Total Rentals (cnt)')
plt.xticks(range(0, 24))
plt.grid(True)
st.pyplot(plt)

# Mengelompokkan berdasarkan hari kerja dan hari libur untuk membandingkan rata-rata penyewaan
st.write("### Average Rentals by Weekday and Holiday Status")
weekday_holiday_df = day_df.groupby(['weekday', 'holiday']).agg({'cnt': 'mean'}).reset_index()

# Plotting data
plt.figure(figsize=(10, 6))
sns.barplot(x='weekday', y='cnt', hue='holiday', data=weekday_holiday_df, palette='Set2')
plt.title('Average Rentals by Weekday and Holiday Status')
plt.xlabel('Day of the Week (0=Sunday, 6=Saturday)')
plt.ylabel('Average Rentals (cnt)')
plt.legend(title='Holiday', labels=['No', 'Yes'])
plt.grid(True)
st.pyplot(plt)

# Mengelompokkan berdasarkan musim dan hitung jumlah sewa rata-rata
st.write("### Average Rentals by Season")
season_df = day_df.groupby('season').agg({'cnt': 'mean'}).reset_index()

# Mapping nomor musim ke nama agar lebih mudah dibaca
season_map = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
season_df['season'] = season_df['season'].map(season_map)

# Plotting data
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=season_df, palette='viridis')
plt.title('Average Rentals by Season')
plt.xlabel('Season')
plt.ylabel('Average Rentals (cnt)')
plt.grid(True)
st.pyplot(plt)
