# Component Props

Complete reference for all props available in the Dash CopilotKit Components.

## Required Props

### `id`
- **Type**: `string`
- **Required**: Yes
- **Description**: Unique identifier for the component, used for Dash callbacks
- **Example**: `'my-copilot'`

### `ui_type`
- **Type**: `string`
- **Required**: Yes
- **Options**: `'chat'`, `'popup'`, `'sidebar'`, `'textarea'`
- **Description**: Determines which UI interface to render
- **Example**: `'chat'`

### API Authentication (One Required)

#### `public_api_key`
- **Type**: `string`
- **Required**: Yes (if not using `api_key` + `runtime_url`)
- **Description**: Your CopilotKit Cloud public API key
- **Example**: `'ck_pub_1234567890abcdef'`

#### `api_key` + `runtime_url`
- **Type**: `string`
- **Required**: Yes (if not using `public_api_key`)
- **Description**: Your OpenAI API key and custom runtime URL
- **Example**: 
  ```python
  api_key='sk-1234567890abcdef'
  runtime_url='http://localhost:3000/api/copilotkit'
  ```

## Optional Props

### `instructions`
- **Type**: `string`
- **Default**: `"You are a helpful AI assistant."`
- **Description**: Custom instructions that define the AI's behavior and role
- **Example**: 
  ```python
  instructions="You are a customer support assistant. Be helpful and professional."
  ```

### `labels`
- **Type**: `object`
- **Default**: `{}`
- **Description**: Custom labels for UI text elements
- **Properties**:
  - `title` (string): Title displayed in the interface
  - `initial` (string): Initial message from the AI
- **Example**:
  ```python
  labels={
      'title': 'Customer Support',
      'initial': 'Hello! How can I help you today?'
  }
  ```

### `placeholder`
- **Type**: `string`
- **Default**: `"Type your message here..."`
- **Description**: Placeholder text for input fields
- **Applies to**: All UI types
- **Example**: `'Start typing here...'`

### `value`
- **Type**: `string`
- **Default**: `""`
- **Description**: Current text value (primarily for textarea type)
- **Applies to**: `textarea` UI type
- **Example**: `'Initial content here'`

### `disabled`
- **Type**: `boolean`
- **Default**: `false`
- **Description**: Whether the component is disabled
- **Example**: `True`

### `className`
- **Type**: `string`
- **Default**: `None`
- **Description**: CSS class name for custom styling
- **Example**: `'my-custom-chat'`

### `style`
- **Type**: `object`
- **Default**: `{}`
- **Description**: Inline CSS styles
- **Example**:
  ```python
  style={
      'border': '2px solid #007bff',
      'borderRadius': '10px',
      'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
  }
  ```

### `width`
- **Type**: `string`
- **Default**: `'100%'`
- **Description**: Component width
- **Example**: `'500px'`, `'80%'`, `'100vw'`

### `height`
- **Type**: `string`
- **Default**: `'400px'`
- **Description**: Component height
- **Example**: `'600px'`, `'50vh'`, `'auto'`

## UI Type Specific Props

### Sidebar Props

#### `position`
- **Type**: `string`
- **Default**: `'right'`
- **Options**: `'left'`, `'right'`
- **Applies to**: `sidebar` UI type
- **Description**: Which side the sidebar slides in from
- **Example**: `'left'`

### Popup & Sidebar Props

#### `show_initially`
- **Type**: `boolean`
- **Default**: `false`
- **Applies to**: `popup`, `sidebar` UI types
- **Description**: Whether the component is visible when the page loads
- **Example**: `True`

## Prop Validation

The component validates all props and will raise errors for:

- Invalid `ui_type` values
- Missing required authentication props
- Invalid `position` values for sidebar
- Incorrect prop types

### Example Error Messages

```
TypeError: The `dash_copilotkit_components.DashCopilotkitComponents` component 
received an unexpected keyword argument: `invalid_prop`

Invalid argument `position` passed into DashCopilotkitComponents.
Expected one of ["left","right"]. Value provided: "top"
```

## Complete Example

```python
import dash_copilotkit_components
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    dash_copilotkit_components.DashCopilotkitComponents(
        # Required props
        id='comprehensive-example',
        ui_type='chat',
        public_api_key='ck_pub_1234567890abcdef',
        
        # Optional configuration
        instructions='''
        You are a helpful customer service assistant for TechCorp.
        - Be friendly and professional
        - Help with product questions and technical support
        - Escalate complex issues to human agents
        - Keep responses concise but thorough
        ''',
        
        labels={
            'title': 'TechCorp Support',
            'initial': 'Hi! I\'m here to help with any questions about our products.'
        },
        
        placeholder='Ask me anything about our products...',
        
        # Styling
        className='custom-support-chat',
        style={
            'border': '2px solid #0066cc',
            'borderRadius': '12px',
            'boxShadow': '0 4px 12px rgba(0,102,204,0.15)'
        },
        
        # Dimensions
        width='100%',
        height='500px',
        
        # State
        disabled=False
    )
])
```

## Environment Variables

For security, store API keys in environment variables:

```python
import os
import dash_copilotkit_components

# Set environment variable first:
# export CKC_PUBLIC_API_KEY=ck_pub_1234567890abcdef

dash_copilotkit_components.DashCopilotkitComponents(
    id='secure-copilot',
    ui_type='chat',
    public_api_key=os.getenv('CKC_PUBLIC_API_KEY'),
    instructions='You are a secure AI assistant.'
)
```

## Prop Combinations

### CopilotKit Cloud Configuration
```python
# Simplest setup with CopilotKit Cloud
dash_copilotkit_components.DashCopilotkitComponents(
    id='cloud-copilot',
    ui_type='chat',
    public_api_key='ck_pub_1234567890abcdef'
)
```

### Custom Runtime Configuration
```python
# Using your own OpenAI key and runtime
dash_copilotkit_components.DashCopilotkitComponents(
    id='custom-copilot',
    ui_type='chat',
    api_key='sk-1234567890abcdef',
    runtime_url='https://my-app.com/api/copilotkit'
)
```

### Sidebar Configuration
```python
# Left sidebar that shows initially
dash_copilotkit_components.DashCopilotkitComponents(
    id='sidebar-copilot',
    ui_type='sidebar',
    public_api_key='ck_pub_1234567890abcdef',
    position='left',
    show_initially=True,
    width='350px'
)
```

### Textarea Configuration
```python
# AI-powered textarea with custom placeholder
dash_copilotkit_components.DashCopilotkitComponents(
    id='textarea-copilot',
    ui_type='textarea',
    public_api_key='ck_pub_1234567890abcdef',
    placeholder='Start writing your article...',
    value='',
    height='300px'
)
```

## Next Steps

- [Callbacks](callbacks.md) - Learn how to interact with the component
- [Styling](styling.md) - Advanced styling and theming options
- [Examples](../examples/basic.md) - See these props in action
