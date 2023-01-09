import dash
from dash import html,Output,Input,State,dcc
import dash_bootstrap_components as dbc

#external_stylesheets = ["/workspaces/MyPortfolioTracker/project/pages/style.css"]

external_stylesheets=[dbc.themes.SPACELAB]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

Menu = html.Div(
    [
        html.H3('My Game',style={'textAlign': 'center'})
        ],    
    className="my-3",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            Menu,
        ]
    ),
    color='#111111',#"dark",
    dark=True,
)

button = html.Div(
                    [
                        dbc.Button("Start A Game", color="primary"),
                    ],
                    className="d-grid gap-2 col-4 mx-auto",
                )

space = '''
###

'''

app.layout = dbc.Container([
    dbc.Row(
        [
                    navbar,#Menu,
                    dcc.Markdown(children=space),
                    button,
                    dash.page_container
        ], align='center',className="g-0",
    )
], fluid=True)

if __name__ == "__main__":
    app.run(debug=False)