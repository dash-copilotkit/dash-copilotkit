# Dash CopilotKit Components

<div align="center">
  <img src="assets/logo.png" alt="Dash CopilotKit Components" width="200"/>
  
  **AI-powered chat interfaces for Dash applications**
  
  [![PyPI version](https://badge.fury.io/py/dash-copilotkit-components.svg)](https://badge.fury.io/py/dash-copilotkit-components)
  [![GitHub stars](https://img.shields.io/github/stars/dash-copilotkit/dash-copilitkit.svg)](https://github.com/dash-copilotkit/dash-copilitkit/stargazers)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
</div>

## Overview

Dash CopilotKit Components is a comprehensive library that brings powerful AI chat interfaces to your Dash applications. Built on top of [CopilotKit](https://copilotkit.ai), it provides four different UI types to seamlessly integrate conversational AI into your web applications.

## ✨ Features

- **🎯 4 UI Types**: Chat, Popup, Sidebar, and Textarea interfaces
- **🔧 Flexible Configuration**: Use CopilotKit Cloud or bring your own API key
- **⚡ Dash 3.0 Compatible**: Built for the latest Dash version
- **🎨 Customizable**: Full control over styling, instructions, and behavior
- **📱 Responsive**: Works perfectly on desktop and mobile devices
- **🔒 Secure**: Built-in security best practices

## 🚀 Quick Start

### Installation

```bash
pip install dash-copilotkit-components
```

### Basic Usage

```python
import dash_copilotkit_components
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    dash_copilotkit_components.DashCopilotkitComponents(
        id='copilot',
        ui_type='chat',
        public_api_key='your-copilotkit-cloud-api-key',
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

## 🎨 UI Types

### Chat Interface
A full-featured chat interface embedded directly in your application.

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='chat-copilot',
    ui_type='chat',
    height='500px',
    public_api_key='your-api-key'
)
```

### Popup Chat
A toggleable popup chat window that doesn't interfere with your UI.

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='popup-copilot',
    ui_type='popup',
    show_initially=False,
    public_api_key='your-api-key'
)
```

### Sidebar Chat
A slide-in sidebar chat that can be positioned left or right.

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='sidebar-copilot',
    ui_type='sidebar',
    position='right',
    public_api_key='your-api-key'
)
```

### AI Textarea
An AI-powered textarea that helps users write better content.

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='textarea-copilot',
    ui_type='textarea',
    placeholder='Start typing here...',
    public_api_key='your-api-key'
)
```

## 🔑 API Configuration

### Option 1: CopilotKit Cloud (Recommended)

Get your free API key from [CopilotKit Cloud](https://cloud.copilotkit.ai):

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

## 📚 Documentation

- **[Getting Started](getting-started/installation.md)** - Installation and setup
- **[UI Types](ui-types/chat.md)** - Detailed guide for each interface type
- **[API Reference](api/props.md)** - Complete component documentation
- **[Examples](examples/basic.md)** - Code examples and use cases
- **[Deployment](deployment/production.md)** - Production deployment guide

## 🎯 Use Cases

- **Customer Support**: Add AI-powered help to your applications
- **Content Creation**: Assist users with writing and editing
- **Data Analysis**: Provide AI insights and explanations
- **Form Assistance**: Guide users through complex forms
- **Interactive Tutorials**: Create AI-powered learning experiences

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](contributing/development.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/dash-copilotkit/dash-copilitkit/blob/main/LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Dash](https://dash.plotly.com/) by Plotly
- Powered by [CopilotKit](https://copilotkit.ai)
- UI components from [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)

## 📞 Support

- 📖 [Documentation](https://dash-copilotkit.biyani.xyz)
- 🐛 [Issues](https://github.com/dash-copilotkit/dash-copilitkit/issues)
- 💬 [Discussions](https://github.com/dash-copilotkit/dash-copilitkit/discussions)
- 🌟 [GitHub](https://github.com/dash-copilotkit/dash-copilitkit)
