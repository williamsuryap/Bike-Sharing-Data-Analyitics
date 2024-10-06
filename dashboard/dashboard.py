import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from datetime import date

# Set seaborn style
sns.set(style='dark')

# Load dataset
all_df = pd.read_csv('dashboard/all_data.csv')

min_date = pd.to_datetime(all_df['dateday']).dt.date.min()
max_date = pd.to_datetime(all_df['dateday']).dt.date.max()

with st.sidebar:

    st.image('dashboard/bike.png')

    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date, 
        max_value=max_date, 
        value=[min_date, max_date]
        )

st.title("Bike Sharing Data Analysis")

# Display the data
st.subheader('Bike Rentals Data')
st.write(all_df)

# Plot the Most Bike Rentals by Season
st.subheader('Most Bike Rentals By Season')
plt.figure(figsize=(8,5))
most_season = all_df.groupby('season')['count'].sum().reset_index()
colors = ['#72BCD4', '#D3D3D3', '#D3D3D3', '#D3D3D3']
bars = plt.bar(most_season['season'], most_season['count'], color=colors)
plt.title('Bike Renters By Season')
plt.xlabel('Season')
plt.ylabel('Count')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')
st.pyplot(plt)
st.markdown('**Conclusion: Fall is the season with the most bike rentals compared to other seasons, this could indicate that good weather tends to encourage more people to use bike.**')
plt.close()

# Plot the Impact of Several Variables and Bike Rentals
st.subheader('Impact of Temperature, Feels Like Temperature, and Humidity to Bike Rentals Total Number')
plt.figure(figsize=(7, 5))
sns.regplot(x='temp', 
            y='count', 
            data=all_df, 
            scatter_kws={'alpha':0.5}, 
            line_kws={'color':'red'})

# Plot Temp vs Count
plt.title('Temperature vs Count Correlation')
plt.xlabel('Temperature')
plt.ylabel('Count')
st.pyplot(plt)
plt.close()

plt.figure(figsize=(7, 5))
sns.regplot(x='atemp', 
            y='count', 
            data=all_df, 
            scatter_kws={'alpha':0.5}, 
            line_kws={'color':'red'})

# Plot Atemp vs Count
plt.title('Feels Like vs Count Correlation')
plt.xlabel('ATemp')
plt.ylabel('Count')
st.pyplot(plt)
plt.close()

plt.figure(figsize=(7, 5))
sns.regplot(x='hum', 
            y='count', 
            data=all_df, 
            scatter_kws={'alpha':0.5}, 
            line_kws={'color':'red'})

# Plot Humidity vs Count
plt.title('Humidity vs Count Correlation')
plt.xlabel('Humidity')
plt.ylabel('Count')
st.pyplot(plt)
st.markdown('**Conclusion: Temperature (Temp and Atemp) has a positive correlation with bike rentals, meaning higher temperatures lead to more users. Humidity, though having a small effect, shows a negative correlation, with rentals slightly decreasing as humidity rises.**')
plt.close()

plt.figure(figsize=(10,6))
sns.barplot(
    x='weather_cond',
    y='count',
    data=all_df)

# Plot the Impact of Weather Conditions and Bike Rentals
st.subheader('Impact of Weather Conditions on Bike Rentals')
plt.title('Bike Renters Based on Weather')
plt.xlabel('Weather')
plt.ylabel('Count')
st.pyplot(plt)
st.markdown('**Conclusion: Weather conditions significantly impact bike rentals, with clear/partly cloudy weather seeing the highest usage, followed by misty/cloudy, and light snow/rain having the lowest.**')
plt.close()
