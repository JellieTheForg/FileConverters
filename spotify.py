import json
import pandas as pd
import plotly.express as px


with open('spotify_history.json') as file:
    data = json.load(file)

#extract relevant information from each entry
streaming_data = []
for entry in data:
    date = entry['endTime'].split()[0]
    artist = entry['artistName']
    minutes_played = entry['msPlayed'] / 60000
    streaming_data.append({'Date': date, 'Artist': artist, 'Minutes Played': minutes_played})

#create a DataFrame from the extracted data
df = pd.DataFrame(streaming_data)

#convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

#group by date and artist, calculate the total minutes played per day
daily_minutes_artist = df.groupby(['Date', 'Artist'])['Minutes Played'].sum().reset_index()

#plot the minutes streamed per day with colored bars based on artists using Plotly
fig = px.bar(daily_minutes_artist, x='Date', y='Minutes Played', color='Artist', title='Minutes Streamed per Day (Coloured by Artist)')
fig.update_xaxes(title='Date')
fig.update_yaxes(title='Minutes Played')
fig.show()