import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table

import pandas as pd
import os
from starter import app

UPLOAD_DIRECTORY = "\\assets"

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files'),

        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            'margin-left': '300px',
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-div', children=[]),
    html.Div(id='output-data-upload', children=[]),
])

@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))

def display_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

def parse_contents(contents, filename, date):
    if contents is not None:

        content_type, content_string = contents.split(',')
        # # # change this to a .wav use pipeline to get. test
        # data = content_string.encode("utf-8")
        # # rawdata = data.split(',')[1]
        decoded = base64.b64decode(content_string)
        try:
            # if '.wav' in filename:
            #     fh = open(f'assets/{filename}', "wb")
            #     fh.write(rawdata.decode('base64'))
            #     fh.close()

            if '.csv' in filename:
                # Assume that the user uploaded a CSV file
                df = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')))
            elif '.xls' in filename:
                # Assume that the user uploaded an excel file
                df = pd.read_excel(io.BytesIO(decoded))
            elif '.wav' in filename:
                # path =
                # AUDIO_FILE = io.StringIO(decoded.decode('utf-8'))
                # to_assets(filename)
                # Attempt to make the file playable
                df = pd.read_csv("assets/random.csv")
                html.Audio(id="audio", src=app.get_asset_url(filename), controls=True)
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])
        if '.csv' in filename or '.xls' in filename:
            return html.Div([
                html.H5(filename),
                html.H6(datetime.datetime.fromtimestamp(date)),

                dash_table.DataTable(
                    df.to_dict('records'),
                    [{'name': i, 'id': i} for i in df.columns]
                ),

                html.Hr(),  # horizontal line

                # For debugging, display the raw contents provided by the web browser
                html.Div('Raw Content'),
                html.Pre(contents[0:200] + '...', style={
                    'whiteSpace': 'pre-wrap',
                    'wordBreak': 'break-all'
                })
            ], id = 'transcript')
        else:
            return html.Div([
                html.H5(filename),
                # html.Button(html.Audio(id="audio", src=app.get_asset_url(filename), controls=True)),
                html.Button(html.Audio(id="audio", src=f'assets/{filename}', controls=True)),
                html.Div(style={'padding': '2rem'}),
                dash_table.DataTable(
                    df.to_dict('records'),
                    [{'name': i, 'id': i} for i in df.columns],
                    style_table={'textAlign': 'center'},
                ),

                html.Hr(),  # horizontal line

                # For debugging, display the raw contents provided by the web browser
                html.Div('Raw Content'),
                html.Pre(contents[0:200] + '...', style={
                    'whiteSpace': 'pre-wrap',
                    'wordBreak': 'break-all',
                })
            ],
            style={'margin-left': '300px'}
            )

# @app.callback(Output('stored-data', 'data'),
#               Input('transcript', 'transcript'))
#
# def put_in_data(transcript):
#     print(transcript)

@app.callback(Output('output-div', 'children'),
              Input('submit-button','n_clicks'),
              State('stored-data','data'),
              State('xaxis-data','value'),
              State('yaxis-data', 'value'))

def make_graphs(n, data, x_data, y_data):
    if n is None:
        return dash.no_update
    else:
        bar_fig = px.bar(data, x=x_data, y=y_data)
        # print(data)
        return dcc.Graph(figure=bar_fig)

# def to_assets(wave):
#     path = f"assets/{wave}"  # =====> here change the name of the direcotry to point to the static directory
#     with open(path, "a+") as file:
#         return

def to_assets(wave):
    path = f"assets/{wave}"  # =====> here change the name of the direcotry to point to the static directory
    with open(path, "a+") as file:
        # close(file)
        return

