# Styling Examples

Examples of custom styling and theming for Dash CopilotKit Components.

## Basic Styling

### Custom Colors and Borders

```python
import dash
from dash import html
import dash_copilotkit_components

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Custom Styled Chat"),
    
    dash_copilotkit_components.DashCopilotkitComponents(
        id='custom-styled-chat',
        ui_type='chat',
        public_api_key='your-copilotkit-cloud-api-key',
        className='custom-chat',
        style={
            'border': '3px solid #007bff',
            'borderRadius': '15px',
            'boxShadow': '0 8px 25px rgba(0, 123, 255, 0.2)',
            'background': 'linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)'
        },
        height='500px'
    )
])

# Add custom CSS
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            .custom-chat {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
                transition: all 0.3s ease;
            }
            
            .custom-chat:hover {
                transform: translateY(-2px);
                box-shadow: 0 12px 35px rgba(0, 123, 255, 0.3) !important;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
```

## Theme Examples

### Dark Theme

```python
import dash
from dash import html
import dash_bootstrap_components as dbc
import dash_copilotkit_components

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1("Dark Theme Example", style={'color': 'white'}),
    
    dash_copilotkit_components.DashCopilotkitComponents(
        id='dark-theme-chat',
        ui_type='chat',
        public_api_key='your-copilotkit-cloud-api-key',
        className='dark-theme-chat',
        height='500px'
    )
], style={'backgroundColor': '#1a1a1a', 'minHeight': '100vh', 'padding': '20px'})

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            :root {
                --dark-bg: #2d3748;
                --dark-surface: #4a5568;
                --dark-text: #e2e8f0;
                --dark-border: #718096;
                --dark-accent: #63b3ed;
            }
            
            .dark-theme-chat {
                background-color: var(--dark-bg);
                border: 2px solid var(--dark-border);
                border-radius: 12px;
                color: var(--dark-text);
            }
            
            .dark-theme-chat * {
                color: var(--dark-text);
            }
            
            .dark-theme-chat input,
            .dark-theme-chat textarea {
                background-color: var(--dark-surface);
                border-color: var(--dark-border);
                color: var(--dark-text);
            }
            
            .dark-theme-chat button {
                background-color: var(--dark-accent);
                border-color: var(--dark-accent);
                color: white;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
```

### Corporate Theme

```python
import dash
from dash import html
import dash_bootstrap_components as dbc
import dash_copilotkit_components

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Corporate Assistant", className="corporate-title"),
            html.P("Professional AI assistance for your business needs.", 
                   className="corporate-subtitle"),
            
            dash_copilotkit_components.DashCopilotkitComponents(
                id='corporate-chat',
                ui_type='chat',
                public_api_key='your-copilotkit-cloud-api-key',
                className='corporate-chat',
                instructions='You are a professional business assistant.',
                labels={
                    'title': 'Business Assistant',
                    'initial': 'Good day! How may I assist you with your business needs?'
                },
                height='600px'
            )
        ], md=8, className='mx-auto')
    ])
], fluid=True, className='corporate-container')

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
            
            :root {
                --corporate-primary: #003366;
                --corporate-secondary: #0066cc;
                --corporate-accent: #f0f8ff;
                --corporate-text: #333333;
                --corporate-border: #cccccc;
            }
            
            .corporate-container {
                background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                min-height: 100vh;
                padding: 40px 0;
                font-family: 'Roboto', sans-serif;
            }
            
            .corporate-title {
                color: var(--corporate-primary);
                font-weight: 700;
                text-align: center;
                margin-bottom: 10px;
            }
            
            .corporate-subtitle {
                color: var(--corporate-text);
                text-align: center;
                margin-bottom: 30px;
                font-weight: 300;
            }
            
            .corporate-chat {
                background: white;
                border: 1px solid var(--corporate-border);
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0, 51, 102, 0.1);
                font-family: 'Roboto', sans-serif;
            }
            
            .corporate-chat .chat-header {
                background: var(--corporate-primary);
                color: white;
                padding: 20px;
                border-radius: 8px 8px 0 0;
                font-weight: 500;
            }
            
            .corporate-chat .chat-input {
                border-top: 1px solid var(--corporate-border);
                background: var(--corporate-accent);
            }
            
            .corporate-chat button {
                background-color: var(--corporate-secondary);
                border-color: var(--corporate-secondary);
                font-weight: 500;
                transition: all 0.2s ease;
            }
            
            .corporate-chat button:hover {
                background-color: var(--corporate-primary);
                border-color: var(--corporate-primary);
                transform: translateY(-1px);
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
```

## Responsive Design Examples

### Mobile-First Popup

```python
import dash
from dash import html
import dash_copilotkit_components

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Mobile-Responsive Popup"),
    html.P("This popup adapts to different screen sizes."),
    
    dash_copilotkit_components.DashCopilotkitComponents(
        id='responsive-popup',
        ui_type='popup',
        public_api_key='your-copilotkit-cloud-api-key',
        className='responsive-popup'
    )
])

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            .responsive-popup {
                /* Mobile styles (default) */
                position: fixed;
                bottom: 10px;
                right: 10px;
                left: 10px;
                width: auto;
                max-height: 70vh;
                border-radius: 12px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            }
            
            /* Tablet styles */
            @media (min-width: 768px) {
                .responsive-popup {
                    left: auto;
                    width: 400px;
                    bottom: 20px;
                    right: 20px;
                    max-height: 500px;
                }
            }
            
            /* Desktop styles */
            @media (min-width: 1024px) {
                .responsive-popup {
                    width: 450px;
                    bottom: 30px;
                    right: 30px;
                    max-height: 600px;
                }
            }
            
            /* Large desktop */
            @media (min-width: 1440px) {
                .responsive-popup {
                    width: 500px;
                    bottom: 40px;
                    right: 40px;
                }
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
```

