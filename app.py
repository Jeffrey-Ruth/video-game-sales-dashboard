import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, callback, Input, Output

#Read csv file
df = pd.read_csv(r'C:/Portfolio Projects/data-analytics/video-game-sales/data/vgsales_clean.csv')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Genre Popularity ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
genre_year = df.groupby(['Year', 'Genre']) ['Global_Sales'].sum().reset_index()

genre_fig = px.line(genre_year, x='Year', y='Global_Sales', color='Genre', title='Genre Popularity Over Time (Global Sales)')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Publisher Growth ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
top_publishers = df.groupby('Publisher')['Global_Sales'].sum().nlargest(10).index
pub_df = df[df['Publisher'].isin(top_publishers)]

publisher_year = pub_df.groupby(['Year', 'Publisher']) ['Global_Sales'].sum().reset_index()

pub_fig = px.line(publisher_year, x='Year', y='Global_Sales', color='Publisher', title='Publisher Growth Over Time (Global Sales)')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Regional Market Growth ~~~~~~~~~~~~~~~~~~~~~~~~~
df = pd.melt(df, id_vars=['Year'], value_vars=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'], var_name='Region', value_name='Sales')

region_sales = df.groupby(['Year', 'Region']) ['Sales'].sum().reset_index()

region_fig = px.line(region_sales, x='Year', y='Sales', color='Region', title='Regional Market Growth')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



app = Dash(__name__)

app.layout = html.Div([
    html.H1("Video Game Sales Dashboard"),
    dcc.RangeSlider(
        id='year-slider',
        min=1980,
        max=2016,
        step=1,
        value=[1980, 2016],
        marks={i: str(i) for i in range(1980, 2017, 5)}
    ),
    dcc.Graph(figure=genre_fig),
    html.P("Action and Sports games saw the most growth from 2000 to 2009. Sports declined sharply after 2009 due to limited competition and repetitive annual releases, while Action remained more stable due to its broader range of developers."),
    dcc.Graph(figure=pub_fig),
    html.P("Nintendo saw massive growth around 2006 driven by the launch of the Wii, one of the best selling consoles of all time. EA, Nintendo, Activision, and Ubisoft consistently dominated global sales throughout the dataset.""Nintendo saw massive growth around 2006 driven by the launch of the Wii, one of the best selling consoles of all time. EA, Nintendo, Activision, and Ubisoft consistently dominated global sales throughout the dataset."),
    dcc.Graph(figure=region_fig),
    html.P("North America has been the largest and fastest growing gaming market since the 90s, followed by Europe. Japan and other regions remained relatively flat with no significant growth over time.")
])



if __name__ == '__main__':
    app.run(debug=True)
