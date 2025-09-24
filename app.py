import dash
from dash import Dash, html, dcc, Input, Output, callback, page_container
import dash_bootstrap_components as dbc

# Initialize the Dash app with pages support
app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
    ],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        {"name": "description", "content": "Dash CopilotKit Components - AI-powered chat interfaces for Dash applications"},
        {"name": "keywords", "content": "dash, copilotkit, ai, chatbot, react, python"},
        {"name": "author", "content": "Dash CopilotKit Team"}
    ]
)

# App title and favicon
app.title = "Dash CopilotKit Components"

def create_navbar():
    """Create the navigation bar with modern styling."""
    return dbc.Navbar(
        dbc.Container([
            # Brand/Logo
            dbc.NavbarBrand([
                html.I(className="fas fa-robot me-2"),
                "Dash CopilotKit"
            ], href="/", className="fw-bold fs-4"),
            
            # Navigation items
            dbc.Nav([
                dbc.NavItem(dbc.NavLink([
                    html.I(className="fas fa-home me-1"),
                    "Home"
                ], href="/", active="exact")),
                
                dbc.NavItem(dbc.NavLink([
                    html.I(className="fas fa-comments me-1"),
                    "Chat"
                ], href="/chat", active="exact")),
                
                dbc.NavItem(dbc.NavLink([
                    html.I(className="fas fa-window-restore me-1"),
                    "Popup"
                ], href="/popup", active="exact")),
                
                dbc.NavItem(dbc.NavLink([
                    html.I(className="fas fa-bars me-1"),
                    "Sidebar"
                ], href="/sidebar", active="exact")),
                
                dbc.NavItem(dbc.NavLink([
                    html.I(className="fas fa-edit me-1"),
                    "Textarea"
                ], href="/textarea", active="exact")),
                
                dbc.NavItem(dbc.NavLink([
                    html.I(className="fab fa-github me-1"),
                    "GitHub"
                ], href="https://github.com/dash-copilotkit/dash-copilitkit", target="_blank")),
            ], navbar=True, className="ms-auto"),
        ], fluid=True),
        color="light",
        sticky="top",
        className="shadow-sm mb-4"
    )

def create_footer():
    """Create the footer with links and information."""
    return dbc.Container([
        html.Hr(),
        dbc.Row([
            dbc.Col([
                html.H5("Dash CopilotKit Components", className="fw-bold"),
                html.P("AI-powered chat interfaces for Dash applications", className="text-muted"),
                html.Div([
                    dbc.Button([
                        html.I(className="fab fa-github me-1"),
                        "GitHub"
                    ], href="https://github.com/dash-copilotkit/dash-copilitkit", 
                       target="_blank", color="outline-primary", size="sm", className="me-2"),
                    
                    dbc.Button([
                        html.I(className="fas fa-book me-1"),
                        "Documentation"
                    ], href="https://dash-copilotkit.biyani.xyz", 
                       target="_blank", color="outline-secondary", size="sm"),
                ])
            ], md=6),
            
            dbc.Col([
                html.H6("Quick Links", className="fw-bold"),
                html.Ul([
                    html.Li(html.A("CopilotKit Docs", href="https://docs.copilotkit.ai", target="_blank")),
                    html.Li(html.A("Dash Documentation", href="https://dash.plotly.com", target="_blank")),
                    html.Li(html.A("Get API Key", href="https://cloud.copilotkit.ai", target="_blank")),
                ], className="list-unstyled")
            ], md=3),
            
            dbc.Col([
                html.H6("Support", className="fw-bold"),
                html.Ul([
                    html.Li(html.A("Issues", href="https://github.com/dash-copilotkit/dash-copilitkit/issues", target="_blank")),
                    html.Li(html.A("Discussions", href="https://github.com/dash-copilotkit/dash-copilitkit/discussions", target="_blank")),
                    html.Li(html.A("Examples", href="/", target="_blank")),
                ], className="list-unstyled")
            ], md=3),
        ]),
        
        html.Hr(),
        dbc.Row([
            dbc.Col([
                html.P([
                    "© 2024 Dash CopilotKit Components. Built with ❤️ using ",
                    html.A("Dash", href="https://dash.plotly.com", target="_blank"),
                    " and ",
                    html.A("CopilotKit", href="https://copilotkit.ai", target="_blank"),
                    "."
                ], className="text-muted text-center mb-0")
            ])
        ])
    ], className="py-4")

# Main app layout
app.layout = html.Div([
    create_navbar(),
    
    # Main content area
    dbc.Container([
        page_container
    ], fluid=True, className="flex-grow-1"),
    
    # Footer
    create_footer()
], className="d-flex flex-column min-vh-100")

if __name__ == '__main__':
    app.run(debug=True, port=8050)
