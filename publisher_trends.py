import pandas as pd
import plotly.express as px

df = pd.read_csv(r'C:/Portfolio Projects/data-analytics/video-game-sales/vgsales_clean.csv')

top_publishers = df.groupby('Publisher')['Global_Sales'].sum().nlargest(10).index
df = df[df['Publisher'].isin(top_publishers)]

publisher_year = df.groupby(['Year', 'Publisher']) ['Global_Sales'].sum().reset_index()

fig = px.line(publisher_year, x='Year', y='Global_Sales', color='Publisher', title='Publisher Growth Over Time (Global Sales)')
fig.show()