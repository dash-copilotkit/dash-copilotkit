# Basic Examples

Get started with simple examples of each UI type in Dash CopilotKit Components.

## Chat Interface

### Simple Chat

```python
import dash
from dash import html
import dash_copilotkit_components

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Simple Chat Example"),
    
    dash_copilotkit_components.DashCopilotkitComponents(
        id='simple-chat',
        ui_type='chat',
        public_api_key='your-copilotkit-cloud-api-key',
        instructions='You are a helpful assistant.',
        height='400px'
    )
])

if __name__ == '__main__':
    app.run(debug=True)
```

### Customer Support Chat

```python
import dash
from dash import html
import dash_copilotkit_components

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Customer Support"),
    html.P("Get help with your questions and issues."),
    
    dash_copilotkit_components.DashCopilotkitComponents(
        id='support-chat',
        ui_type='chat',
        public_api_key='your-copilotkit-cloud-api-key',
        instructions='''
        You are a friendly customer support assistant for TechCorp.
        - Help users with product questions and technical issues
        - Be professional and empathetic
        - If you can't solve an issue, offer to escalate to human support
        - Keep responses concise but helpful
        ''',
        labels={
            'title': 'Customer Support',
            'initial': 'Hi! I\'m here to help with any questions about our products and services. How can I assist you today?'
        },
        height='500px'
    )
])

if __name__ == '__main__':
    app.run(debug=True)
```

## Popup Chat

### Basic Popup

```python
import dash
from dash import html
import dash_copilotkit_components

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("My Application"),
    html.P("This is the main content of your application."),
    html.P("The popup chat will appear in the bottom corner."),
    
    # Popup chat - doesn't interfere with layout
    dash_copilotkit_components.DashCopilotkitComponents(
        id='popup-chat',
        ui_type='popup',
        public_api_key='your-copilotkit-cloud-api-key',
        instructions='You are a helpful assistant for this application.',
        show_initially=False
    )
])

if __name__ == '__main__':
    app.run(debug=True)
```

### Help System Popup

```python
import dash
from dash import html, dcc
import dash_copilotkit_components

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Application"),
    
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [{'x': [1, 2, 3, 4], 'y': [4, 5, 3, 6], 'type': 'bar'}],
            'layout': {'title': 'Sample Chart'}
        }
    ),
    
    html.Div([
        html.H3("Key Metrics"),
        html.P("Revenue: $125,000"),
        html.P("Users: 1,250"),
        html.P("Growth: +15%")
    ]),
    
    # Help popup
    dash_copilotkit_components.DashCopilotkitComponents(
        id='help-popup',
        ui_type='popup',
        public_api_key='your-copilotkit-cloud-api-key',
        instructions='''
        You are a help assistant for this dashboard application.
        Help users understand:
        - How to read the charts and metrics
        - How to navigate the dashboard
        - What different features do
        - How to interpret the data
        ''',
        labels={
            'title': 'Dashboard Help',
            'initial': 'Hi! I can help you understand and navigate this dashboard. What would you like to know?'
        }
    )
])

if __name__ == '__main__':
    app.run(debug=True)
```

## Sidebar Chat

### Right Sidebar

```python
import dash
from dash import html, dcc
import dash_copilotkit_components

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Analytics Dashboard"),
    
    html.Div([
        dcc.Graph(
            id='main-chart',
            figure={
                'data': [
                    {'x': ['Jan', 'Feb', 'Mar', 'Apr'], 'y': [20, 14, 23, 25], 'type': 'line', 'name': 'Sales'},
                    {'x': ['Jan', 'Feb', 'Mar', 'Apr'], 'y': [16, 18, 18, 19], 'type': 'line', 'name': 'Costs'}
                ],
                'layout': {'title': 'Monthly Performance'}
            }
        )
    ]),
    
    # Right sidebar assistant
    dash_copilotkit_components.DashCopilotkitComponents(
        id='analytics-sidebar',
        ui_type='sidebar',
        public_api_key='your-copilotkit-cloud-api-key',
        position='right',
        instructions='''
        You are an analytics assistant for this dashboard.
        Help users:
        - Understand the data and trends shown in charts
        - Interpret metrics and KPIs
        - Find specific information
        - Analyze performance patterns
        ''',
        labels={
            'title': 'Analytics Assistant',
            'initial': 'Hello! I can help you analyze and understand your dashboard data. What insights are you looking for?'
        },
        width='350px'
    )
])

if __name__ == '__main__':
    app.run(debug=True)
```

