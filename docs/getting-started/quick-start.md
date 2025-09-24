# Quick Start

Get up and running with Dash CopilotKit Components in just a few minutes!

## 1. Get Your API Key

### Option A: CopilotKit Cloud (Recommended)

1. Visit [CopilotKit Cloud](https://cloud.copilotkit.ai)
2. Sign up for a free account
3. Create a new project
4. Copy your public API key

### Option B: Bring Your Own Key

If you prefer to use your own OpenAI API key:

1. Get an API key from [OpenAI](https://platform.openai.com/api-keys)
2. Set up a CopilotKit runtime server (see [CopilotKit docs](https://docs.copilotkit.ai))

## 2. Create Your First App

Create a new Python file called `my_copilot_app.py`:

```python
import dash_copilotkit_components
from dash import Dash, html

# Initialize the Dash app
app = Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("My AI Assistant", style={'textAlign': 'center'}),
    
    # Add the CopilotKit component
    dash_copilotkit_components.DashCopilotkitComponents(
        id='my-copilot',
        ui_type='chat',  # Choose: 'chat', 'popup', 'sidebar', 'textarea'
        public_api_key='your-copilotkit-cloud-api-key',  # Replace with your key
        instructions='You are a helpful AI assistant for my Dash application.',
        labels={
            'title': 'AI Assistant',
            'initial': 'Hello! How can I help you today?'
        },
        height='500px'
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

## 3. Run Your App

```bash
python my_copilot_app.py
```

Open your browser and go to `http://127.0.0.1:8050/` to see your AI-powered Dash app!

## 4. Try Different UI Types

### Chat Interface
```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='chat-copilot',
    ui_type='chat',
    public_api_key='your-api-key',
    height='500px'
)
```

### Popup Chat
```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='popup-copilot',
    ui_type='popup',
    public_api_key='your-api-key',
    show_initially=False
)
```

### Sidebar Chat
```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='sidebar-copilot',
    ui_type='sidebar',
    public_api_key='your-api-key',
    position='right'
)
```

### AI Textarea
```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='textarea-copilot',
    ui_type='textarea',
    public_api_key='your-api-key',
    placeholder='Start typing here...'
)
```

## 5. Add Callbacks (Optional)

You can interact with the component using Dash callbacks:

```python
from dash import callback, Input, Output

@callback(
    Output('output-div', 'children'),
    Input('my-copilot', 'value')
)
def display_output(value):
    if value:
        return f"AI Textarea content: {value}"
    return "No content yet..."
```

## What's Next?

- **[Configuration](configuration.md)** - Learn about all available options
- **[UI Types](../ui-types/chat.md)** - Detailed guide for each interface
- **[Examples](../examples/basic.md)** - More code examples and use cases
- **[API Reference](../api/props.md)** - Complete component documentation

## Need Help?

- 📖 [Full Documentation](../index.md)
- 🐛 [Report Issues](https://github.com/dash-copilotkit/dash-copilitkit/issues)
- 💬 [Join Discussions](https://github.com/dash-copilotkit/dash-copilitkit/discussions)
