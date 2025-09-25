# Demo App Separation Guide

This document outlines the steps needed to separate the demo application from the core component package before uploading to PyPI.

## Overview

Currently, the repository contains both:
1. **Core Component Package** - The actual `dash_copilotkit_components` package for PyPI
2. **Demo Application** - The multi-page Dash app showcasing the component (`app.py`, `pages/`, `assets/`)

For PyPI distribution, we need to separate these concerns to keep the package clean and focused.

## Current Structure

```
dash_copilotkit_components/
├── dash_copilotkit_components/          # Core package (KEEP)
│   ├── __init__.py
│   ├── DashCopilotkitComponents.py
│   └── ...
├── src/                                 # React source (KEEP)
│   └── lib/
├── app.py                              # Demo app (MOVE)
├── pages/                              # Demo pages (MOVE)
├── assets/                             # Demo assets (MOVE)
├── docs/                               # Documentation (KEEP)
├── tests/                              # Tests (KEEP)
├── package.json                        # Build config (KEEP)
├── setup.py                           # PyPI config (KEEP)
├── README.md                          # Package docs (KEEP)
└── ...
```

## Recommended New Structure

### Option 1: Separate Repository (Recommended)

Create a new repository for the demo app:

```
dash-copilotkit-components/             # Main package repo
├── dash_copilotkit_components/
├── src/
├── docs/
├── tests/
├── setup.py
├── README.md
└── ...

dash-copilotkit-demo/                   # New demo repo
├── app.py
├── pages/
├── assets/
├── requirements.txt
├── README.md
└── ...
```

### Option 2: Subdirectory Structure

Keep everything in one repo but organize better:

```
dash-copilotkit-components/
├── dash_copilotkit_components/          # Core package
├── src/                                 # React source
├── docs/                               # Documentation
├── tests/                              # Tests
├── demo/                               # Demo application
│   ├── app.py
│   ├── pages/
│   ├── assets/
│   ├── requirements.txt
│   └── README.md
├── examples/                           # Simple examples
│   ├── basic_chat.py
│   ├── textarea_example.py
│   └── ...
├── setup.py
├── README.md
└── ...
```

## Step-by-Step Separation Process

### Step 1: Create Demo Directory Structure

```bash
# Create demo directory
mkdir demo
mkdir demo/assets
mkdir demo/assets/css
mkdir demo/assets/js
mkdir demo/assets/img

# Create examples directory
mkdir examples
```

### Step 2: Move Demo Files

```bash
# Move main demo app
mv app.py demo/

# Move demo pages
mv pages/ demo/

# Move demo assets
mv assets/* demo/assets/

# Remove empty assets directory
rmdir assets
```

### Step 3: Create Demo Requirements

Create `demo/requirements.txt`:
```txt
dash>=2.0.0
dash-bootstrap-components>=1.0.0
dash-copilotkit-components>=1.0.0
plotly>=5.0.0
```

### Step 4: Create Demo README

Create `demo/README.md`:
```markdown
# Dash CopilotKit Components Demo

This is a comprehensive demo application showcasing all features of the Dash CopilotKit Components package.

## Installation

1. Install the component package:
```bash
pip install dash-copilotkit-components
```

2. Install demo dependencies:
```bash
pip install -r requirements.txt
```

## Running the Demo

```bash
python app.py
```

Visit http://localhost:8050 to see the demo.

## Features Demonstrated

- Chat Interface
- Popup Chat
- Sidebar Chat  
- AI Textarea
- Configuration options
- Styling examples
- Integration patterns
```

### Step 5: Update Demo App Imports

Update `demo/app.py` to use the installed package:

```python
# Change from relative import
# import dash_copilotkit_components

# To absolute import (assuming package is installed)
import dash_copilotkit_components
```

### Step 6: Create Simple Examples

Create `examples/basic_chat.py`:
```python
import dash_copilotkit_components
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Basic Chat Example"),
    dash_copilotkit_components.DashCopilotkitComponents(
        id='basic-chat',
        ui_type='chat',
        public_api_key='your-api-key-here',
        instructions='You are a helpful assistant.'
    )
])

if __name__ == '__main__':
    app.run(debug=True)
```

Create `examples/textarea_example.py`:
```python
import dash_copilotkit_components
from dash import Dash, html, Input, Output, callback

app = Dash(__name__)

app.layout = html.Div([
    html.H1("AI Textarea Example"),
    dash_copilotkit_components.DashCopilotkitComponents(
        id='ai-textarea',
        ui_type='textarea',
        public_api_key='your-api-key-here',
        placeholder='Start writing...',
        height='200px'
    ),
    html.Div(id='output')
])

@callback(
    Output('output', 'children'),
    Input('ai-textarea', 'value')
)
def display_content(value):
    return f"Content: {value or 'No content yet...'}"

if __name__ == '__main__':
    app.run(debug=True)
```

