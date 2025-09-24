# Installation

## Requirements

- Python 3.8 or higher
- Dash 3.0 or higher
- Node.js 16+ (for development)

## Install from PyPI

The easiest way to install Dash CopilotKit Components is using pip:

```bash
pip install dash-copilotkit-components
```

## Install from Source

For development or to get the latest features:

```bash
git clone https://github.com/dash-copilotkit/dash-copilitkit.git
cd dash-copilitkit
pip install -e .
```

## Dependencies

The package automatically installs the following dependencies:

- `dash>=3.0.0` - The main Dash framework
- `dash-bootstrap-components` - For modern UI components (optional but recommended)

## Verify Installation

Create a simple test file to verify the installation:

```python
# test_installation.py
import dash_copilotkit_components
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Installation Test"),
    dash_copilotkit_components.DashCopilotkitComponents(
        id='test-copilot',
        ui_type='chat',
        instructions='You are a test assistant.'
    )
])

if __name__ == '__main__':
    app.run(debug=True)
```

Run the test:

```bash
python test_installation.py
```

If you see the Dash app running at `http://127.0.0.1:8050/`, the installation was successful!

## Next Steps

- [Quick Start Guide](quick-start.md) - Get up and running in minutes
- [Configuration](configuration.md) - Learn about API keys and settings
- [UI Types](../ui-types/chat.md) - Explore different interface options
