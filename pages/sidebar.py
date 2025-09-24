import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import dash_copilotkit_components
import os

# Register this page
dash.register_page(__name__, path='/sidebar', name='Sidebar Chat', title='Sidebar Chat - Dash CopilotKit')

def create_page_header():
    """Create the page header with description."""
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H1([
                        html.I(className="fas fa-bars me-3", style={"color": "#2563eb"}),
                        "Sidebar Chat"
                    ], className="display-5 fw-bold mb-3"),
                    
                    html.P([
                        "The sidebar chat interface slides in from the left or right side of your application. ",
                        "Perfect for applications where you want a persistent chat option that doesn't take up main content space."
                    ], className="lead text-muted mb-4"),
                    
                    dbc.Alert([
                        html.I(className="fas fa-info-circle me-2"),
                        "The sidebar can be positioned on either side and configured to show initially or remain hidden until triggered."
                    ], color="info", className="mb-4")
                ])
            ])
        ])
    ], className="py-4")

def create_configuration_panel():
    """Create the configuration panel for the sidebar interface."""
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
                            id="sidebar-api-key",
                            type="password",
                            placeholder="Enter your CopilotKit Cloud API key",
                            value=os.getenv('CKC_PUBLIC_API_KEY', '')
                        ),
                        dbc.Button([
                            html.I(className="fas fa-eye", id="sidebar-toggle-icon")
                        ], id="sidebar-toggle-password", color="outline-secondary")
                    ], className="mb-3"),
                    html.Small("Get your free API key from CopilotKit Cloud", className="text-muted")
                ], md=6),
                
                dbc.Col([
                    html.Label("Instructions", className="fw-bold mb-2"),
                    dbc.Textarea(
                        id="sidebar-instructions",
                        placeholder="Enter custom instructions for the AI assistant",
                        value="You are a helpful AI assistant available in the sidebar. Provide concise and helpful responses to user questions.",
                        rows=3
                    )
                ], md=6)
            ]),
            
            html.Hr(),
            
            dbc.Row([
                dbc.Col([
                    html.Label("Chat Title", className="fw-bold mb-2"),
                    dbc.Input(
                        id="sidebar-title",
                        placeholder="AI Assistant",
                        value="AI Assistant"
                    )
                ], md=3),
                
                dbc.Col([
                    html.Label("Initial Message", className="fw-bold mb-2"),
                    dbc.Input(
                        id="sidebar-initial",
                        placeholder="Hello! How can I assist you?",
                        value="Hello! I'm your AI assistant. How can I help you today?"
                    )
                ], md=3),
                
                dbc.Col([
                    html.Label("Position", className="fw-bold mb-2"),
                    dbc.Select(
                        id="sidebar-position",
                        options=[
                            {"label": "Right Side", "value": "right"},
                            {"label": "Left Side", "value": "left"}
                        ],
                        value="right"
                    )
                ], md=3),
                
                dbc.Col([
                    html.Label("Show Initially", className="fw-bold mb-2"),
                    dbc.Select(
                        id="sidebar-show-initially",
                        options=[
                            {"label": "Hidden", "value": "false"},
                            {"label": "Visible", "value": "true"}
                        ],
                        value="false"
                    )
                ], md=3)
            ])
        ])
    ], className="mb-4")

def create_demo_section():
    """Create the demo section with the sidebar component."""
    return dbc.Card([
        dbc.CardHeader([
            html.H5([
                html.I(className="fas fa-play me-2"),
                "Live Demo"
            ], className="mb-0")
        ]),
        dbc.CardBody([
            dbc.Alert([
                html.I(className="fas fa-hand-pointer me-2"),
                "Look for the sidebar toggle button! The sidebar will slide in from the configured side."
            ], color="success", className="mb-3"),
            
            html.Div([
                html.Div(id="sidebar-demo-container", className="position-relative border rounded", 
                        style={"minHeight": "500px", "backgroundColor": "#f8f9fa"}),
                
                # Sample content to show how sidebar works with existing content
                html.Div([
                    html.Div([
                        html.H3("Your Application Dashboard", className="text-center mb-4"),
                        
                        dbc.Row([
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardHeader("Analytics"),
                                    dbc.CardBody([
                                        html.H4("1,234", className="text-primary"),
                                        html.P("Total Users", className="text-muted")
                                    ])
                                ])
                            ], md=4),
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardHeader("Revenue"),
                                    dbc.CardBody([
                                        html.H4("$12,345", className="text-success"),
                                        html.P("This Month", className="text-muted")
                                    ])
                                ])
                            ], md=4),
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardHeader("Support"),
                                    dbc.CardBody([
                                        html.H4("98%", className="text-info"),
                                        html.P("Satisfaction", className="text-muted")
                                    ])
                                ])
                            ], md=4)
                        ], className="mb-4"),
                        
                        dbc.Card([
                            dbc.CardHeader("Recent Activity"),
                            dbc.CardBody([
                                html.P("• User John Doe signed up", className="mb-1"),
                                html.P("• New order #1234 received", className="mb-1"),
                                html.P("• Support ticket #567 resolved", className="mb-1"),
                                html.P("• System backup completed", className="mb-0")
                            ])
                        ])
                    ], className="p-4")
                ], className="position-absolute w-100 h-100")
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
    html.H1("My Dashboard"),
    html.Div("Your dashboard content goes here..."),
    
    # Sidebar chat component
    dash_copilotkit_components.DashCopilotkitComponents(
        id='sidebar-copilot',
        ui_type='sidebar',
        public_api_key='your-copilotkit-cloud-api-key',
        instructions='You are a helpful AI assistant in the sidebar.',
        labels={
            'title': 'AI Assistant',
            'initial': 'Hello! How can I help you today?'
        },
        position='right',  # 'left' or 'right'
        show_initially=False,  # Hidden by default
        width='350px'  # Sidebar width
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
    Output("sidebar-toggle-icon", "className"),
    Output("sidebar-api-key", "type"),
    Input("sidebar-toggle-password", "n_clicks"),
    prevent_initial_call=True
)
def toggle_password_visibility(n_clicks):
    if n_clicks and n_clicks % 2 == 1:
        return "fas fa-eye-slash", "text"
    return "fas fa-eye", "password"

@callback(
    Output("sidebar-demo-container", "children"),
    [Input("sidebar-api-key", "value"),
     Input("sidebar-instructions", "value"),
     Input("sidebar-title", "value"),
     Input("sidebar-initial", "value"),
     Input("sidebar-position", "value"),
     Input("sidebar-show-initially", "value")]
)
def update_sidebar_demo(api_key, instructions, title, initial, position, show_initially):
    if not api_key:
        return dbc.Alert([
            html.I(className="fas fa-key me-2"),
            "Please enter your CopilotKit Cloud API key to see the live demo."
        ], color="warning", className="text-center mt-5")
    
    return dash_copilotkit_components.DashCopilotkitComponents(
        id='sidebar-demo',
        ui_type='sidebar',
        public_api_key=api_key,
        instructions=instructions or "You are a helpful AI assistant in the sidebar.",
        labels={
            'title': title or 'AI Assistant',
            'initial': initial or 'Hello! How can I help you today?'
        },
        position=position or 'right',
        show_initially=show_initially == "true",
        width='350px'
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