### Left Sidebar Navigation Helper

```python
import dash
from dash import html, dcc
import dash_copilotkit_components

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Nav([
        html.A("Home", href="/", className="nav-link"),
        html.A("Products", href="/products", className="nav-link"),
        html.A("Services", href="/services", className="nav-link"),
        html.A("Contact", href="/contact", className="nav-link")
    ], className="navbar"),
    
    html.Main([
        html.H1("Welcome to Our Website"),
        html.P("Navigate through our site to explore our products and services."),
        dcc.Location(id='url'),
        html.Div(id='page-content')
    ]),
    
    # Left sidebar navigation helper
    dash_copilotkit_components.DashCopilotkitComponents(
        id='nav-sidebar',
        ui_type='sidebar',
        public_api_key='your-copilotkit-cloud-api-key',
        position='left',
        instructions='''
        You are a navigation assistant for this website.
        Help users:
        - Find specific pages or information
        - Understand what each section contains
        - Navigate to relevant content
        - Answer questions about our products and services
        ''',
        labels={
            'title': 'Navigation Helper',
            'initial': 'Hi! I can help you find what you\'re looking for on our website. Where would you like to go?'
        },
        width='300px'
    )
])

if __name__ == '__main__':
    app.run(debug=True)
```

## AI Textarea

### Simple Writing Assistant

```python
import dash
from dash import html, callback, Input, Output
import dash_copilotkit_components

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("AI Writing Assistant"),
    html.P("Start typing and get AI-powered writing suggestions."),
    
    dash_copilotkit_components.DashCopilotkitComponents(
        id='writing-textarea',
        ui_type='textarea',
        public_api_key='your-copilotkit-cloud-api-key',
        instructions='You are a helpful writing assistant. Help improve grammar, style, and clarity.',
        placeholder='Start writing here...',
        height='300px'
    ),
    
    html.Div(id='content-stats')
])

@callback(
    Output('content-stats', 'children'),
    Input('writing-textarea', 'value')
)
def show_stats(content):
    if not content:
        return html.P("Start typing to see statistics...")
    
    words = len(content.split())
    chars = len(content)
    
    return html.Div([
        html.P(f"Words: {words}"),
        html.P(f"Characters: {chars}"),
        html.P(f"Reading time: {max(1, words // 200)} minutes")
    ])

if __name__ == '__main__':
    app.run(debug=True)
```

### Email Composer

```python
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash_copilotkit_components

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Email Composer", className="mb-4"),
    
    dbc.Form([
        dbc.Row([
            dbc.Label("To:", width=1),
            dbc.Col([
                dbc.Input(id="email-to", type="email", placeholder="recipient@example.com")
            ], width=11)
        ], className="mb-3"),
        
        dbc.Row([
            dbc.Label("Subject:", width=1),
            dbc.Col([
                dbc.Input(id="email-subject", type="text", placeholder="Email subject")
            ], width=11)
        ], className="mb-3"),
        
        dbc.Row([
            dbc.Label("Message:", width=1),
            dbc.Col([
                dash_copilotkit_components.DashCopilotkitComponents(
                    id='email-body',
                    ui_type='textarea',
                    public_api_key='your-copilotkit-cloud-api-key',
                    instructions='''
                    You are an email writing assistant. Help users write:
                    - Professional and clear emails
                    - Appropriate tone for business communication
                    - Proper email structure and formatting
                    - Concise and effective messaging
                    ''',
                    placeholder='Compose your email here...',
                    height='250px'
                )
            ], width=11)
        ], className="mb-3"),
        
        dbc.Button("Send Email", id="send-btn", color="primary"),
        html.Div(id="send-result", className="mt-3")
    ])
])

@callback(
    Output('send-result', 'children'),
    Input('send-btn', 'n_clicks'),
    [State('email-to', 'value'),
     State('email-subject', 'value'),
     State('email-body', 'value')]
)
def send_email(n_clicks, to, subject, body):
    if not n_clicks:
        return ""
    
    if not all([to, subject, body]):
        return dbc.Alert("Please fill in all fields", color="warning")
    
    # In a real app, you would send the email here
    return dbc.Alert(f"Email sent to {to}!", color="success")

if __name__ == '__main__':
    app.run(debug=True)
```

