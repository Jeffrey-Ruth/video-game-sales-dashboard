import pandas as pd
import plotly.express as px

df = pd.read_csv(r'C:/Portfolio Projects/data-analytics/video-game-sales/vgsales_clean.csv')

df = pd.melt(df, id_vars=['Year'], value_vars=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'], var_name='Region', value_name='Sales')

region_sales = df.groupby(['Year', 'Region']) ['Sales'].sum().reset_index()

fig = px.line(region_sales, x='Year', y='Sales', color='Region', title='Regional Market Growth')
fig.show()