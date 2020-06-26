import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
from app.utils import get_data
import pandas as pd
import plotly.graph_objects as go


def index_page():
    content = html.Div([
        html.Div([
            dbc.Button("Go to covid stats ", color="dark", className="mr-1", href='/covid')
        ], className='text-center container', style={'paddingTop': "50px"})
    ])
    return content


def covid_page():
    data = get_data()
    df = pd.DataFrame({
        "height": [x['height'] for x in data],
        "weight": [x['weight'] for x in data],
        "pokemon": [x['name'] for x in data],
        "image": [x['image'] for x in data],
        "size": [ x['weight'] / x['height'] for x in data]
    })
    fig = px.scatter(df, x="height", y="weight", size='size', text="pokemon", hover_data=["pokemon"])
    # fig.update_traces(hovertemplate="<b>%{marker.pokemon}%{text}</b><br><br><b>Height: </b>%{x:.2f}<br><b>Weight: </b>%{y:.2f}")
    content = html.Div([
        html.Div([
            dbc.Button("Back to home", color="dark", className="mr-1", href='/'),
            html.Div([
                dcc.Graph(
                    id='Pokemon and their height',
                    figure=fig
                )
            ], style={"paddingTop": "40px"})
        ], className='text-center container', style={'paddingTop': "50px"})
    ])
    return content