### Step 7: Update Main README

Update the main `README.md` to focus on the package:

```markdown
# Dash CopilotKit Components

[![PyPI version](https://badge.fury.io/py/dash-copilotkit-components.svg)](https://badge.fury.io/py/dash-copilotkit-components)

AI-powered chat interfaces for Dash applications using CopilotKit.

## Quick Start

```python
import dash_copilotkit_components
from dash import Dash, html

app = Dash(__name__)
app.layout = html.Div([
    dash_copilotkit_components.DashCopilotkitComponents(
        id='copilot',
        ui_type='chat',
        public_api_key='your-api-key'
    )
])

if __name__ == '__main__':
    app.run(debug=True)
```

## Examples

See the `examples/` directory for simple usage examples.

## Demo Application

A comprehensive demo showcasing all features is available in the `demo/` directory.

## Documentation

Full documentation is available at: https://dash-copilotkit.biyani.xyz
```

### Step 8: Update Package Configuration

Update `setup.py` to exclude demo files:

```python
setup(
    # ... existing config ...
    packages=[package_name],
    package_data={
        package_name: [
            "*.js",
            "*.js.map",
            "*.json",
            "*.css"
        ]
    },
    exclude_package_data={
        '': ['demo/*', 'examples/*']
    },
    # ... rest of config ...
)
```

### Step 9: Update .gitignore

Add to `.gitignore`:
```
# Demo app specific
demo/__pycache__/
demo/*.pyc

# Examples
examples/__pycache__/
examples/*.pyc
```

### Step 10: Update Documentation

Update `mkdocs.yml` to reference the new structure:

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - Installation: getting-started/installation.md
    - Quick Start: getting-started/quick-start.md
  - Examples:
    - Basic Usage: examples/basic.md
    - Demo Application: examples/demo.md
  # ... rest of nav
```

## Testing the Separation

### Test Package Installation

1. Build the package:
```bash
python setup.py sdist bdist_wheel
```

2. Install in a clean environment:
```bash
pip install dist/dash_copilotkit_components-1.0.0.tar.gz
```

3. Test basic import:
```python
import dash_copilotkit_components
print(dash_copilotkit_components.__version__)
```

### Test Demo App

1. Navigate to demo directory:
```bash
cd demo
```

2. Install demo requirements:
```bash
pip install -r requirements.txt
```

3. Run demo:
```bash
python app.py
```

### Test Examples

1. Navigate to examples:
```bash
cd examples
```

2. Run basic example:
```bash
python basic_chat.py
```

## Benefits of Separation

1. **Cleaner Package**: PyPI package only contains essential files
2. **Smaller Download**: Users don't download demo assets they don't need
3. **Better Organization**: Clear separation of concerns
4. **Easier Maintenance**: Demo and package can evolve independently
5. **Professional Appearance**: Package looks more professional on PyPI

## Deployment Considerations

### PyPI Package
- Only includes core component files
- Minimal dependencies
- Clean, focused README
- Professional metadata

### Demo Deployment
- Can be deployed separately (e.g., Heroku, Railway)
- Showcases all features
- Includes comprehensive examples
- Links back to PyPI package

### Documentation
- Remains comprehensive
- Links to both package and demo
- Includes migration guide if needed

## Migration Script

Create `migrate_demo.py` to automate the separation:

```python
#!/usr/bin/env python3
"""
Script to migrate demo files to separate directory structure.
"""
import os
import shutil
from pathlib import Path

def migrate_demo():
    """Migrate demo files to new structure."""
    # Create directories
    Path("demo").mkdir(exist_ok=True)
    Path("demo/assets").mkdir(exist_ok=True)
    Path("examples").mkdir(exist_ok=True)
    
    # Move files
    if Path("app.py").exists():
        shutil.move("app.py", "demo/app.py")
    
    if Path("pages").exists():
        shutil.move("pages", "demo/pages")
    
    if Path("assets").exists():
        shutil.move("assets", "demo/assets")
    
    print("Demo migration completed!")

if __name__ == "__main__":
    migrate_demo()
```

Run with:
```bash
python migrate_demo.py
```

This separation will result in a clean, professional PyPI package while maintaining a comprehensive demo application for showcasing features.
