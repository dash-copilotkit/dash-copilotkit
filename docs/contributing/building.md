# Building Components

Advanced guide for building and customizing Dash CopilotKit Components.

## Build System Overview

The build system uses Webpack to bundle React components and generate Python bindings automatically.

### Build Configuration

```javascript
// webpack.config.js
const path = require('path');
const packagejson = require('./package.json');

const dashLibraryName = packagejson.name.replace(/-/g, '_');

module.exports = (env, argv) => {
    const mode = argv.mode || 'development';
    
    return {
        mode: mode,
        entry: {
            main: './src/lib/index.js'
        },
        output: {
            path: path.resolve(__dirname, dashLibraryName),
            filename: `${dashLibraryName}.js`,
            library: dashLibraryName,
            libraryTarget: 'window'
        },
        externals: {
            'react': 'React',
            'react-dom': 'ReactDOM',
            'plotly.js': 'Plotly'
        },
        module: {
            rules: [
                {
                    test: /\.jsx?$/,
                    exclude: /node_modules/,
                    use: {
                        loader: 'babel-loader',
                        options: {
                            presets: ['@babel/preset-env', '@babel/preset-react']
                        }
                    }
                },
                {
                    test: /\.css$/,
                    use: ['style-loader', 'css-loader']
                }
            ]
        },
        resolve: {
            extensions: ['.js', '.jsx']
        }
    };
};
```

### Babel Configuration

```json
{
  "presets": [
    ["@babel/preset-env", {
      "targets": {
        "browsers": ["last 2 versions", "ie >= 11"]
      }
    }],
    "@babel/preset-react"
  ],
  "plugins": [
    "@babel/plugin-proposal-class-properties",
    "@babel/plugin-proposal-object-rest-spread"
  ]
}
```

## Component Architecture

### Base Component Structure

```javascript
// src/lib/components/DashCopilotkitComponents.react.js
import React, { useState, useEffect, useCallback } from 'react';
import PropTypes from 'prop-types';
import { CopilotKitProvider } from '@copilotkit/react-core';
import { 
    CopilotPopup, 
    CopilotSidebar, 
    CopilotChat, 
    CopilotTextarea 
} from '@copilotkit/react-ui';

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

    // State management
    const [currentValue, setCurrentValue] = useState(value || '');
    const [isInitialized, setIsInitialized] = useState(false);

    // Effect for prop synchronization
    useEffect(() => {
        if (value !== currentValue) {
            setCurrentValue(value || '');
        }
    }, [value]);

    // Callback for value changes
    const handleValueChange = useCallback((newValue) => {
        setCurrentValue(newValue);
        if (setProps) {
            setProps({ value: newValue });
        }
    }, [setProps]);

    // Render different UI types
    const renderUIComponent = () => {
        const commonProps = {
            instructions: instructions || 'You are a helpful AI assistant.',
            disabled: disabled,
            className: className,
            style: style
        };

        switch (ui_type) {
            case 'chat':
                return (
                    <CopilotChat
                        {...commonProps}
                        labels={labels}
                        style={{
                            ...style,
                            width: width,
                            height: height
                        }}
                    />
                );

            case 'popup':
                return (
                    <CopilotPopup
                        {...commonProps}
                        labels={labels}
                        defaultOpen={show_initially}
                    />
                );

            case 'sidebar':
                return (
                    <CopilotSidebar
                        {...commonProps}
                        labels={labels}
                        defaultOpen={show_initially}
                        side={position}
                        style={{
                            ...style,
                            width: width
                        }}
                    />
                );

            case 'textarea':
                return (
                    <CopilotTextarea
                        {...commonProps}
                        placeholder={placeholder}
                        value={currentValue}
                        onChange={handleValueChange}
                        style={{
                            ...style,
                            width: width,
                            height: height
                        }}
                    />
                );

            default:
                return <div>Unsupported UI type: {ui_type}</div>;
        }
    };

    // Main render
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

// Default props
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

// Prop types validation
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

### Component Registration

```javascript
// src/lib/index.js
import DashCopilotkitComponents from './components/DashCopilotkitComponents.react';

