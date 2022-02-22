# Add Model Retraining Page Here
# GET BUTTONS
import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table

import pandas as pd

from starter import app



layout = html.Div([
    html.H1("Select or Upload a Model"),
    # dcc.Upload(html.Button('Upload File'), id="upload-file"),

    html.Hr(),

    # dcc.Upload(html.A('Upload File')),

    # html.Hr(),

    dcc.Upload(
        id = "upload-file",
        children = [
        'Drag and Drop or ',
        html.A('Select a File')
    ], style={
        'width': '100%',
        'height': '60px',
        'lineHeight': '60px',
        'borderWidth': '1px',
        'borderStyle': 'dashed',
        'borderRadius': '5px',
        'textAlign': 'center'
        },
        multiple= True
    ),
    html.Div(id='output-data', children=[], style= {'margin': '20px'}),
    # Add a list of hard-coded models in separate div
    html.Div(id='models', children=[
        html.Button("Model 2", id='model-two'),
    ])
],
style={'margin-left': '300px'})

@app.callback(Output('output-data', 'children'),
              Input('upload-file', 'contents'),
              State('upload-file', 'filename'),
              State('upload-file', 'last_modified'))

def display_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

def parse_contents(contents, filename, date):
    if contents is not None:
        return html.Div([
            html.H5(f"Current model is: {filename}.json"),
        ])
