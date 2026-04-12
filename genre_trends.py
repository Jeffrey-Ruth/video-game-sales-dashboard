import pandas as pd
import plotly.express as px

df = pd.read_csv(r'C:/Portfolio Projects/data-analytics/video-game-sales/vgsales_clean.csv')

genre_year = df.groupby(['Year', 'Genre']) ['Global_Sales'].sum().reset_index()

fig = px.line(genre_year, x='Year', y='Global_Sales', color='Genre', title='Genre Popularity Over Time (Global Sales)')
fig.show()