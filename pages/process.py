# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process


            """
        ),

    ],
)

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

fnameDict = {'chriddy': ['opt1_c', 'opt2_c', 'opt3_c'], 'jackp': ['opt1_j', 'opt2_j']}

names = list(fnameDict.keys())
nestedOptions = fnameDict[names[0]]

app.layout = html.Div(
    [
        html.Div([
        dcc.Dropdown(
            id='name-dropdown',
            options=[{'label':name, 'value':name} for name in names],
            value = list(fnameDict.keys())[0]
            ),
            ],style={'width': '20%', 'display': 'inline-block'}),
        html.Div([
        dcc.Dropdown(
            id='opt-dropdown',
            options=[{'label':opt, 'value':opt} for opt in nestedOptions],
            value = nestedOptions[0]
            ),
            ],style={'width': '20%', 'display': 'inline-block'}
        ),
    ]
)

@app.callback(
    dash.dependencies.Output('opt-dropdown', 'options'),
    [dash.dependencies.Input('name-dropdown', 'value')]
)
def update_date_dropdown(name):
    opts = fnameDict[name]
    options=[{'label':opt, 'value':opt} for opt in opts]
    return {'options':options}


layout = dbc.Row([column1])