export {
    DashCopilotkitComponents
};
```

## Python Binding Generation

### Automatic Generation

```bash
# Generate Python bindings
python -m dash.development.build_components \
    ./src/lib/components \
    dash_copilotkit_components \
    --r-prefix ckc \
    --jl-prefix ckc
```

### Generated Python Component

The build process generates `dash_copilotkit_components/DashCopilotkitComponents.py`:

```python
# AUTO GENERATED FILE - DO NOT EDIT

import typing
from typing_extensions import TypedDict, NotRequired, Literal
from dash.development.base_component import Component, _explicitize_args

class DashCopilotkitComponents(Component):
    """A DashCopilotkitComponents component.
    
    Keyword arguments:
    - id (string; optional): The ID used to identify this component in Dash callbacks.
    - ui_type (a value equal to: 'chat', 'popup', 'sidebar', 'textarea'; default 'chat')
    - public_api_key (string; optional): Your CopilotKit Cloud public API key.
    # ... other props
    """
    
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_copilotkit_components'
    _type = 'DashCopilotkitComponents'

    def __init__(self, id=None, ui_type=None, **kwargs):
        self._prop_names = ['id', 'ui_type', 'public_api_key', ...]
        self._valid_wildcard_attributes = []
        self.available_properties = ['id', 'ui_type', 'public_api_key', ...]
        self.available_wildcard_properties = []
        
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)
        args = {k: _locals[k] for k in _explicit_args}

        super(DashCopilotkitComponents, self).__init__(**args)
```

## Advanced Component Features

### Custom Hooks

```javascript
// src/lib/hooks/useCopilotState.js
import { useState, useEffect, useCallback } from 'react';

export const useCopilotState = (initialValue, setProps) => {
    const [value, setValue] = useState(initialValue);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const updateValue = useCallback((newValue) => {
        setValue(newValue);
        if (setProps) {
            setProps({ value: newValue });
        }
    }, [setProps]);

    const handleError = useCallback((err) => {
        setError(err);
        if (setProps) {
            setProps({ error: err.message });
        }
    }, [setProps]);

    return {
        value,
        setValue: updateValue,
        isLoading,
        setIsLoading,
        error,
        handleError
    };
};
```

### Context Provider

```javascript
// src/lib/context/CopilotContext.js
import React, { createContext, useContext, useReducer } from 'react';

const CopilotContext = createContext();

const initialState = {
    isConnected: false,
    messages: [],
    currentUser: null,
    settings: {}
};

function copilotReducer(state, action) {
    switch (action.type) {
        case 'SET_CONNECTED':
            return { ...state, isConnected: action.payload };
        case 'ADD_MESSAGE':
            return { ...state, messages: [...state.messages, action.payload] };
        case 'SET_USER':
            return { ...state, currentUser: action.payload };
        case 'UPDATE_SETTINGS':
            return { ...state, settings: { ...state.settings, ...action.payload } };
        default:
            return state;
    }
}

export const CopilotProvider = ({ children }) => {
    const [state, dispatch] = useReducer(copilotReducer, initialState);

    return (
        <CopilotContext.Provider value={{ state, dispatch }}>
            {children}
        </CopilotContext.Provider>
    );
};

export const useCopilot = () => {
    const context = useContext(CopilotContext);
    if (!context) {
        throw new Error('useCopilot must be used within a CopilotProvider');
    }
    return context;
};
```

## Build Optimization

### Code Splitting

```javascript
// Dynamic imports for code splitting
const LazyChat = React.lazy(() => import('./components/LazyChat'));
const LazySidebar = React.lazy(() => import('./components/LazySidebar'));

