# Development Guide

Guide for contributing to Dash CopilotKit Components development.

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- Python 3.8+
- Git

### Development Setup

1. **Clone the repository:**

```bash
git clone https://github.com/dash-copilotkit/dash-copilitkit.git
cd dash-copilitkit
```

2. **Install Python dependencies:**

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

3. **Install Node.js dependencies:**

```bash
npm install
```

4. **Build the component:**

```bash
npm run build
```

## Project Structure

```
dash-copilotkit/
├── src/
│   └── lib/
│       ├── components/
│       │   └── DashCopilotkitComponents.react.js
│       └── fragments/
├── dash_copilotkit_components/
│   ├── __init__.py
│   └── DashCopilotkitComponents.py
├── tests/
├── docs/
├── examples/
├── package.json
├── requirements.txt
└── setup.py
```

### Key Files

- `src/lib/components/DashCopilotkitComponents.react.js` - Main React component
- `dash_copilotkit_components/DashCopilotkitComponents.py` - Python wrapper (auto-generated)
- `package.json` - Node.js dependencies and build scripts
- `setup.py` - Python package configuration

## Development Workflow

### Making Changes

1. **Create a feature branch:**

```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes:**
   - Edit React component in `src/lib/components/`
   - Update tests in `tests/`
   - Update documentation in `docs/`

3. **Build and test:**

```bash
# Build the component
npm run build

# Generate Python bindings
python -m dash.development.build_components ./src/lib/components dash_copilotkit_components --r-prefix ckc --jl-prefix ckc

# Run tests
npm test
python -m pytest tests/
```

4. **Test your changes:**

```bash
# Run example app
python app.py
```

### Component Development

#### React Component Structure

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { CopilotKit, CopilotPopup, CopilotSidebar, CopilotChat, CopilotTextarea } from '@copilotkit/react-ui';
import { CopilotKitProvider } from '@copilotkit/react-core';

const DashCopilotkitComponents = (props) => {
    const {
        id,
        ui_type,
        public_api_key,
        api_key,
        runtime_url,
        instructions,
        labels,
        placeholder,
        value,
        disabled,
        className,
        style,
        width,
        height,
        position,
        show_initially,
        setProps
    } = props;

    // Component logic here
    
    return (
        <div id={id} className={className} style={style}>
            <CopilotKitProvider 
                publicApiKey={public_api_key}
                runtimeUrl={runtime_url}
            >
                {renderUIComponent()}
            </CopilotKitProvider>
        </div>
    );
};

DashCopilotkitComponents.defaultProps = {
    ui_type: 'chat',
    instructions: 'You are a helpful AI assistant.',
    placeholder: 'Type your message here...',
    disabled: false,
    width: '100%',
    height: '400px',
    position: 'right',
    show_initially: false
};

DashCopilotkitComponents.propTypes = {
    id: PropTypes.string,
    ui_type: PropTypes.oneOf(['chat', 'popup', 'sidebar', 'textarea']),
    public_api_key: PropTypes.string,
    api_key: PropTypes.string,
    runtime_url: PropTypes.string,
    instructions: PropTypes.string,
    labels: PropTypes.object,
    placeholder: PropTypes.string,
    value: PropTypes.string,
    disabled: PropTypes.bool,
    className: PropTypes.string,
    style: PropTypes.object,
    width: PropTypes.string,
    height: PropTypes.string,
    position: PropTypes.oneOf(['left', 'right']),
    show_initially: PropTypes.bool,
    setProps: PropTypes.func
};

export default DashCopilotkitComponents;
```

#### Adding New Props

1. **Add prop to React component:**

```javascript
// In DashCopilotkitComponents.react.js
const { new_prop } = props;

// Add to propTypes
DashCopilotkitComponents.propTypes = {
    // ... existing props
    new_prop: PropTypes.string
};

// Add to defaultProps if needed
DashCopilotkitComponents.defaultProps = {
    // ... existing defaults
    new_prop: 'default_value'
};
```

2. **Rebuild component:**

```bash
npm run build
python -m dash.development.build_components ./src/lib/components dash_copilotkit_components --r-prefix ckc --jl-prefix ckc
```

3. **Update documentation:**

```markdown
### `new_prop`
- **Type**: `string`
- **Default**: `'default_value'`
- **Description**: Description of the new prop
```

### Testing

#### Unit Tests

