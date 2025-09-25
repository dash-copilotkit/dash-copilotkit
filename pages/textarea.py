import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import dash_copilotkit_components
import os

# Register this page
dash.register_page(__name__, path='/textarea', name='AI Textarea', title='AI Textarea - Dash CopilotKit')

def create_page_header():
    """Create the page header with description."""
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H1([
                        html.I(className="fas fa-edit me-3", style={"color": "#2563eb"}),
                        "AI Textarea"
                    ], className="display-5 fw-bold mb-3"),
                    
                    html.P([
                        "The AI textarea provides an intelligent text input field that helps users write better content. ",
                        "Perfect for forms, content creation, email composition, or any text input that benefits from AI assistance."
                    ], className="lead text-muted mb-4"),
                    
                    dbc.Alert([
                        html.I(className="fas fa-info-circle me-2"),
                        "Start typing in the textarea below and the AI will provide suggestions and improvements as you write."
                    ], color="info", className="mb-4")
                ])
            ])
        ])
    ], className="py-4")

def create_configuration_panel():
    """Create the configuration panel for the textarea interface."""
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
                            id="textarea-api-key",
                            type="password",
                            placeholder="Enter your CopilotKit Cloud API key",
                            value=os.getenv('CKC_PUBLIC_API_KEY', '')
                        ),
                        dbc.Button([
                            html.I(className="fas fa-eye", id="textarea-toggle-icon")
                        ], id="textarea-toggle-password", color="outline-secondary")
                    ], className="mb-3"),
                    html.Small("Get your free API key from CopilotKit Cloud", className="text-muted")
                ], md=6),
                
                dbc.Col([
                    html.Label("Instructions", className="fw-bold mb-2"),
                    dbc.Textarea(
                        id="textarea-instructions",
                        placeholder="Enter custom instructions for the AI assistant",
                        value="You are a helpful writing assistant. Help users improve their writing by providing suggestions, corrections, and enhancements.",
                        rows=3
                    )
                ], md=6)
            ]),
            
            html.Hr(),
            
            dbc.Row([
                dbc.Col([
                    html.Label("Placeholder Text", className="fw-bold mb-2"),
                    dbc.Input(
                        id="textarea-placeholder",
                        placeholder="Start typing here...",
                        value="Start writing your content here. The AI will help you improve it as you type..."
                    )
                ], md=4),
                
                dbc.Col([
                    html.Label("Height", className="fw-bold mb-2"),
                    dbc.Select(
                        id="textarea-height",
                        options=[
                            {"label": "200px", "value": "200px"},
                            {"label": "300px", "value": "300px"},
                            {"label": "400px", "value": "400px"},
                            {"label": "500px", "value": "500px"}
                        ],
                        value="300px"
                    )
                ], md=4),

                dbc.Col([
                    html.Label("Width", className="fw-bold mb-2"),
                    dbc.Select(
                        id="textarea-width",
                        options=[
                            {"label": "100%", "value": "100%"},
                            {"label": "80%", "value": "80%"},
                            {"label": "500px", "value": "500px"},
                            {"label": "600px", "value": "600px"}
                        ],
                        value="100%"
                    )
                ], md=4)
            ])
        ])
    ], className="mb-4")

def create_demo_section():
    """Create the demo section with the textarea component."""
    return dbc.Card([
        dbc.CardHeader([
            html.H5([
                html.I(className="fas fa-play me-2"),
                "Live Demo"
            ], className="mb-0")
        ]),
        dbc.CardBody([
            dbc.Alert([
                html.I(className="fas fa-keyboard me-2"),
                "Start typing in the textarea below. The AI will provide real-time suggestions and improvements!"
            ], color="success", className="mb-3"),
            
            html.Div(id="textarea-demo-container", className="mb-4"),
            
            # Output display
            html.Div([
                html.H6("Current Content:", className="fw-bold mb-2"),
                html.Div(id="textarea-output", className="border rounded p-3 bg-light", 
                        style={"minHeight": "100px", "whiteSpace": "pre-wrap"})
            ])
        ])
    ])

