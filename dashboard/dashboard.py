import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

def create_daily_rent_total_df(df):
    daily_rent_df = df.groupby(by='date_day').agg({
        'user_count': 'sum'
    }).reset_index()
    return daily_rent_df

def create_daily_rent_user_registered_df(df):
    daily_rent_df = df.groupby(by='date_day').agg({
        'user_registered': 'sum'
    }).reset_index()
    return daily_rent_df

def create_daily_rent_user_casual_df(df):
    daily_rent_df = df.groupby(by='date_day').agg({
        'user_casual': 'sum'
    }).reset_index()
    return daily_rent_df

def create_hour_rent_df(df):
    sum_order_items_df = df.groupby("hour").user_count.sum()
    return sum_order_items_df

def create_season_rent_df(df):
    season_rent_df = df.groupby(by='season')[['user_registered', 'user_casual']].sum().reset_index()
    return season_rent_df

def create_weather_rent_df(df):
    weather_rent_df = df.groupby(by='weather_situation').agg({
        'user_count': 'sum'
    })
    return weather_rent_df



# Load cleaned data
all_df = pd.read_csv("dashboard/main_data.csv")

datetime_columns = ["date_day"]
all_df.sort_values(by="date_day", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

# Filter data
min_date = all_df["date_day"].min()
max_date = all_df["date_day"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://i.ibb.co.com/G4pDWL2v/7094.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["date_day"] >= str(start_date)) & 
                (all_df["date_day"] <= str(end_date))]

# st.dataframe(main_df)

# # Menyiapkan berbagai dataframe
daily_rent_total_df = create_daily_rent_total_df(main_df)
daily_rent_user_registered_df = create_daily_rent_user_registered_df(main_df)
daily_rent_user_casual_df = create_daily_rent_user_casual_df(main_df)
hour_rent_user_df = create_hour_rent_df(main_df)
season_rent_df = create_season_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)

# sum_order_items_df = create_sum_order_items_df(main_df)
# bygender_df = create_bygender_df(main_df)
# byage_df = create_byage_df(main_df)
# bystate_df = create_bystate_df(main_df)
# rfm_df = create_rfm_df(main_df)


# plot number of daily orders (2021)
st.header('Bike Sharing Dashboard :bike:')
st.subheader('Daily Rent')

col1, col2, col3 = st.columns(3)

with col1:
    total_users = daily_rent_total_df['user_count'].sum()
    st.metric("Total Users", value=total_users)

with col2:
    total_user_registered = daily_rent_user_registered_df['user_registered'].sum()
    st.metric("Total Registered", value=total_user_registered)

with col3:
    total_user_casual = daily_rent_user_casual_df['user_casual'].sum() 
    st.metric("Total Casual", value=total_user_casual)

#Hourly rent
st.subheader('Hourly Rent')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    hour_rent_user_df.index,
    hour_rent_user_df.values,
    marker='o', 
    #color="#90CAF9"
    linestyle="-", color="b"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)

st.subheader('Seasonly Rentals')

fig, ax = plt.subplots(figsize=(16, 8))

sns.barplot(
    x='season',
    y='user_registered',
    data=season_rent_df,
    label='Registered',
    color='tab:blue',
    ax=ax
)

sns.barplot(
    x='season',
    y='user_casual',
    data=season_rent_df,
    label='Casual',
    color='tab:orange',
    ax=ax
)

for index, row in season_rent_df.iterrows():
    ax.text(index, row['user_registered'], str(row['user_registered']), ha='center', va='bottom', fontsize=12)
    ax.text(index, row['user_casual'], str(row['user_casual']), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20, rotation=0)
ax.tick_params(axis='y', labelsize=15)
ax.legend()
st.pyplot(fig)

#Weatherly Rent
st.subheader('Weatherly Rent')

fig, ax = plt.subplots(figsize=(16, 8))

colors=["tab:blue", "tab:orange", "tab:green"]

sns.barplot(
    x=weather_rent_df.index,
    y=weather_rent_df['user_count'],
    palette=colors,
    ax=ax
)

for index, row in enumerate(weather_rent_df['user_count']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=15)
ax.set_xticklabels(weather_rent_df.index, rotation=30, ha="right")  # Bisa ganti 30 sesuai kebutuhan
st.pyplot(fig)


st.caption('Copyright © R R M 2025')