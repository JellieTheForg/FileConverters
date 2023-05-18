import json
import pandas as pd
import plotly.express as px


with open('spotify_history.json') as file:
    data = json.load(file)

#extract relevant information from each entry
streaming_data = []
for entry in data:
    date = entry['endTime'].split()[0]
    minutes_played = entry['msPlayed'] / 60000
    streaming_data.append({'Date': date, 'Minutes Played': minutes_played})

#create a DataFrame from the extracted data
df = pd.DataFrame(streaming_data)

#convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

#group by date and calculate the total minutes played per day
daily_minutes = df.groupby('Date')['Minutes Played'].sum().reset_index()

#plot the minutes streamed using Plotly
fig = px.line(daily_minutes, x='Date', y='Minutes Played', title='Daily Minutes Streamed on Spotify')
fig.update_xaxes(title='Date')
fig.update_yaxes(title='Minutes Played')
fig.show()
