import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Bike Sharing", layout="wide")

# Load datasets
day_df = pd.read_csv('./data/day.csv')
hour_df = pd.read_csv('./data/hour.csv')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv("sample_data/day.csv")
day_df.sample(15)

hour_df = pd.read_csv("sample_data/hour.csv")
hour_df.sample(15)

day_df.info()

print("Duplikasi = ",day_df.duplicated().sum())
day_df.describe()

hour_df.info()

print("Duplikasi = ",hour_df.duplicated().sum())
day_df.describe()

day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

day_df.info()

hour_df.info()

day_df.describe(include="all")

day_df.groupby(by="workingday").agg({
    "instant": "nunique",
    "cnt": ["min", "max", "mean", "std"]})

day_df.groupby(by="weathersit").agg({
    "instant": "nunique",
    "cnt": ["min", "max", "mean", "std"]})

hour_df.describe(include="all")

hour_df.groupby(by="workingday").agg({
    "instant": "nunique",
    "cnt": ["min", "max", "mean", "std"]})


hour_df.groupby(by="weathersit").agg({
    "instant": "nunique",
    "cnt": ["min", "max", "mean", "std"]})

import matplotlib.pyplot as plt
import seaborn as sns

# Baik disini saya memvisualisasikan yang bertujuan untuk menganalisis hubungan antara suhu dan total penyewaan harian
plt.figure(figsize=(10, 6))
sns.scatterplot(x=day_df['temp'], y=day_df['cnt'], hue=day_df['weathersit'], palette='coolwarm')
plt.title('Total Daily Rentals vs Temperature')
plt.xlabel('Normalized Temperature')
plt.ylabel('Total Rentals (cnt)')
plt.legend(title='Weather Situation', loc='upper left')
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(x=hour_df['hr'], y=hour_df['cnt'], ci=None)
plt.title('Hourly Rental Trend Throughout the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Total Rentals (cnt)')
plt.xticks(range(0, 24))
plt.grid(True)
plt.show()

# Group by weekday and holiday to compare average rentals
weekday_holiday_df = day_df.groupby(['weekday', 'holiday']).agg({'cnt': 'mean'}).reset_index()

# Plotting the data
plt.figure(figsize=(10, 6))
sns.barplot(x='weekday', y='cnt', hue='holiday', data=weekday_holiday_df, palette='Set2')
plt.title('Average Rentals by Weekday and Holiday Status')
plt.xlabel('Day of the Week (0=Sunday, 6=Saturday)')
plt.ylabel('Average Rentals (cnt)')
plt.legend(title='Holiday', labels=['No', 'Yes'])
plt.grid(True)
plt.show()

# Group by season and calculate the mean rental count
season_df = day_df.groupby('season').agg({'cnt': 'mean'}).reset_index()

# Mapping season numbers to names for better readability
season_map = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
season_df['season'] = season_df['season'].map(season_map)

# Plotting the data
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=season_df, palette='viridis')
plt.title('Average Rentals by Season')
plt.xlabel('Season')
plt.ylabel('Average Rentals (cnt)')
plt.grid(True)
plt.show()