const DashCopilotkitComponents = (props) => {
    const renderUIComponent = () => {
        return (
            <React.Suspense fallback={<div>Loading...</div>}>
                {ui_type === 'chat' && <LazyChat {...props} />}
                {ui_type === 'sidebar' && <LazySidebar {...props} />}
            </React.Suspense>
        );
    };

    return (
        <div id={id}>
            {renderUIComponent()}
        </div>
    );
};
```

### Bundle Analysis

```bash
# Install bundle analyzer
npm install --save-dev webpack-bundle-analyzer

# Add to package.json scripts
"analyze": "webpack-bundle-analyzer dist/static/js/*.js"

# Run analysis
npm run build
npm run analyze
```

### Tree Shaking

```javascript
// webpack.config.js optimization
module.exports = {
    optimization: {
        usedExports: true,
        sideEffects: false,
        splitChunks: {
            chunks: 'all',
            cacheGroups: {
                vendor: {
                    test: /[\\/]node_modules[\\/]/,
                    name: 'vendors',
                    chunks: 'all'
                }
            }
        }
    }
};
```

## Testing the Build

### Unit Tests for Build

```javascript
// tests/build.test.js
import { DashCopilotkitComponents } from '../src/lib/index';

describe('Build Output', () => {
    test('exports DashCopilotkitComponents', () => {
        expect(DashCopilotkitComponents).toBeDefined();
        expect(typeof DashCopilotkitComponents).toBe('function');
    });

    test('component has required props', () => {
        const component = new DashCopilotkitComponents({
            id: 'test',
            ui_type: 'chat'
        });
        
        expect(component.props.id).toBe('test');
        expect(component.props.ui_type).toBe('chat');
    });
});
```

### Integration Tests

```python
# tests/test_build_integration.py
import subprocess
import os
import pytest

def test_build_process():
    """Test that build process completes successfully"""
    result = subprocess.run(['npm', 'run', 'build'], 
                          capture_output=True, text=True)
    assert result.returncode == 0

def test_python_bindings_generation():
    """Test Python bindings generation"""
    result = subprocess.run([
        'python', '-m', 'dash.development.build_components',
        './src/lib/components',
        'dash_copilotkit_components',
        '--r-prefix', 'ckc',
        '--jl-prefix', 'ckc'
    ], capture_output=True, text=True)
    
    assert result.returncode == 0
    assert os.path.exists('dash_copilotkit_components/DashCopilotkitComponents.py')
```

## Continuous Integration

### GitHub Actions

```yaml
# .github/workflows/build.yml
name: Build and Test

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        node-version: [16.x, 18.x]
        python-version: [3.8, 3.9, '3.10', '3.11']

    steps:
    - uses: actions/checkout@v3
    
    - name: Use Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v3
      with:
        node-version: ${{ matrix.node-version }}
        cache: 'npm'
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install Node dependencies
      run: npm ci
    
    - name: Install Python dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Lint JavaScript
      run: npm run lint
    
    - name: Test JavaScript
      run: npm test
    
    - name: Build component
      run: npm run build
    
    - name: Generate Python bindings
      run: |
        python -m dash.development.build_components \
          ./src/lib/components \
          dash_copilotkit_components \
          --r-prefix ckc \
          --jl-prefix ckc
    
    - name: Test Python
      run: python -m pytest tests/
    
    - name: Build documentation
      run: |
        pip install mkdocs mkdocs-material
        mkdocs build
```

## Troubleshooting Build Issues

### Common Problems

1. **Node modules not found**: Run `npm install`
2. **Python binding generation fails**: Check component prop types
3. **Webpack build errors**: Check JavaScript syntax and imports
4. **Missing dependencies**: Update package.json and requirements.txt

### Debug Build

```bash
# Enable verbose webpack output
npm run build -- --verbose

# Debug Python binding generation
python -m dash.development.build_components \
  ./src/lib/components \
  dash_copilotkit_components \
  --r-prefix ckc \
  --jl-prefix ckc \
  --verbose
```

## Next Steps

- [Development Guide](development.md) - General development workflow
- [Testing Guide](testing.md) - Comprehensive testing strategies
- [Deployment](../deployment/production.md) - Deploy your built components
