# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ### Predict Precipitation using Global Climate Data!
            

            💧 MET can be used to make a prediction based on various climate conditions. Just select various climatic parameters to predict the precipitation of any place.

            💧 MET is an online application that helps you make a prediction based on data from the past. The application can be used how precipitation changes by 🌎 latitude, longitude, or by changing 🇨🇦 🇺🇸 countries.

            Try the app by clicking the link below.

            """
        ),
        dcc.Link(dbc.Button('Predict Precipitation', color='primary'), href='/predictions')
    ],
    md=4,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    # [
    #     dcc.Graph(figure=fig),
    # ]
    [
        dcc.Markdown(
            """
        
            ![Precipitation-Cover](https://raw.githubusercontent.com/singparvi/singparvi.github.io/16eba23f87cc1e46af785959f992382e26f816cb/assets/img/Precipitation-Cover-723X407.jpg)

            """
        )
    ],
    md=4,
)

layout = dbc.Row([column1, column2])