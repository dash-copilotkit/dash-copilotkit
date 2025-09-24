import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import dash_copilotkit_components
import os

# Register this page
dash.register_page(__name__, path='/chat', name='Chat Interface', title='Chat Interface - Dash CopilotKit')

def create_page_header():
    """Create the page header with description."""
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H1([
                        html.I(className="fas fa-comments me-3", style={"color": "#2563eb"}),
                        "Chat Interface"
                    ], className="display-5 fw-bold mb-3"),
                    
                    html.P([
                        "The chat interface provides a full-featured chat experience embedded directly in your application. ",
                        "Perfect for customer support, interactive assistants, or any conversational AI use case."
                    ], className="lead text-muted mb-4"),
                    
                    dbc.Alert([
                        html.I(className="fas fa-info-circle me-2"),
                        "This demo uses a placeholder API key. Add your own CopilotKit Cloud API key below to enable real AI responses."
                    ], color="info", className="mb-4")
                ])
            ])
        ])
    ], className="py-4")

def create_configuration_panel():
    """Create the configuration panel for the chat interface."""
    return dbc.Card([
        dbc.CardHeader([
            html.H5([
                html.I(className="fas fa-cog me-2"),
                "Configuration"
            ], className="mb-0")
        ]),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.Label("API Key", className="fw-bold mb-2"),
                    dbc.InputGroup([
                        dbc.Input(
                            id="chat-api-key",
                            type="password",
                            placeholder="Enter your CopilotKit Cloud API key",
                            value=os.getenv('CKC_PUBLIC_API_KEY', '')
                        ),
                        dbc.Button([
                            html.I(className="fas fa-eye", id="chat-toggle-icon")
                        ], id="chat-toggle-password", color="outline-secondary")
                    ], className="mb-3"),
                    html.Small("Get your free API key from CopilotKit Cloud", className="text-muted")
                ], md=6),
                
                dbc.Col([
                    html.Label("Instructions", className="fw-bold mb-2"),
                    dbc.Textarea(
                        id="chat-instructions",
                        placeholder="Enter custom instructions for the AI assistant",
                        value="You are a helpful AI assistant integrated into a Dash application. Help users with their questions and provide clear, concise answers.",
                        rows=3
                    )
                ], md=6)
            ]),
            
            html.Hr(),
            
            dbc.Row([
                dbc.Col([
                    html.Label("Chat Title", className="fw-bold mb-2"),
                    dbc.Input(
                        id="chat-title",
                        placeholder="Chat Assistant",
                        value="AI Assistant"
                    )
                ], md=4),
                
                dbc.Col([
                    html.Label("Initial Message", className="fw-bold mb-2"),
                    dbc.Input(
                        id="chat-initial",
                        placeholder="Hello! How can I help you?",
                        value="Hello! I'm your AI assistant. How can I help you today?"
                    )
                ], md=4),
                
                dbc.Col([
                    html.Label("Height", className="fw-bold mb-2"),
                    dbc.Select(
                        id="chat-height",
                        options=[
                            {"label": "400px", "value": "400px"},
                            {"label": "500px", "value": "500px"},
                            {"label": "600px", "value": "600px"},
                            {"label": "700px", "value": "700px"}
                        ],
                        value="500px"
                    )
                ], md=4)
            ])
        ])
    ], className="mb-4")

def create_demo_section():
    """Create the demo section with the chat component."""
    return dbc.Card([
        dbc.CardHeader([
            html.H5([
                html.I(className="fas fa-play me-2"),
                "Live Demo"
            ], className="mb-0")
        ]),
        dbc.CardBody([
            html.Div(id="chat-demo-container", className="border rounded p-3", 
                    style={"minHeight": "500px", "backgroundColor": "#f8f9fa"})
        ])
    ])

def create_code_example():
    """Create the code example section."""
    return dbc.Card([
        dbc.CardHeader([
            html.H5([
                html.I(className="fas fa-code me-2"),
                "Code Example"
            ], className="mb-0")
        ]),
        dbc.CardBody([
            dcc.Markdown("""
```python
import dash_copilotkit_components
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    dash_copilotkit_components.DashCopilotkitComponents(
        id='chat-copilot',
        ui_type='chat',
        public_api_key='your-copilotkit-cloud-api-key',
        instructions='You are a helpful AI assistant.',
        labels={
            'title': 'AI Assistant',
            'initial': 'Hello! How can I help you today?'
        },
        height='500px',
        width='100%'
    )
])

if __name__ == '__main__':
    app.run(debug=True)
```
            """, className="mb-0")
        ])
    ], className="mt-4")

# Callbacks
@callback(
    Output("chat-toggle-icon", "className"),
    Output("chat-api-key", "type"),
    Input("chat-toggle-password", "n_clicks"),
    prevent_initial_call=True
)
def toggle_password_visibility(n_clicks):
    if n_clicks and n_clicks % 2 == 1:
        return "fas fa-eye-slash", "text"
    return "fas fa-eye", "password"

@callback(
    Output("chat-demo-container", "children"),
    [Input("chat-api-key", "value"),
     Input("chat-instructions", "value"),
     Input("chat-title", "value"),
     Input("chat-initial", "value"),
     Input("chat-height", "value")]
)
def update_chat_demo(api_key, instructions, title, initial, height):
    if not api_key:
        return dbc.Alert([
            html.I(className="fas fa-key me-2"),
            "Please enter your CopilotKit Cloud API key to see the live demo."
        ], color="warning", className="text-center")
    
    return dash_copilotkit_components.DashCopilotkitComponents(
        id='chat-demo',
        ui_type='chat',
        public_api_key=api_key,
        instructions=instructions or "You are a helpful AI assistant.",
        labels={
            'title': title or 'AI Assistant',
            'initial': initial or 'Hello! How can I help you today?'
        },
        height=height,
        width='100%'
    )

# Page layout
layout = html.Div([
    create_page_header(),
    dbc.Container([
        create_configuration_panel(),
        create_demo_section(),
        create_code_example()
    ], className="pb-5")
])
