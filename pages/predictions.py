# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
from joblib import load

# Imports from this application
from app import app

# load pipeline
pipeline = load('assets/pipeline_xgboost.joblib')

# row = html.Div(
#     [
#         dbc.Row(dbc.Col(html.Div("A single, half-width column"), width=6)),
#         dbc.Row(
#             dbc.Col(html.Div("An automatically sized column"), width="auto")
#         ),
#         dbc.Row(
#             [
#                 dbc.Col(html.Div("One of three columns"), width=3),
#                 dbc.Col(html.Div("One of three columns")),
#                 dbc.Col(html.Div("One of three columns"), width=3),
#             ]
#         ),
#     ]
# )


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            ##### Select Parameters to predict precipitation

            """,
            className='mb-5'
        ),
        
        # Country Code
        dcc.Markdown('#### Country Code'), 
        dcc.Dropdown(
            id='country_code', 
            options = [
                {'label': 'AD', 'value': 'AD'},
                {'label': 'AE', 'value': 'AE'},
                {'label': 'AF', 'value': 'AF'},
                {'label': 'AG', 'value': 'AG'},
                {'label': 'AI', 'value': 'AI'},
                {'label': 'AL', 'value': 'AL'},
                {'label': 'AM', 'value': 'AM'},
                {'label': 'AN', 'value': 'AN'},
                {'label': 'AO', 'value': 'AO'},
                {'label': 'AP', 'value': 'AP'},
                {'label': 'AQ', 'value': 'AQ'},
                {'label': 'AR', 'value': 'AR'},
                {'label': 'AS', 'value': 'AS'},
                {'label': 'AT', 'value': 'AT'},
                {'label': 'AU', 'value': 'AU'},
                {'label': 'AW', 'value': 'AW'},
                {'label': 'AZ', 'value': 'AZ'},
                {'label': 'BA', 'value': 'BA'},
                {'label': 'BB', 'value': 'BB'},
                {'label': 'BD', 'value': 'BD'},
                {'label': 'BE', 'value': 'BE'},
                {'label': 'BF', 'value': 'BF'},
                {'label': 'BG', 'value': 'BG'},
                {'label': 'BH', 'value': 'BH'},
                {'label': 'BI', 'value': 'BI'},
                {'label': 'BJ', 'value': 'BJ'},
                {'label': 'BM', 'value': 'BM'},
                {'label': 'BN', 'value': 'BN'},
                {'label': 'BO', 'value': 'BO'},
                {'label': 'BR', 'value': 'BR'},
                {'label': 'BS', 'value': 'BS'},
                {'label': 'BT', 'value': 'BT'},
                {'label': 'BV', 'value': 'BV'},
                {'label': 'BW', 'value': 'BW'},
                {'label': 'BY', 'value': 'BY'},
                {'label': 'BZ', 'value': 'BZ'},
                {'label': 'CA', 'value': 'CA'},
                {'label': 'CC', 'value': 'CC'},
                {'label': 'CD', 'value': 'CD'},
                {'label': 'CF', 'value': 'CF'},
                {'label': 'CG', 'value': 'CG'},
                {'label': 'CH', 'value': 'CH'},
                {'label': 'CI', 'value': 'CI'},
                {'label': 'CK', 'value': 'CK'},
                {'label': 'CL', 'value': 'CL'},
                {'label': 'CM', 'value': 'CM'},
                {'label': 'CN', 'value': 'CN'},
                {'label': 'CO', 'value': 'CO'},
                {'label': 'CR', 'value': 'CR'},
                {'label': 'CU', 'value': 'CU'},
                {'label': 'CV', 'value': 'CV'},
                {'label': 'CX', 'value': 'CX'},
                {'label': 'CY', 'value': 'CY'},
                {'label': 'CZ', 'value': 'CZ'},
                {'label': 'DE', 'value': 'DE'},
                {'label': 'DJ', 'value': 'DJ'},
                {'label': 'DK', 'value': 'DK'},
                {'label': 'DM', 'value': 'DM'},
                {'label': 'DO', 'value': 'DO'},
                {'label': 'DZ', 'value': 'DZ'},
                {'label': 'EC', 'value': 'EC'},
                {'label': 'EE', 'value': 'EE'},
                {'label': 'EG', 'value': 'EG'},
                {'label': 'EH', 'value': 'EH'},
                {'label': 'ER', 'value': 'ER'},
                {'label': 'ES', 'value': 'ES'},
                {'label': 'ET', 'value': 'ET'},
                {'label': 'EU', 'value': 'EU'},
                {'label': 'FI', 'value': 'FI'},
                {'label': 'FJ', 'value': 'FJ'},
                {'label': 'FK', 'value': 'FK'},
                {'label': 'FM', 'value': 'FM'},
                {'label': 'FO', 'value': 'FO'},
                {'label': 'FR', 'value': 'FR'},
                {'label': 'GA', 'value': 'GA'},
                {'label': 'GB', 'value': 'GB'},
                {'label': 'GD', 'value': 'GD'},
                {'label': 'GE', 'value': 'GE'},
                {'label': 'GF', 'value': 'GF'},
                {'label': 'GH', 'value': 'GH'},
                {'label': 'GI', 'value': 'GI'},
                {'label': 'GL', 'value': 'GL'},
                {'label': 'GM', 'value': 'GM'},
                {'label': 'GN', 'value': 'GN'},
                {'label': 'GP', 'value': 'GP'},
                {'label': 'GQ', 'value': 'GQ'},
                {'label': 'GR', 'value': 'GR'},
                {'label': 'GS', 'value': 'GS'},
                {'label': 'GT', 'value': 'GT'},
                {'label': 'GU', 'value': 'GU'},
                {'label': 'GW', 'value': 'GW'},
                {'label': 'GY', 'value': 'GY'},
                {'label': 'HK', 'value': 'HK'},
                {'label': 'HM', 'value': 'HM'},
                {'label': 'HN', 'value': 'HN'},
                {'label': 'HR', 'value': 'HR'},
                {'label': 'HT', 'value': 'HT'},
                {'label': 'HU', 'value': 'HU'},
                {'label': 'ID', 'value': 'ID'},
                {'label': 'IE', 'value': 'IE'},
                {'label': 'IL', 'value': 'IL'},
                {'label': 'IN', 'value': 'IN'},
                {'label': 'IO', 'value': 'IO'},
                {'label': 'IQ', 'value': 'IQ'},
                {'label': 'IR', 'value': 'IR'},
                {'label': 'IS', 'value': 'IS'},
                {'label': 'IT', 'value': 'IT'},
                {'label': 'JM', 'value': 'JM'},
                {'label': 'JO', 'value': 'JO'},
                {'label': 'JP', 'value': 'JP'},
                {'label': 'KE', 'value': 'KE'},
                {'label': 'KG', 'value': 'KG'},
                {'label': 'KH', 'value': 'KH'},
                {'label': 'KI', 'value': 'KI'},
                {'label': 'KM', 'value': 'KM'},
                {'label': 'KN', 'value': 'KN'},
                {'label': 'KP', 'value': 'KP'},
                {'label': 'KR', 'value': 'KR'},
                {'label': 'KW', 'value': 'KW'},
                {'label': 'KY', 'value': 'KY'},
                {'label': 'KZ', 'value': 'KZ'},
                {'label': 'LA', 'value': 'LA'},
                {'label': 'LB', 'value': 'LB'},
                {'label': 'LC', 'value': 'LC'},
                {'label': 'LI', 'value': 'LI'},
                {'label': 'LK', 'value': 'LK'},
                {'label': 'LR', 'value': 'LR'},
                {'label': 'LS', 'value': 'LS'},
                {'label': 'LT', 'value': 'LT'},
                {'label': 'LU', 'value': 'LU'},
                {'label': 'LV', 'value': 'LV'},
                {'label': 'LY', 'value': 'LY'},
                {'label': 'MA', 'value': 'MA'},
                {'label': 'MC', 'value': 'MC'},
                {'label': 'MD', 'value': 'MD'},
                {'label': 'ME', 'value': 'ME'},
                {'label': 'MG', 'value': 'MG'},
                {'label': 'MH', 'value': 'MH'},
                {'label': 'MK', 'value': 'MK'},
                {'label': 'ML', 'value': 'ML'},
                {'label': 'MM', 'value': 'MM'},
                {'label': 'MN', 'value': 'MN'},
                {'label': 'MO', 'value': 'MO'},
                {'label': 'MP', 'value': 'MP'},
                {'label': 'MQ', 'value': 'MQ'},
                {'label': 'MR', 'value': 'MR'},
                {'label': 'MS', 'value': 'MS'},
                {'label': 'MT', 'value': 'MT'},
                {'label': 'MU', 'value': 'MU'},
                {'label': 'MV', 'value': 'MV'},
                {'label': 'MW', 'value': 'MW'},
                {'label': 'MX', 'value': 'MX'},
                {'label': 'MY', 'value': 'MY'},
                {'label': 'MZ', 'value': 'MZ'},
                {'label': 'NA', 'value': 'NA'},
                {'label': 'NC', 'value': 'NC'},
                {'label': 'NE', 'value': 'NE'},
                {'label': 'NF', 'value': 'NF'},
                {'label': 'NG', 'value': 'NG'},
                {'label': 'NI', 'value': 'NI'},
                {'label': 'NL', 'value': 'NL'},
                {'label': 'NO', 'value': 'NO'},
                {'label': 'NP', 'value': 'NP'},
                {'label': 'NR', 'value': 'NR'},
                {'label': 'NU', 'value': 'NU'},
                {'label': 'NZ', 'value': 'NZ'},
                {'label': 'OM', 'value': 'OM'},
                {'label': 'PA', 'value': 'PA'},
                {'label': 'PE', 'value': 'PE'},
                {'label': 'PF', 'value': 'PF'},
                {'label': 'PG', 'value': 'PG'},
                {'label': 'PH', 'value': 'PH'},
                {'label': 'PK', 'value': 'PK'},
                {'label': 'PL', 'value': 'PL'},
                {'label': 'PM', 'value': 'PM'},
                {'label': 'PR', 'value': 'PR'},
                {'label': 'PS', 'value': 'PS'},
                {'label': 'PT', 'value': 'PT'},
                {'label': 'PW', 'value': 'PW'},
                {'label': 'PY', 'value': 'PY'},
                {'label': 'QA', 'value': 'QA'},
                {'label': 'RE', 'value': 'RE'},
                {'label': 'RO', 'value': 'RO'},
                {'label': 'RS', 'value': 'RS'},
                {'label': 'RU', 'value': 'RU'},
                {'label': 'RW', 'value': 'RW'},
                {'label': 'SA', 'value': 'SA'},
                {'label': 'SB', 'value': 'SB'},
                {'label': 'SC', 'value': 'SC'},
                {'label': 'SD', 'value': 'SD'},
                {'label': 'SE', 'value': 'SE'},
                {'label': 'SG', 'value': 'SG'},
                {'label': 'SH', 'value': 'SH'},
                {'label': 'SI', 'value': 'SI'},
                {'label': 'SJ', 'value': 'SJ'},
                {'label': 'SK', 'value': 'SK'},
                {'label': 'SL', 'value': 'SL'},
                {'label': 'SM', 'value': 'SM'},
                {'label': 'SN', 'value': 'SN'},
                {'label': 'SO', 'value': 'SO'},
                {'label': 'SR', 'value': 'SR'},
                {'label': 'ST', 'value': 'ST'},
                {'label': 'SV', 'value': 'SV'},
                {'label': 'SY', 'value': 'SY'},
                {'label': 'SZ', 'value': 'SZ'},
                {'label': 'TC', 'value': 'TC'},
                {'label': 'TD', 'value': 'TD'},
                {'label': 'TF', 'value': 'TF'},
                {'label': 'TG', 'value': 'TG'},
                {'label': 'TH', 'value': 'TH'},
                {'label': 'TJ', 'value': 'TJ'},
                {'label': 'TK', 'value': 'TK'},
                {'label': 'TM', 'value': 'TM'},
                {'label': 'TN', 'value': 'TN'},
                {'label': 'TO', 'value': 'TO'},
                {'label': 'TR', 'value': 'TR'},
                {'label': 'TT', 'value': 'TT'},
                {'label': 'TV', 'value': 'TV'},
                {'label': 'TW', 'value': 'TW'},
                {'label': 'TZ', 'value': 'TZ'},
                {'label': 'UA', 'value': 'UA'},
                {'label': 'UG', 'value': 'UG'},
                {'label': 'UM', 'value': 'UM'},
                {'label': 'US', 'value': 'US'},
                {'label': 'UY', 'value': 'UY'},
                {'label': 'UZ', 'value': 'UZ'},
                {'label': 'VA', 'value': 'VA'},
                {'label': 'VC', 'value': 'VC'},
                {'label': 'VE', 'value': 'VE'},
                {'label': 'VG', 'value': 'VG'},
                {'label': 'VI', 'value': 'VI'},
                {'label': 'VN', 'value': 'VN'},
                {'label': 'VU', 'value': 'VU'},
                {'label': 'WF', 'value': 'WF'},
                {'label': 'WS', 'value': 'WS'},
                {'label': 'YE', 'value': 'YE'},
                {'label': 'YT', 'value': 'YT'},
                {'label': 'ZA', 'value': 'ZA'},
                {'label': 'ZM', 'value': 'ZM'},
                {'label': 'ZW', 'value': 'ZW'}
            ], 
            value = 'AD', 
            className='mb-3', 
        ), 
                    
        # lat 
        dcc.Markdown('#### Latitude'), 
        dcc.Input(
            id='lat', 
            placeholder='Enter country Latitude',
            type='number',
            value='',
            className='mb-3'
            ),
        
        # long 
        dcc.Markdown('#### Longitude'), 
        dcc.Input(
            id='long', 
            placeholder='Enter country Longitude',
            type='number',
            value='',
            className='mb-3'
            ),
        
        # Elevation
        dcc.Markdown('#### Elevation'), 
        dcc.Slider(
            id='elevation', 
            min=0, 
            max=3800, 
            # step=500, 
            value=2000, 
            marks={n: str(n) for n in range(0,3801,500)}, 
            className='mb-1', 
        ), 
        
        dcc.Markdown('', id='elevation_display'), 

        # Suface Pressure
        dcc.Markdown('#### Suface Pressure'), 
        dcc.Slider(
            id='surface_pressure', 
            min=63.27, 
            max=104.8, 
            # step=500, 
            value=98.6, 
            marks={n: str(n) for n in range(63,105,10)}, 
            className='mb-1', 
        ), 
        
        dcc.Markdown('', id='surface_pressure_display'),

        
        # Skin Temperature
        dcc.Markdown('#### Skin Temperature'), 
        dcc.Slider(
            id='skin_temperature', 
            min=-78.2, 
            max=45.6, 
            # step=500, 
            value=2.42, 
            marks={n: str(n) for n in range(-78,46,10)}, 
            className='mb-1', 
        ), 
        
        dcc.Markdown('', id='skin_temperature_display'),


        
        # Dew Frost
        dcc.Markdown('#### Dew Frost'), 
        dcc.Slider(
            id='dew_frost', 
            min=-77.97, 
            max=30.38, 
            # step=500, 
            value=1.5, 
            marks={n: str(n) for n in range(-77,31,10)}, 
            className='mb-1', 
        ), 
        
        dcc.Markdown('', id='dew_frost_display')



        # dcc.Slider(
        # id='slider1',
        # min=0,
        # max=100,
        # step=0.5,
        # value=0,
        # className='mb-5',
        # marks={i: '{}'.format(i) for i in range(0,120,20)}
        # ),
        
        # dcc.Markdown('', id='out1')
    ],
    md=4
)

column2 = dbc.Col(
    [
        
        # Temperature at 2m
        dcc.Markdown('#### Temperature at 2m'), 
        dcc.Slider(
            id='temperature2m', 
            min=-77.97, 
            max=30.38, 
            # step=500, 
            value=1.5, 
            marks={n: str(n) for n in range(-77,31,10)}, 
            className='mb-1', 
        ), 
        
        dcc.Markdown('', id='temperature2m_display'),


        
        # Wind Speed 10m
        dcc.Markdown('#### Wind Speed 10m'), 
        dcc.Slider(
            id='windspeed10m', 
            min=0.26, 
            max=23.81, 
            # step=500, 
            value=3.57, 
            marks={n: str(n) for n in range(0,24,3)}, 
            className='mb-1', 
        ), 
        
        dcc.Markdown('', id='windspeed10m_display'),


        
        # Wind Speed 50m
        dcc.Markdown('#### Wind Speed 50m'), 
        dcc.Slider(
            id='windspeed50m', 
            min=0.28, 
            max=28.26, 
            # step=500, 
            value=4.88, 
            marks={n: str(n) for n in range(0,30,3)}, 
            className='mb-1', 
        ), 
        
        dcc.Markdown('', id='windspeed50m_display'),


        
        # Wet Buld Temp.
        dcc.Markdown('#### Wet Buld Temp.'), 
        dcc.Slider(
            id='wet_bulb_temp', 
            min=-74.52, 
            max=30.38, 
            # step=500, 
            value=1.5, 
            marks={n: str(n) for n in range(-75 ,31,10)}, 
            className='mb-1', 
        ), 
        
        dcc.Markdown('', id='wet_bulb_temp_display'),

        # Temp Range
        dcc.Markdown('#### Temp Range'), 
        dcc.Slider(
            id='temp_range', 
            min=0.04, 
            max=35.49, 
            # step=500, 
            value=7.26, 
            marks={n: str(n) for n in range(0,36,5)}, 
            className='mb-1', 
        ), 
        
        dcc.Markdown('', id='temp_range_display'),
        
        
        # Clearness Index
        dcc.Markdown('#### Clearness Index'), 
        dcc.Slider(
            id='clearness_index', 
            min=-999, 
            max=1, 
            # step=500, 
            value=-0.59, 
            marks={n: str(n) for n in range(-999,2,100)}, 
            className='mb-1', 
        ), 
        
        dcc.Markdown('', id='clearness_index_display'),
        
        
        # All Sky Insolation
        dcc.Markdown('#### Clear Sky Insolation'), 
        dcc.Slider(
            id='clear_sky_insolation', 
            min=-999, 
            max=11.65, 
            # step=500, 
            value=3.95, 
            marks={n: str(n) for n in range(-999,12,100)}, 
            className='mb-1', 
        ), 
        
        dcc.Markdown('', id='clear_sky_insolation_display'),
        
        
        
        # All Sky Insolation
        dcc.Markdown('#### All Sky Insolation'), 
        dcc.Slider(
            id='all_sky_insolation', 
            min=-999, 
            max=11.58, 
            # step=500, 
            value=5.21, 
            marks={n: str(n) for n in range(-999,12,100)}, 
            className='mb-1', 
        ), 
        
        dcc.Markdown('', id='all_sky_insolation_display'),
        
        
        # Radiative Flux
        dcc.Markdown('#### Radiative Flux'), 
        dcc.Slider(
            id='radiative_flux', 
            min=-999, 
            max=12.07, 
            # step=500, 
            value=9, 
            marks={n: str(n) for n in range(-999,13,100)}, 
            className='mb-1', 
        ), 
        
        dcc.Markdown('', id='radiative_flux_display'),
        
                
    ], md=5
)

# column3 = dbc.Col(
#     [
#         dcc.Markdown('### Predicted Precipiration'),
#         daq.Gauge(
#         id='my-daq-gauge3',
#         min=0,  
#         max=100,
#         value=50
#         )
#     ], md=3
    
# )

column3 = dbc.Col(
    [
        html.H2('Expected Precipitation', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2, column3])

# @app.callback(
#     Output(component_id='my-daq-gauge', component_property='value'),
#     [Input(component_id='slider1', component_property='value')]
# )
# def update_output_div(input_value):
#     return input_value


@app.callback(
    Output(component_id='elevation_display', component_property='children'),
    [Input(component_id='elevation', component_property='value')]
)
def elevation_display(input_value):
    return 'Elevation is {}m'.format(input_value)


@app.callback(
    Output(component_id='surface_pressure_display', component_property='children'),
    [Input(component_id='surface_pressure', component_property='value')]
)
def surface_pressure_display(input_value):
    return 'Surface Pressure is {}kPa'.format(input_value)

@app.callback(
    Output(component_id='skin_temperature_display', component_property='children'),
    [Input(component_id='skin_temperature', component_property='value')]
)
def surface_pressure_display(input_value):
    return 'Skin Temperature is {}C'.format(input_value)

@app.callback(
    Output(component_id='dew_frost_display', component_property='children'),
    [Input(component_id='dew_frost', component_property='value')]
)
def surface_pressure_display(input_value):
    return 'Dew Frost is {}C'.format(input_value)

@app.callback(
    Output(component_id='temperature2m_display', component_property='children'),
    [Input(component_id='temperature2m', component_property='value')]
)
def surface_pressure_display(input_value):
    return 'Temperature2m is {}C'.format(input_value)

@app.callback(
    Output(component_id='windspeed10m_display', component_property='children'),
    [Input(component_id='windspeed10m', component_property='value')]
)
def surface_pressure_display(input_value):
    return 'Windspeed10m is {}'.format(input_value)

@app.callback(
    Output(component_id='windspeed50m_display', component_property='children'),
    [Input(component_id='windspeed50m', component_property='value')]
)
def surface_pressure_display(input_value):
    return 'Windspeed50m is {}'.format(input_value)

@app.callback(
    Output(component_id='wet_bulb_temp_display', component_property='children'),
    [Input(component_id='wet_bulb_temp', component_property='value')]
)
def surface_pressure_display(input_value):
    return 'Web Bulb Temperature is {}C'.format(input_value)

@app.callback(
    Output(component_id='temp_range_display', component_property='children'),
    [Input(component_id='temp_range', component_property='value')]
)
def surface_pressure_display(input_value):
    return 'Temperature Range is {}C'.format(input_value)

@app.callback(
    Output(component_id='clearness_index_display', component_property='children'),
    [Input(component_id='clearness_index', component_property='value')]
)
def surface_pressure_display(input_value):
    return 'Clearness Index is {}'.format(input_value)

@app.callback(
    Output(component_id='clear_sky_insolation_display', component_property='children'),
    [Input(component_id='clear_sky_insolation', component_property='value')]
)
def surface_pressure_display(input_value):
    return 'Clear Sky Insolation is {}'.format(input_value)

@app.callback(
    Output(component_id='all_sky_insolation_display', component_property='children'),
    [Input(component_id='all_sky_insolation', component_property='value')]
)
def surface_pressure_display(input_value):
    return 'All Sky Insolation is {}'.format(input_value)

@app.callback(
    Output(component_id='radiative_flux_display', component_property='children'),
    [Input(component_id='radiative_flux', component_property='value')]
)
def surface_pressure_display(input_value):
    return 'Radiative Flux is {}'.format(input_value)

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('country_code', 'value'), Input('lat', 'value'), Input('long', 'value'), Input('elevation', 'value'), Input('surface_pressure', 'value'), Input('skin_temperature', 'value'), Input('dew_frost', 'value'), Input('temperature2m', 'value'), Input('windspeed10m', 'value'), Input('windspeed50m', 'value'), Input('wet_bulb_temp', 'value'), Input('temp_range', 'value'), Input('clearness_index', 'value'), Input('clear_sky_insolation', 'value'), Input('all_sky_insolation', 'value'), Input('radiative_flux', 'value')],
)
def predict(country_code, lat, long, elevation, surface_pressure,
       skin_temperature, dew_frost, temperature2m, windspeed10m,
       windspeed50m, wet_bulb_temp, temp_range, clearness_index,
       clear_sky_insolation, all_sky_insolation, radiative_flux):
    df = pd.DataFrame(
        columns=['country_code', 'lat', 'long', 'elevation', 'surface_pressure',
       'skin_temperature', 'dew_frost', 'temperature2m', 'windspeed10m',
       'windspeed50m', 'wet_bulb_temp', 'temp_range', 'clearness_index',
       'clear_sky_insolation', 'all_sky_insolation', 'radiative_flux'],
        data=[[country_code, lat, long, elevation, surface_pressure,
       skin_temperature, dew_frost, temperature2m, windspeed10m,
       windspeed50m, wet_bulb_temp, temp_range, clearness_index,
       clear_sky_insolation, all_sky_insolation, radiative_flux]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred}'