## Multi-Component Example

### Content Creation Workflow

```python
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash_copilotkit_components

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Content Creation Workflow", className="mb-4"),
    
    dcc.Tabs(id="workflow-tabs", value="outline", children=[
        dcc.Tab(label="1. Outline", value="outline"),
        dcc.Tab(label="2. Draft", value="draft"),
        dcc.Tab(label="3. Review", value="review")
    ]),
    
    html.Div(id="tab-content", className="mt-4")
])

@callback(
    Output('tab-content', 'children'),
    Input('workflow-tabs', 'value')
)
def render_tab_content(active_tab):
    if active_tab == "outline":
        return html.Div([
            html.H3("Create Article Outline"),
            dash_copilotkit_components.DashCopilotkitComponents(
                id='outline-textarea',
                ui_type='textarea',
                public_api_key='your-copilotkit-cloud-api-key',
                instructions='''
                Help create well-structured article outlines with:
                - Clear main topics and subtopics
                - Logical flow and organization
                - Key points to cover in each section
                - Engaging introduction and conclusion ideas
                ''',
                placeholder='Create your article outline here...',
                height='400px'
            ),
            dbc.Button("Generate Draft", id="generate-draft-btn", color="primary", className="mt-3")
        ])
    
    elif active_tab == "draft":
        return html.Div([
            html.H3("Write Article Draft"),
            dash_copilotkit_components.DashCopilotkitComponents(
                id='draft-textarea',
                ui_type='textarea',
                public_api_key='your-copilotkit-cloud-api-key',
                instructions='''
                Help write engaging article content with:
                - Clear and compelling prose
                - Good paragraph structure
                - Smooth transitions between ideas
                - Engaging examples and explanations
                ''',
                placeholder='Your article draft will appear here...',
                height='400px'
            )
        ])
    
    elif active_tab == "review":
        return html.Div([
            html.H3("Review and Feedback"),
            dash_copilotkit_components.DashCopilotkitComponents(
                id='review-chat',
                ui_type='chat',
                public_api_key='your-copilotkit-cloud-api-key',
                instructions='''
                Provide constructive feedback on article drafts focusing on:
                - Content clarity and structure
                - Writing style and tone
                - Areas for improvement
                - Suggestions for enhancement
                ''',
                labels={
                    'title': 'Content Reviewer',
                    'initial': 'I can help review your article and provide feedback for improvement. Share your draft or ask specific questions!'
                },
                height='400px'
            )
        ])

if __name__ == '__main__':
    app.run(debug=True)
```

## Running the Examples

1. **Install Dependencies**:
   ```bash
   pip install dash dash-copilotkit-components
   ```

2. **Get API Key**:
   - Sign up at [CopilotKit Cloud](https://cloud.copilotkit.ai)
   - Get your public API key
   - Replace `'your-copilotkit-cloud-api-key'` in the examples

3. **Run the Example**:
   ```bash
   python your_example_file.py
   ```

4. **Open in Browser**:
   - Navigate to `http://127.0.0.1:8050`
   - Interact with the CopilotKit components

## Next Steps

- [Advanced Examples](advanced.md) - More complex integration patterns
- [Styling Examples](styling.md) - Custom styling and theming
- [Integration Examples](integration.md) - Integration with other libraries
