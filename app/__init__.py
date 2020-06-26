import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


def create_app():
    # app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    # server = app.server
    server = flask.Flask(__name__)
    app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])
    setup_pages()

    @app.callback(dash.dependencies.Output('page-content', 'children'), [dash.dependencies.Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/covid':
            return func.covid_page()
        else:
            return func.index_page()

    return server


def setup_pages():
    from app import func

