import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


def index_page():
    content = html.Div([
        html.Div([
            dbc.Button("Go to covid stats", color="dark", className="mr-1", href='/covid')
        ], className='text-center container', style={'paddingTop': "50px"})
    ])
    return content


def covid_page():
    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }
    content = html.Div([
        html.Div([
            dbc.Button("Back to home", color="dark", className="mr-1", href='/'),
            html.Div([
                dcc.Graph(
                    id='Graph1',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'plot_bgcolor': colors['background'],
                            'paper_bgcolor': colors['background'],
                            'font': {
                                'color': colors['text']
                            }
                        }
                    }
                )
            ], style={"paddingTop": "40px"})
        ], className='text-center container', style={'paddingTop': "50px"})
    ])
    return content
