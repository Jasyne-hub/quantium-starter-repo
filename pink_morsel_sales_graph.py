import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

app = Dash()

df = pd.read_csv('./data/pink_morsel_total.csv')

fig = px.line(df, x='Date', y='Sales', title='Pink Morsel Total Sales')

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales'),
    dcc.Graph(
        id='pink-morsel-sales',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)