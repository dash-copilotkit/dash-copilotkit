import os
import dash_copilotkit_components
from dash import Dash, callback, html, Input, Output, dcc

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.H1("CopilotKit Dash Component", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Select UI Type:"),
        dcc.Dropdown(
            id='ui-type-dropdown',
            options=[
                {'label': 'Chat Interface', 'value': 'chat'},
                {'label': 'Popup Chat', 'value': 'popup'},
                {'label': 'Sidebar Chat', 'value': 'sidebar'},
                {'label': 'AI Textarea', 'value': 'textarea'}
            ],
            value='chat'
        ),
        
        html.Label("Public API Key (optional):"),
        dcc.Input(
            id='api-key-input',
            type='text',
            placeholder='Enter your CopilotKit Cloud API key'
        ),
    ], style={'margin': '20px'}),
    
    html.Div(id='copilot-container', style={'margin': '20px'}),
    
    html.Div(id='output')
])

@callback(
    Output('copilot-container', 'children'),
    [Input('ui-type-dropdown', 'value'),
     Input('api-key-input', 'value')]
)
def update_copilot(ui_type, api_key):
    props = {
        'id': 'copilot',
        'ui_type': ui_type,
        'instructions': "You are a helpful AI assistant in a Dash application.",
        "public_api_key": os.getenv('CKC_PUBLIC_API_KEY')
    }
    
    if api_key:
        props['public_api_key'] = api_key
    
    return dash_copilotkit_components.DashCopilotkitComponents(**props)

@callback(
    Output('output', 'children'),
    Input('copilot', 'value'),
    prevent_initial_call=True
)
def display_output(value):
    if value:
        return f'Textarea value: {value}'
    return ''

if __name__ == '__main__':
    app.run(debug=True)