def create_use_cases_section():
    """Create the use cases section."""
    use_cases = [
        {
            "title": "Email Composition",
            "description": "Help users write professional emails with proper tone and structure",
            "icon": "fas fa-envelope"
        },
        {
            "title": "Content Creation",
            "description": "Assist with blog posts, articles, and marketing copy",
            "icon": "fas fa-pen-fancy"
        },
        {
            "title": "Form Assistance",
            "description": "Guide users through complex form fields and descriptions",
            "icon": "fas fa-wpforms"
        },
        {
            "title": "Code Documentation",
            "description": "Help developers write better comments and documentation",
            "icon": "fas fa-code"
        }
    ]
    
    return dbc.Card([
        dbc.CardHeader([
            html.H5([
                html.I(className="fas fa-lightbulb me-2"),
                "Use Cases"
            ], className="mb-0")
        ]),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.I(className=f"{case['icon']} fa-2x text-primary mb-3"),
                        html.H6(case['title'], className="fw-bold mb-2"),
                        html.P(case['description'], className="text-muted mb-0")
                    ], className="text-center")
                ], md=6, lg=3, className="mb-3") for case in use_cases
            ])
        ])
    ], className="mt-4")

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
from dash import Dash, html, callback, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H1("AI-Powered Text Editor"),
    
    # AI Textarea component
    dash_copilotkit_components.DashCopilotkitComponents(
        id='ai-textarea',
        ui_type='textarea',
        public_api_key='your-copilotkit-cloud-api-key',
        instructions='You are a helpful writing assistant.',
        placeholder='Start writing your content here...',
        value='',
        rows=10,
        auto_resize=True
    ),
    
    # Display the current content
    html.Div(id='content-output')
])

@callback(
    Output('content-output', 'children'),
    Input('ai-textarea', 'value')
)
def display_content(value):
    return f"Current content: {value or 'No content yet...'}"

if __name__ == '__main__':
    app.run(debug=True)
```
            """, className="mb-0")
        ])
    ], className="mt-4")

# Callbacks
@callback(
    Output("textarea-toggle-icon", "className", allow_duplicate=True),
    Output("textarea-api-key", "type", allow_duplicate=True),
    Input("textarea-toggle-password", "n_clicks"),
    prevent_initial_call=True
)
def toggle_password_visibility(n_clicks):
    if n_clicks and n_clicks % 2 == 1:
        return "fas fa-eye-slash", "text"
    return "fas fa-eye", "password"

@callback(
    Output("textarea-demo-container", "children", allow_duplicate=True),
    [Input("textarea-api-key", "value"),
     Input("textarea-instructions", "value"),
     Input("textarea-placeholder", "value"),
     Input("textarea-height", "value"),
     Input("textarea-width", "value")],
    prevent_initial_call=True
)
def update_textarea_demo(api_key, instructions, placeholder, height, width):
    if not api_key:
        return dbc.Alert([
            html.I(className="fas fa-key me-2"),
            "Please enter your CopilotKit Cloud API key to see the live demo."
        ], color="warning", className="text-center")
    
    return dash_copilotkit_components.DashCopilotkitComponents(
        id='textarea-demo',
        ui_type='textarea',
        public_api_key=api_key,
        instructions=instructions or "You are a helpful writing assistant.",
        placeholder=placeholder or "Start typing here...",
        value="",  # Initialize with empty string
        height=height or "300px",
        width=width or "100%"
    )

# REMOVED THE PROBLEMATIC CIRCULAR CALLBACK
# The React component handles the value updates internally, no need for Python callback

@callback(
    Output("textarea-output", "children", allow_duplicate=True),
    Input("textarea-demo", "value"),
    prevent_initial_call=True
)
def display_textarea_output(value):
    """Display the current textarea content."""

    # Handle case where value might be an event object (shouldn't happen now)
    if isinstance(value, dict):
        if 'target' in value and 'value' in value['target']:
            actual_value = value['target']['value']
        elif 'currentTarget' in value and 'value' in value['currentTarget']:
            actual_value = value['currentTarget']['value']
        else:
            actual_value = ""
    else:
        actual_value = value
    
    if actual_value:
        return actual_value
    return "No content yet. Start typing in the textarea above..."

# Page layout
layout = html.Div([
    create_page_header(),
    dbc.Container([
        create_configuration_panel(),
        create_demo_section(),
        create_use_cases_section(),
        create_code_example()
    ], className="pb-5")
])
