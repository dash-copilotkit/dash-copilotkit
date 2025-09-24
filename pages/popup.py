import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import dash_copilotkit_components
import os

# Register this page
dash.register_page(__name__, path='/popup', name='Popup Chat', title='Popup Chat - Dash CopilotKit')

def create_page_header():
    """Create the page header with description."""
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H1([
                        html.I(className="fas fa-window-restore me-3", style={"color": "#2563eb"}),
                        "Popup Chat"
                    ], className="display-5 fw-bold mb-3"),
                    
                    html.P([
                        "The popup chat interface provides a toggleable chat window that appears over your application. ",
                        "Perfect for customer support or help systems where you want the chat to be available but not always visible."
                    ], className="lead text-muted mb-4"),
                    
                    dbc.Alert([
                        html.I(className="fas fa-info-circle me-2"),
                        "Click the chat button to open/close the popup. The popup can be configured to show initially or remain hidden until triggered."
                    ], color="info", className="mb-4")
                ])
            ])
        ])
    ], className="py-4")

def create_configuration_panel():
    """Create the configuration panel for the popup interface."""
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
                            id="popup-api-key",
                            type="password",
                            placeholder="Enter your CopilotKit Cloud API key",
                            value=os.getenv('CKC_PUBLIC_API_KEY', '')
                        ),
                        dbc.Button([
                            html.I(className="fas fa-eye", id="popup-toggle-icon")
                        ], id="popup-toggle-password", color="outline-secondary")
                    ], className="mb-3"),
                    html.Small("Get your free API key from CopilotKit Cloud", className="text-muted")
                ], md=6),
                
                dbc.Col([
                    html.Label("Instructions", className="fw-bold mb-2"),
                    dbc.Textarea(
                        id="popup-instructions",
                        placeholder="Enter custom instructions for the AI assistant",
                        value="You are a helpful customer support AI assistant. Provide quick and accurate help to users.",
                        rows=3
                    )
                ], md=6)
            ]),
            
            html.Hr(),
            
            dbc.Row([
                dbc.Col([
                    html.Label("Chat Title", className="fw-bold mb-2"),
                    dbc.Input(
                        id="popup-title",
                        placeholder="Support Assistant",
                        value="Support Assistant"
                    )
                ], md=3),
                
                dbc.Col([
                    html.Label("Initial Message", className="fw-bold mb-2"),
                    dbc.Input(
                        id="popup-initial",
                        placeholder="How can I help you?",
                        value="Hi! I'm here to help. What can I assist you with?"
                    )
                ], md=3),
                
                dbc.Col([
                    html.Label("Show Initially", className="fw-bold mb-2"),
                    dbc.Select(
                        id="popup-show-initially",
                        options=[
                            {"label": "Hidden", "value": "false"},
                            {"label": "Visible", "value": "true"}
                        ],
                        value="false"
                    )
                ], md=3),
                
                dbc.Col([
                    html.Label("Position", className="fw-bold mb-2"),
                    dbc.Select(
                        id="popup-position",
                        options=[
                            {"label": "Bottom Right", "value": "bottom-right"},
                            {"label": "Bottom Left", "value": "bottom-left"},
                            {"label": "Top Right", "value": "top-right"},
                            {"label": "Top Left", "value": "top-left"}
                        ],
                        value="bottom-right"
                    )
                ], md=3)
            ])
        ])
    ], className="mb-4")

def create_demo_section():
    """Create the demo section with the popup component."""
    return dbc.Card([
        dbc.CardHeader([
            html.H5([
                html.I(className="fas fa-play me-2"),
                "Live Demo"
            ], className="mb-0")
        ]),
        dbc.CardBody([
            dbc.Alert([
                html.I(className="fas fa-mouse-pointer me-2"),
                "The popup chat will appear in the corner of this demo area. Look for the chat button!"
            ], color="success", className="mb-3"),
            
            html.Div([
                html.Div(id="popup-demo-container", className="position-relative border rounded p-4", 
                        style={"minHeight": "400px", "backgroundColor": "#f8f9fa"}),
                
                # Sample content to show how popup works with existing content
                html.Div([
                    html.H4("Your Application Content", className="text-center text-muted mb-4"),
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.H5("Feature 1", className="card-title"),
                                    html.P("This is some sample content to demonstrate how the popup chat works alongside your existing application.", className="card-text")
                                ])
                            ])
                        ], md=6),
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.H5("Feature 2", className="card-title"),
                                    html.P("The popup chat will appear over this content when activated, providing help without navigating away.", className="card-text")
                                ])
                            ])
                        ], md=6)
                    ])
                ], className="p-4")
            ], className="position-relative")
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
    # Your existing app content
    html.H1("My Application"),
    html.P("Your app content goes here..."),
    
    # Popup chat component
    dash_copilotkit_components.DashCopilotkitComponents(
        id='popup-copilot',
        ui_type='popup',
        public_api_key='your-copilotkit-cloud-api-key',
        instructions='You are a helpful customer support assistant.',
        labels={
            'title': 'Support Assistant',
            'initial': 'Hi! How can I help you today?'
        },
        show_initially=False,  # Hidden by default
        position='bottom-right'  # Position in corner
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
    Output("popup-toggle-icon", "className"),
    Output("popup-api-key", "type"),
    Input("popup-toggle-password", "n_clicks"),
    prevent_initial_call=True
)
def toggle_password_visibility(n_clicks):
    if n_clicks and n_clicks % 2 == 1:
        return "fas fa-eye-slash", "text"
    return "fas fa-eye", "password"

@callback(
    Output("popup-demo-container", "children"),
    [Input("popup-api-key", "value"),
     Input("popup-instructions", "value"),
     Input("popup-title", "value"),
     Input("popup-initial", "value"),
     Input("popup-show-initially", "value"),
     Input("popup-position", "value")]
)
def update_popup_demo(api_key, instructions, title, initial, show_initially, position):
    if not api_key:
        return dbc.Alert([
            html.I(className="fas fa-key me-2"),
            "Please enter your CopilotKit Cloud API key to see the live demo."
        ], color="warning", className="text-center")
    
    return dash_copilotkit_components.DashCopilotkitComponents(
        id='popup-demo',
        ui_type='popup',
        public_api_key=api_key,
        instructions=instructions or "You are a helpful customer support assistant.",
        labels={
            'title': title or 'Support Assistant',
            'initial': initial or 'Hi! How can I help you today?'
        },
        show_initially=show_initially == "true",
        position=position or 'bottom-right'
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
