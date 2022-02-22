# Add Transcript Archive here
# Have wav and associated csv and be able to view full csv
import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table
import datetime

import pandas as pd

from starter import app

button = html.A(html.Button('Show Transcript', id="dispaly"), href="/")

row =  html.Div([
        html.Div(html.H5(datetime.datetime.now().strftime('%m/%d/%Y')),
                 style={'display': 'inline-block',
                        'width': '17%',
                        'borderStyle': 'dashed',
                        'borderWidth': '2px',
                        'textAlign': 'center'}),
        html.Div(html.H5("audio_file_02192022.wav"),
                 style={'display': 'inline-block',
                        'width': '34%',
                        'borderStyle': 'dashed',
                        'borderWidth': '2px',
                        'textAlign': 'center'}),
        html.Div(html.H5("transcript_02192022.csv"),
                 style={'display': 'inline-block',
                        'width': '33%',
                        'borderStyle': 'dashed',
                        'borderWidth': '2px',
                        'textAlign': 'center'}),
        html.A(html.Button('Show Transcript', id="dispaly"), href="/", style={'display': 'inline-block'}),
    ], style= {'display': 'inline-block', 'margin': '10px', 'width': '120%', 'borderStyle': 'dashed',
                        'borderWidth': '1px', 'padding': '1rem'}),

layout = html.Div([
    html.H1("Transcript Archive"),
    html.Div(row),
    html.Div(id="archive", children=[])
],
style={'margin-left': '300px'})

@app.callback(Output("archive", "children"),
              [Input("stored_data", "data")])

def display_archive(data):
    return html.Div([
        html.H1(data)
        # dash_table.DataTable(
        # data.to_dict('records'),
        # [{'name': i, 'id': i} for i in data.columns]
        # ),
        #
        # html.Hr(),  # horizontal line
        #
        # # For debugging, display the raw contents provided by the web browser
        # html.Div('Raw Content'),
        # html.Pre(contents[0:200] + '...', style={
        #     'whiteSpace': 'pre-wrap',
        #     'wordBreak': 'break-all'
        # })
    ])