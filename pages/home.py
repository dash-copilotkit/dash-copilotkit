import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

# Register this page
dash.register_page(__name__, path='/', name='Home', title='Dash CopilotKit Components')

def create_hero_section():
    """Create the hero section for the home page."""
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H1([
                        html.I(className="fas fa-robot me-3", style={"color": "#2563eb"}),
                        "Dash CopilotKit Components"
                    ], className="display-4 fw-bold mb-4"),
                    
                    html.P([
                        "Integrate powerful AI chat interfaces into your Dash applications with ease. ",
                        "Choose from 4 different UI types and customize to fit your needs."
                    ], className="lead mb-4 text-muted"),
                    
                    html.Div([
                        dbc.Button([
                            html.I(className="fas fa-rocket me-2"),
                            "Get Started"
                        ], color="primary", size="lg", className="me-3", href="/chat"),
                        
                        dbc.Button([
                            html.I(className="fab fa-github me-2"),
                            "View on GitHub"
                        ], color="outline-secondary", size="lg", 
                           href="https://github.com/dash-copilotkit/dash-copilitkit", target="_blank"),
                    ], className="mb-5"),
                    
                    # Quick stats
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H3("4", className="fw-bold text-primary mb-0"),
                                html.P("UI Types", className="text-muted mb-0")
                            ], className="text-center")
                        ], md=3),
                        dbc.Col([
                            html.Div([
                                html.H3("∞", className="fw-bold text-primary mb-0"),
                                html.P("Customizable", className="text-muted mb-0")
                            ], className="text-center")
                        ], md=3),
                        dbc.Col([
                            html.Div([
                                html.H3("⚡", className="fw-bold text-primary mb-0"),
                                html.P("Fast Setup", className="text-muted mb-0")
                            ], className="text-center")
                        ], md=3),
                        dbc.Col([
                            html.Div([
                                html.H3("🔒", className="fw-bold text-primary mb-0"),
                                html.P("Secure", className="text-muted mb-0")
                            ], className="text-center")
                        ], md=3),
                    ], className="mt-5")
                ], className="text-center")
            ], lg=10, className="mx-auto")
        ])
    ], className="py-5")

def create_features_section():
    """Create the features section."""
    features = [
        {
            "icon": "fas fa-comments",
            "title": "Chat Interface",
            "description": "Full-featured chat interface embedded directly in your app",
            "link": "/chat"
        },
        {
            "icon": "fas fa-window-restore",
            "title": "Popup Chat",
            "description": "Toggleable popup chat window that doesn't interfere with your UI",
            "link": "/popup"
        },
        {
            "icon": "fas fa-bars",
            "title": "Sidebar Chat",
            "description": "Slide-in sidebar chat that can be positioned left or right",
            "link": "/sidebar"
        },
        {
            "icon": "fas fa-edit",
            "title": "AI Textarea",
            "description": "AI-powered textarea that helps users write better content",
            "link": "/textarea"
        }
    ]
    
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H2("Choose Your Interface", className="text-center mb-5 fw-bold"),
                html.P("Select the perfect AI interface for your application", 
                       className="text-center text-muted mb-5 lead")
            ])
        ]),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Div([
                            html.I(className=f"{feature['icon']} fa-3x text-primary mb-3"),
                            html.H4(feature['title'], className="fw-bold mb-3"),
                            html.P(feature['description'], className="text-muted mb-4"),
                            dbc.Button([
                                "Try it out ",
                                html.I(className="fas fa-arrow-right")
                            ], color="outline-primary", href=feature['link'], className="w-100")
                        ], className="text-center")
                    ])
                ], className="h-100 shadow-sm border-0")
            ], md=6, lg=3, className="mb-4") for feature in features
        ])
    ], className="py-5")

def create_installation_section():
    """Create the installation section."""
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H2("Quick Installation", className="text-center mb-5 fw-bold"),
                
                dbc.Card([
                    dbc.CardBody([
                        html.H5("1. Install the package", className="fw-bold mb-3"),
                        dcc.Markdown("""
```bash
pip install dash-copilotkit-components
```
                        """, className="mb-4"),
                        
                        html.H5("2. Basic usage", className="fw-bold mb-3"),
                        dcc.Markdown("""
```python
import dash_copilotkit_components
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    dash_copilotkit_components.DashCopilotkitComponents(
        id='copilot',
        ui_type='chat',
        public_api_key='your-api-key',
        instructions="You are a helpful AI assistant."
    )
])

if __name__ == '__main__':
    app.run(debug=True)
```
                        """, className="mb-4"),
                        
                        html.H5("3. Get your API key", className="fw-bold mb-3"),
                        html.P([
                            "Get your free API key from ",
                            html.A("CopilotKit Cloud", href="https://cloud.copilotkit.ai", target="_blank", className="text-primary"),
                            " or use your own OpenAI key with a custom runtime."
                        ], className="text-muted")
                    ])
                ], className="shadow-sm border-0")
            ], lg=8, className="mx-auto")
        ])
    ], className="py-5 bg-light")

# Page layout
layout = html.Div([
    create_hero_section(),
    create_features_section(),
    create_installation_section()
])