## Animation Examples

### Animated Sidebar

```python
import dash
from dash import html
import dash_copilotkit_components

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Animated Sidebar Example"),
    html.P("Click the sidebar trigger to see smooth animations."),
    
    dash_copilotkit_components.DashCopilotkitComponents(
        id='animated-sidebar',
        ui_type='sidebar',
        public_api_key='your-copilotkit-cloud-api-key',
        position='right',
        className='animated-sidebar',
        width='350px'
    )
])

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            .animated-sidebar {
                transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                box-shadow: -8px 0 32px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(10px);
                background: rgba(255, 255, 255, 0.95);
            }
            
            .animated-sidebar.opening {
                animation: slideInRight 0.4s ease-out;
            }
            
            .animated-sidebar.closing {
                animation: slideOutRight 0.4s ease-in;
            }
            
            @keyframes slideInRight {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
            
            @keyframes slideOutRight {
                from {
                    transform: translateX(0);
                    opacity: 1;
                }
                to {
                    transform: translateX(100%);
                    opacity: 0;
                }
            }
            
            /* Backdrop animation */
            .sidebar-backdrop {
                background: rgba(0, 0, 0, 0.5);
                backdrop-filter: blur(4px);
                transition: all 0.4s ease;
            }
            
            .sidebar-backdrop.entering {
                animation: fadeIn 0.4s ease-out;
            }
            
            .sidebar-backdrop.exiting {
                animation: fadeOut 0.4s ease-in;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            
            @keyframes fadeOut {
                from { opacity: 1; }
                to { opacity: 0; }
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
```

## Custom Component Styling

### Glassmorphism Effect

```python
import dash
from dash import html
import dash_copilotkit_components

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Glassmorphism Chat", style={'color': 'white', 'textAlign': 'center'}),
    
    dash_copilotkit_components.DashCopilotkitComponents(
        id='glass-chat',
        ui_type='chat',
        public_api_key='your-copilotkit-cloud-api-key',
        className='glass-chat',
        height='500px'
    )
], className='glass-background')

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            .glass-background {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 40px 20px;
                position: relative;
            }
            
            .glass-background::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="2" fill="rgba(255,255,255,0.1)"/><circle cx="80" cy="40" r="3" fill="rgba(255,255,255,0.1)"/><circle cx="40" cy="80" r="1" fill="rgba(255,255,255,0.1)"/></svg>');
                pointer-events: none;
            }
            
            .glass-chat {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
                max-width: 800px;
                margin: 0 auto;
                position: relative;
                overflow: hidden;
            }
            
            .glass-chat::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 1px;
                background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            }
            
            .glass-chat * {
                color: white;
            }
            
            .glass-chat input,
            .glass-chat textarea {
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 12px;
                color: white;
                backdrop-filter: blur(10px);
            }
            
            .glass-chat input::placeholder,
            .glass-chat textarea::placeholder {
                color: rgba(255, 255, 255, 0.7);
            }
            
            .glass-chat button {
                background: rgba(255, 255, 255, 0.2);
                border: 1px solid rgba(255, 255, 255, 0.3);
                border-radius: 12px;
                color: white;
                backdrop-filter: blur(10px);
                transition: all 0.3s ease;
            }
            
            .glass-chat button:hover {
                background: rgba(255, 255, 255, 0.3);
                transform: translateY(-2px);
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
```

## CSS Framework Integration

### Tailwind CSS Example

```python
import dash
from dash import html
import dash_copilotkit_components

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Tailwind Styled Components", 
            className="text-4xl font-bold text-center text-gray-800 mb-8"),
    
    html.Div([
        dash_copilotkit_components.DashCopilotkitComponents(
            id='tailwind-chat',
            ui_type='chat',
            public_api_key='your-copilotkit-cloud-api-key',
            className='tailwind-chat',
            height='500px'
        )
    ], className="max-w-4xl mx-auto")
], className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4")

# Include Tailwind CSS
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        <script src="https://cdn.tailwindcss.com"></script>
        {%css%}
        <style>
            .tailwind-chat {
                @apply bg-white rounded-2xl shadow-2xl border border-gray-200;
                @apply hover:shadow-3xl transition-all duration-300;
            }
            
            .tailwind-chat .chat-header {
                @apply bg-gradient-to-r from-blue-600 to-indigo-600;
                @apply text-white font-semibold p-6 rounded-t-2xl;
            }
            
            .tailwind-chat .chat-messages {
                @apply p-6 max-h-96 overflow-y-auto;
            }
            
            .tailwind-chat .chat-input {
                @apply border-t border-gray-200 p-6 bg-gray-50 rounded-b-2xl;
            }
            
            .tailwind-chat input,
            .tailwind-chat textarea {
                @apply w-full p-3 border border-gray-300 rounded-lg;
                @apply focus:ring-2 focus:ring-blue-500 focus:border-transparent;
                @apply transition-all duration-200;
            }
            
            .tailwind-chat button {
                @apply bg-blue-600 hover:bg-blue-700 text-white font-medium;
                @apply px-6 py-3 rounded-lg transition-all duration-200;
                @apply hover:transform hover:scale-105 hover:shadow-lg;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
```

## Next Steps

- [Integration Examples](integration.md) - External service integration
- [Advanced Examples](advanced.md) - Complex use cases
- [API Reference](../api/styling.md) - Complete styling documentation