```javascript
// tests/test_component.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import DashCopilotkitComponents from '../src/lib/components/DashCopilotkitComponents.react';

describe('DashCopilotkitComponents', () => {
    test('renders chat component', () => {
        render(
            <DashCopilotkitComponents
                id="test-chat"
                ui_type="chat"
                public_api_key="test-key"
            />
        );
        
        expect(screen.getByRole('main')).toBeInTheDocument();
    });
    
    test('handles prop changes', () => {
        const { rerender } = render(
            <DashCopilotkitComponents
                id="test-chat"
                ui_type="chat"
                public_api_key="test-key"
                disabled={false}
            />
        );
        
        rerender(
            <DashCopilotkitComponents
                id="test-chat"
                ui_type="chat"
                public_api_key="test-key"
                disabled={true}
            />
        );
        
        // Assert disabled state
    });
});
```

#### Integration Tests

```python
# tests/test_integration.py
import pytest
from dash import Dash, html
import dash_copilotkit_components

def test_component_integration():
    """Test component integration with Dash"""
    app = Dash(__name__)
    
    app.layout = html.Div([
        dash_copilotkit_components.DashCopilotkitComponents(
            id='test-component',
            ui_type='chat',
            public_api_key='test-key'
        )
    ])
    
    # Test that component renders without errors
    assert app.layout is not None

def test_component_props():
    """Test component prop validation"""
    component = dash_copilotkit_components.DashCopilotkitComponents(
        id='test-component',
        ui_type='chat',
        public_api_key='test-key',
        instructions='Test instructions',
        height='500px'
    )
    
    assert component.id == 'test-component'
    assert component.ui_type == 'chat'
    assert component.height == '500px'
```

### Code Quality

#### Linting and Formatting

```bash
# JavaScript
npm run lint
npm run format

# Python
black .
isort .
flake8 .
mypy dash_copilotkit_components/
```

#### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
```

## Build Process

### Development Build

```bash
# Watch mode for development
npm run build:dev

# Or build once
npm run build
```

### Production Build

```bash
# Build for production
npm run build:prod

# Generate Python bindings
python -m dash.development.build_components ./src/lib/components dash_copilotkit_components --r-prefix ckc --jl-prefix ckc
```

### Build Scripts

```json
{
  "scripts": {
    "build": "webpack --mode=production",
    "build:dev": "webpack --mode=development --watch",
    "build:prod": "webpack --mode=production --optimize-minimize",
    "test": "jest",
    "test:watch": "jest --watch",
    "lint": "eslint src/",
    "format": "prettier --write src/"
  }
}
```

## Documentation

### Writing Documentation

1. **API Documentation**: Update `docs/api/props.md` for new props
2. **Examples**: Add examples to `docs/examples/`
3. **Guides**: Update relevant guides in `docs/`

### Documentation Build

```bash
# Install MkDocs
pip install mkdocs mkdocs-material

# Serve documentation locally
mkdocs serve

# Build documentation
mkdocs build
```

## Release Process

### Version Management

1. **Update version numbers:**

```bash
# Update package.json
npm version patch  # or minor, major

# Update setup.py
# Update __init__.py
```

2. **Create changelog entry:**

```markdown
## [1.2.3] - 2024-01-15

### Added
- New feature X
- New prop Y

### Changed
- Improved performance of Z

### Fixed
- Fixed bug in component A
```

3. **Build and test:**

```bash
npm run build:prod
python -m pytest tests/
```

4. **Create release:**

```bash
git add .
git commit -m "Release v1.2.3"
git tag v1.2.3
git push origin main --tags
```

## Debugging

### Development Tools

```javascript
// Enable React DevTools
if (process.env.NODE_ENV === 'development') {
    // Development-only code
    console.log('Development mode enabled');
}
```

### Common Issues

1. **Build failures**: Check Node.js and Python versions
2. **Import errors**: Verify component registration
3. **Prop validation**: Check PropTypes definitions
4. **Styling issues**: Verify CSS imports and class names

### Debug Mode

```python
# Enable debug mode in Dash
app = Dash(__name__, debug=True)

# Enable component debugging
import os
os.environ['DASH_DEBUG'] = 'true'
```

## Contributing Guidelines

### Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Update documentation
6. Submit a pull request

### Code Review

- All changes require code review
- Tests must pass
- Documentation must be updated
- Follow coding standards

### Issue Reporting

When reporting issues, include:
- Dash version
- Component version
- Browser information
- Minimal reproduction example
- Error messages and stack traces

## Next Steps

- [Building Components](building.md) - Advanced component building
- [Testing Guide](testing.md) - Comprehensive testing strategies
- [API Reference](../api/props.md) - Complete API documentation
