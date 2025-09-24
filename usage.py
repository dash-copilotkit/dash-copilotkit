import dash_copilotkit_components
from dash import Dash, callback, html, Input, Output, dcc
import os
from typing import Any, Dict

app = Dash(__name__, suppress_callback_exceptions=True)

# Example layout demonstrating all 4 UI types
app.layout = html.Div([
    html.H1("CopilotKit Dash Components Demo", style={'textAlign': 'center', 'marginBottom': '30px'}),

    # Instructions
    html.Div([
        html.P("This demo showcases all 4 CopilotKit UI types. Configure your API key below:"),
        html.P("Option 1: Use CopilotKit Cloud (get your key at https://cloud.copilotkit.ai)"),
        html.P("Option 2: Bring your own key with a runtime URL"),
    ], style={'marginBottom': '20px', 'padding': '10px', 'backgroundColor': '#f0f0f0', 'borderRadius': '5px'}),

    # Configuration inputs
    html.Div([
        html.Label("CopilotKit Cloud Public API Key:"),
        dcc.Input(
            id='public-api-key-input',
            type='text',
            placeholder='Enter your CopilotKit Cloud public API key',
            style={'width': '100%', 'marginBottom': '10px'}
        ),
        html.Label("Runtime URL (for bring your own key):"),
        dcc.Input(
            id='runtime-url-input',
            type='text',
            placeholder='Enter your runtime URL (e.g., http://localhost:3000/api/copilotkit)',
            style={'width': '100%', 'marginBottom': '10px'}
        ),
        html.Label("Select UI Type:"),
        dcc.Dropdown(
            id='ui-type-dropdown',
            options=[
                {'label': 'Chat Interface', 'value': 'chat'},
                {'label': 'Popup Chat', 'value': 'popup'},
                {'label': 'Sidebar Chat', 'value': 'sidebar'},
                {'label': 'AI Textarea', 'value': 'textarea'}
            ],
            value='chat',
            style={'marginBottom': '20px'}
        )
    ], style={'marginBottom': '30px', 'padding': '15px', 'border': '1px solid #ddd', 'borderRadius': '5px'}),

    # CopilotKit Component
    html.Div(id='copilot-container'),
    # Output for textarea mode
    html.Div(id='textarea-output', style={'marginTop': '20px'})
])


@callback(
    Output('copilot-container', 'children'),
    [Input('ui-type-dropdown', 'value'),
     Input('public-api-key-input', 'value'),
     Input('runtime-url-input', 'value')]
)
def update_copilot_component(ui_type, public_api_key, runtime_url):
    """Update the CopilotKit component based on selected configuration."""

    # Prepare component props
    component_props: Dict[str, Any] = {
        'id': 'copilot-component',
        'ui_type': ui_type,
        'instructions': f"You are a helpful AI assistant integrated into a Dash application. "
                       f"You are currently displayed as a {ui_type} interface. "
                       f"Help users with their questions and tasks.",
        'labels': {
            'title': f"AI Assistant ({ui_type.title()})",
            'initial': f"Hello! I'm your AI assistant in {ui_type} mode. How can I help you today?"
        }
    }

    # Add API configuration
    if public_api_key:
        component_props['public_api_key'] = public_api_key
    elif runtime_url:
        component_props['runtime_url'] = runtime_url
    else:
        # Show configuration message
        return html.Div([
            html.P("⚠️ Please configure either a CopilotKit Cloud API key or a runtime URL to use the component.",
                   style={'color': 'orange', 'fontWeight': 'bold', 'textAlign': 'center', 'padding': '20px'})
        ])

    # Customize props based on UI type
    if ui_type == 'chat':
        component_props.update({
            'width': '100%',
            'height': '500px'
        })
    elif ui_type == 'popup':
        component_props.update({
            'show_initially': False
        })
    elif ui_type == 'sidebar':
        component_props.update({
            'position': 'right',
            'show_initially': False
        })
    elif ui_type == 'textarea':
        component_props.update({
            'placeholder': 'Start typing here... The AI will help you write better content!',
            'width': '100%',
            'height': '200px',
            'value': ''
        })

    return dash_copilotkit_components.DashCopilotkitComponents(**component_props)


@callback(
    Output('textarea-output', 'children'),
    Input('copilot-component', 'value'),
    prevent_initial_call=True
)
def display_textarea_output(value):
    """Display the textarea content for textarea mode."""
    if value:
        return html.Div([
            html.H4("Textarea Content:"),
            html.Pre(value, style={
                'backgroundColor': '#f8f9fa',
                'padding': '10px',
                'borderRadius': '5px',
                'border': '1px solid #dee2e6',
                'whiteSpace': 'pre-wrap'
            })
        ])
    return ""


if __name__ == '__main__':
    # Use app.run() for Dash 3.0 compatibility
    app.run(debug=True, port=9050)
