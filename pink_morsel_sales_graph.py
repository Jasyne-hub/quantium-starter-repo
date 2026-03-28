import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

app = Dash()

df = pd.read_csv('./data/pink_morsel_total.csv')

app.layout = html.Div(
    style={
        'minHeight': '100vh',
        'backgroundColor': '#0f0f13',
        'fontFamily': '"DM Mono", "Courier New", monospace',
        'padding': '0',
        'margin': '0',
    },
    children=[
        html.Div(
            style={
                'backgroundColor': '#17171f',
                'borderBottom': '1px solid #2a2a38',
                'padding': '20px 40px',
                'display': 'flex',
                'alignItems': 'center',
                'justifyContent': 'space-between',
            },
            children=[
                html.Div(
                    style={'display': 'flex', 'alignItems': 'center', 'gap': '12px'},
                    children=[
                        html.Div(
                            style={
                                'width': '10px',
                                'height': '10px',
                                'borderRadius': '50%',
                                'backgroundColor': '#ff6b9d',
                                'boxShadow': '0 0 12px #ff6b9d',
                            }
                        ),
                        html.H1(
                            'Pink Morsel Sales',
                            style={
                                'margin': '0',
                                'fontSize': '18px',
                                'fontWeight': '500',
                                'color': '#f0f0f5',
                                'letterSpacing': '0.05em',
                            }
                        ),
                    ]
                ),
                html.Span(
                    'DASHBOARD',
                    style={
                        'fontSize': '11px',
                        'color': '#555568',
                        'letterSpacing': '0.2em',
                        'fontWeight': '400',
                    }
                ),
            ]
        ),

        html.Div(
            style={'padding': '32px 40px'},
            children=[

                # Filter row
                html.Div(
                    style={
                        'marginBottom': '24px',
                        'display': 'flex',
                        'alignItems': 'center',
                        'gap': '16px',
                    },
                    children=[
                        html.Span(
                            'REGION',
                            style={
                                'fontSize': '11px',
                                'color': '#555568',
                                'letterSpacing': '0.15em',
                                'fontWeight': '500',
                            }
                        ),
                        dcc.RadioItems(
                            id='region-filter',
                            options=["North", "South", "East", "West", "All"],
                            value="All",
                            inline=True,
                            inputStyle={
                                'marginRight': '6px',
                                'accentColor': '#ff6b9d',
                                'cursor': 'pointer',
                            },
                            labelStyle={
                                'marginRight': '20px',
                                'fontSize': '13px',
                                'color': '#a0a0b8',
                                'cursor': 'pointer',
                                'letterSpacing': '0.05em',
                            }
                        ),
                    ]
                ),

                html.Div(
                    style={
                        'backgroundColor': '#17171f',
                        'borderRadius': '8px',
                        'border': '1px solid #2a2a38',
                        'overflow': 'hidden',
                    },
                    children=[
                        dcc.Graph(
                            id='pink-morsel-sales',
                            config={'displayModeBar': False},
                            style={'height': '500px'},
                        )
                    ]
                ),
            ]
        ),
    ]
)


@callback(
    Output('pink-morsel-sales', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == "All":
        filtered_df = df
    else:
        filtered_df = df.query(f"Region == '{selected_region.lower()}'")

    fig = px.line(filtered_df, x='Date', y='Sales', title=f'Pink Morsel Sales — {selected_region}')

    fig.update_layout(
        paper_bgcolor='#17171f',
        plot_bgcolor='#17171f',
        font=dict(family='"DM Mono", "Courier New", monospace', color='#a0a0b8', size=12),
        title=dict(
            font=dict(size=14, color='#f0f0f5'),
            x=0.03,
            y=0.97,
        ),
        xaxis=dict(
            gridcolor='#2a2a38',
            linecolor='#2a2a38',
            tickcolor='#2a2a38',
            showgrid=True,
        ),
        yaxis=dict(
            gridcolor='#2a2a38',
            linecolor='#2a2a38',
            tickcolor='#2a2a38',
            showgrid=True,
        ),
        margin=dict(l=40, r=30, t=60, b=40),
        hovermode='x unified',
    )

    fig.update_traces(
        line=dict(color='#ff6b9d', width=2),
        hovertemplate='<b>%{y}</b><extra></extra>',
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)