# Dash CopilotKit Components

[![PyPI version](https://badge.fury.io/py/dash-copilotkit-components.svg)](https://badge.fury.io/py/dash-copilotkit-components)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Dash 2.0+](https://img.shields.io/badge/dash-2.0+-green.svg)](https://dash.plotly.com/)

A comprehensive Dash component library for integrating CopilotKit AI assistants into your Dash applications. This component supports all 4 CopilotKit UI types and is compatible with Dash 3.0.

## 🚀 Features

- **4 UI Types**: Chat, Popup, Sidebar, and AI-powered Textarea interfaces
- **Flexible API Configuration**: Use CopilotKit Cloud or bring your own API key (OpenAI, Anthropic, etc.)
- **Dash 3.0 Compatible**: Updated for the latest Dash version with modern React 18 support
- **Fully Customizable**: Complete control over styling, instructions, and behavior
- **Production Ready**: Comprehensive error handling and performance optimizations
- **TypeScript Support**: Complete type definitions for all props

## 📦 Installation

Install from PyPI:
```bash
pip install dash-copilotkit-components
```

The component automatically includes all required JavaScript dependencies.

## Quick Start

```python
import dash_copilotkit_components
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    dash_copilotkit_components.DashCopilotkitComponents(
        id='copilot',
        ui_type='chat',  # 'chat', 'popup', 'sidebar', or 'textarea'
        public_api_key='your-copilotkit-cloud-api-key',  # Optional
        instructions="You are a helpful AI assistant.",
        labels={
            'title': 'AI Assistant',
            'initial': 'Hello! How can I help you today?'
        }
    )
])

if __name__ == '__main__':
    app.run(debug=True)
```

## UI Types

### 1. Chat Interface (`ui_type='chat'`)
A full chat interface embedded directly in your app.

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='chat-copilot',
    ui_type='chat',
    width='100%',
    height='500px',
    public_api_key='your-api-key'
)
```

### 2. Popup Chat (`ui_type='popup'`)
A popup chat window that can be toggled on/off.

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='popup-copilot',
    ui_type='popup',
    show_initially=False,
    public_api_key='your-api-key'
)
```

### 3. Sidebar Chat (`ui_type='sidebar'`)
A sidebar chat interface that slides in from the side.

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='sidebar-copilot',
    ui_type='sidebar',
    position='right',  # 'left' or 'right'
    show_initially=False,
    public_api_key='your-api-key'
)
```

### 4. AI Textarea (`ui_type='textarea'`)
An AI-powered textarea that helps users write better content.

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='textarea-copilot',
    ui_type='textarea',
    placeholder='Start typing here...',
    value='',
    public_api_key='your-api-key'
)
```

## API Configuration

### Option 1: CopilotKit Cloud (Recommended)
Get your API key from [CopilotKit Cloud](https://cloud.copilotkit.ai):

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='copilot',
    ui_type='chat',
    public_api_key='your-copilotkit-cloud-api-key'
)
```

### Option 2: Bring Your Own Key
Use your own runtime URL with your API key:

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='copilot',
    ui_type='chat',
    runtime_url='http://localhost:3000/api/copilotkit',
    api_key='your-openai-api-key'
)
```

## Component Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `id` | string | - | Component ID for Dash callbacks |
| `ui_type` | string | 'chat' | UI type: 'chat', 'popup', 'sidebar', 'textarea' |
| `api_key` | string | - | Your API key (for bring your own key) |
| `runtime_url` | string | - | Runtime URL for your backend |
| `public_api_key` | string | - | CopilotKit Cloud public API key |
| `instructions` | string | "You are a helpful AI assistant." | Custom instructions for the AI |
| `labels` | object | - | Labels configuration with 'title' and 'initial' |
| `placeholder` | string | "Type your message here..." | Placeholder for textarea mode |
| `value` | string | - | Current value (for textarea mode) |
| `disabled` | boolean | false | Whether the component is disabled |
| `className` | string | - | CSS class name |
| `style` | object | - | Inline styles |
| `width` | string | '100%' | Component width |
| `height` | string | '400px' | Component height |
| `position` | string | 'right' | Sidebar position ('left' or 'right') |
| `show_initially` | boolean | false | Show popup/sidebar initially |

## Examples

See the `usage.py` file for a comprehensive example that demonstrates all UI types with configuration options.

Run the example:
```bash
python usage.py
```

Then visit http://localhost:8050 to see the component in action.

## Development

### Setup Development Environment

1. Clone the repository:
```bash
git clone <repository-url>
cd dash-copilotkit-components
```

2. Install dependencies:
```bash
npm install
pip install -r requirements.txt
```

3. Build the component:
```bash
npm run build
```

4. Generate Python bindings:
```bash
python -c "import dash.development.component_generator as cg; cg.generate_components('./src/lib/components', 'dash_copilotkit_components', rprefix='ckc', jlprefix='ckc')"
```

### Testing

Run the test suite:
```bash
pytest tests/
```

### Building for Production

1. Build JavaScript:
```bash
npm run build:js
```

2. Generate Python components:
```bash
npm run build:backends
```

3. Create distribution:
```bash
python setup.py sdist bdist_wheel
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

- [CopilotKit Documentation](https://docs.copilotkit.ai/)
- [Dash Documentation](https://dash.plotly.com/)
- [GitHub Issues](https://github.com/your-repo/dash-copilotkit-components/issues)
