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
        dbc.Button("Start Game",id = 'start-game',type = 'submit',color="primary"),
    ],
    className="d-grid gap-2 col-4 mx-auto",
)

frequence_input = html.Div(
    [
        dcc.Input(id="frequence-input", type="text",value = '', placeholder=""),
    ],
    className="d-grid gap-2 col-4 mx-auto",
)

unite_input = html.Div(
    [
        dcc.Input(id="unite-input", type="text", value = '',placeholder=""),
    ],
    className="d-grid gap-2 col-4 mx-auto",
)

frequence_txt = html.Div(
    [
        dcc.Markdown(children='Frequence de la notification (1,2,40)'),
    ],
    className="d-grid gap-2 col-4 mx-auto",
)

unite_txt = html.Div(
    [
        dcc.Markdown(children='unité de la frequence (min/h)'),
    ],
    className="d-grid gap-2 col-4 mx-auto",
)

joueur_txt = html.Div(
    [
        dcc.Markdown(children='Joueurs :'),
    ],
    className="d-grid gap-2 col-4 mx-auto",
)

space = '''
###

'''

regles = html.Div(
    [
        dcc.Markdown(id='output-regles'),
    ],
    className="d-grid gap-2 col-4 mx-auto",
)

global joueurs 
joueurs = []

list_joueurs = html.Div(
    [
        dcc.Markdown(id = 'output-joueur'),
    ],
    className="d-grid gap-2 col-4 mx-auto",
)

button_add = html.Div(
    [
        dbc.Button("Add",id = 'add',type = 'submit',color="success"),
    ],
    className="d-grid gap-1 col-2 mx-auto",
)

button_drop = html.Div(
    [
        dbc.Button("Drop",id = 'drop',type = 'submit',color="danger"),
    ],
    className="d-grid gap-1 col-2 mx-auto",
)

joueur_input = html.Div(
    [
        dcc.Input(id="joueur-input", type="text", value = '',placeholder=""),
    ],
    className="d-grid gap-2 col-4 mx-auto",
)

app.layout = dbc.Container([
    dbc.Row(
        [
        navbar,#Menu,
        dcc.Markdown(children=space),
        frequence_txt,
        dcc.Markdown(children=space),
        frequence_input,
        dcc.Markdown(children=space),
        unite_txt,
        dcc.Markdown(children=space),
        unite_input,
        dcc.Markdown(children=space),
        joueur_txt,
        dcc.Markdown(children=space),
        joueur_input,
        dcc.Markdown(children=space),
        button_add,
        button_drop,
        dcc.Markdown(children=space),
        list_joueurs,
        dcc.Markdown(children=space),
        dcc.Markdown(children=space),
        button,
        dcc.Markdown(children=space),
        regles,
        dash.page_container
        ], align='center',className="g-0",
    )
], fluid=True)


#Fonction qui affiche les regles
@app.callback(
    Output('output-regles',"children"),
    [Input('start-game','n_clicks')],
    [State("frequence-input", "value"),State("unite-input", "value")],
    
)
def update_output(clicks,input1, input2):
    if clicks is not None:

        str_joueurs = ''
        for j in joueurs:
            str_joueurs = str_joueurs +'\n -  '+j

        return u'''
        Un Defi sera lancé toutes les {} {},\n
        Les joueurs sont :\n
        {}
        ''' .format(input1, input2,str_joueurs)

#Fonction qui permet de supprimer des joueurs
@app.callback(
    Output('output-joueur',"children"),
    [Input('drop','n_clicks'),Input('add','n_clicks')],
    [State("joueur-input", "value")]
)
def update_output2(click_drop,click_add,name):
    if click_drop is not None:
        joueurs.remove(name)
    elif click_add is not None:
        joueurs.append(name)
    
    str = ''
    for j in joueurs:
        str= str+'\n -  '+j
    return str


if __name__ == "__main__":
    app.run(debug=False)