# Configuration

Learn how to configure Dash CopilotKit Components for your specific needs.

## API Configuration

### CopilotKit Cloud

The easiest way to get started is with CopilotKit Cloud:

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='copilot',
    ui_type='chat',
    public_api_key='ck_pub_1234567890abcdef'  # Your CopilotKit Cloud API key
)
```

**Advantages:**
- No server setup required
- Automatic scaling
- Built-in security
- Free tier available

### Bring Your Own Key

For more control, use your own OpenAI API key:

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='copilot',
    ui_type='chat',
    runtime_url='http://localhost:3000/api/copilotkit',
    api_key='sk-1234567890abcdef'  # Your OpenAI API key
)
```

**Requirements:**
- Set up a CopilotKit runtime server
- Manage your own API keys
- Handle scaling and security

## Environment Variables

For security, store API keys in environment variables:

```python
import os
import dash_copilotkit_components

# Set environment variable
# export CKC_PUBLIC_API_KEY=ck_pub_1234567890abcdef

dash_copilotkit_components.DashCopilotkitComponents(
    id='copilot',
    ui_type='chat',
    public_api_key=os.getenv('CKC_PUBLIC_API_KEY')
)
```

## Component Configuration

### Basic Props

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='copilot',                    # Required: Unique component ID
    ui_type='chat',                  # Required: 'chat', 'popup', 'sidebar', 'textarea'
    public_api_key='your-key',       # API key for CopilotKit Cloud
    instructions='Custom instructions for the AI',
    disabled=False,                  # Enable/disable the component
    className='custom-css-class',    # Custom CSS class
    style={'border': '1px solid #ccc'}  # Inline styles
)
```

### Labels and Messages

Customize the text displayed in the interface:

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='copilot',
    ui_type='chat',
    public_api_key='your-key',
    labels={
        'title': 'Customer Support',
        'initial': 'Hi! How can I help you today?',
        'placeholder': 'Type your message here...'
    }
)
```

### Styling Options

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='copilot',
    ui_type='chat',
    public_api_key='your-key',
    width='100%',                    # Component width
    height='600px',                  # Component height
    style={
        'border': '2px solid #007bff',
        'borderRadius': '10px',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
    }
)
```

## UI Type Specific Configuration

### Chat Interface

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='chat-copilot',
    ui_type='chat',
    public_api_key='your-key',
    height='500px',                  # Chat window height
    width='100%',                    # Chat window width
    show_header=True,                # Show/hide header
    show_footer=True                 # Show/hide footer
)
```

### Popup Chat

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='popup-copilot',
    ui_type='popup',
    public_api_key='your-key',
    show_initially=False,            # Show popup on load
    position='bottom-right',         # Popup position
    trigger_button_text='Chat'       # Button text
)
```

### Sidebar Chat

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='sidebar-copilot',
    ui_type='sidebar',
    public_api_key='your-key',
    position='right',                # 'left' or 'right'
    width='350px',                   # Sidebar width
    show_initially=False,            # Show sidebar on load
    overlay=True                     # Show overlay when open
)
```

### AI Textarea

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='textarea-copilot',
    ui_type='textarea',
    public_api_key='your-key',
    placeholder='Start typing...',   # Placeholder text
    value='',                        # Initial value
    rows=10,                         # Number of rows
    auto_resize=True,                # Auto-resize height
    max_length=5000                  # Maximum character limit
)
```

## Advanced Configuration

### Custom Instructions

Provide detailed instructions to customize the AI's behavior:

```python
instructions = """
You are a helpful customer support assistant for an e-commerce website.
- Be friendly and professional
- Help users with orders, returns, and product questions
- If you don't know something, direct them to contact human support
- Keep responses concise but helpful
- Use emojis sparingly and appropriately
"""

dash_copilotkit_components.DashCopilotkitComponents(
    id='support-copilot',
    ui_type='chat',
    public_api_key='your-key',
    instructions=instructions
)
```

### Multiple Components

You can use multiple components in the same app:

```python
app.layout = html.Div([
    # Main chat for customer support
    dash_copilotkit_components.DashCopilotkitComponents(
        id='support-chat',
        ui_type='chat',
        public_api_key='your-key',
        instructions='You are a customer support assistant.'
    ),
    
    # Sidebar for quick help
    dash_copilotkit_components.DashCopilotkitComponents(
        id='help-sidebar',
        ui_type='sidebar',
        public_api_key='your-key',
        instructions='You provide quick help and tips.',
        position='right'
    ),
    
    # AI textarea for content creation
    dash_copilotkit_components.DashCopilotkitComponents(
        id='content-textarea',
        ui_type='textarea',
        public_api_key='your-key',
        instructions='You help users write better content.',
        placeholder='Write your content here...'
    )
])
```

## Security Best Practices

1. **Use Environment Variables**: Never hardcode API keys in your source code
2. **Validate Inputs**: Always validate user inputs before processing
3. **Rate Limiting**: Implement rate limiting for production applications
4. **HTTPS Only**: Always use HTTPS in production
5. **API Key Rotation**: Regularly rotate your API keys

```python
import os
from dash import Dash, html
import dash_copilotkit_components

# Secure configuration
app = Dash(__name__)

# Validate API key exists
api_key = os.getenv('CKC_PUBLIC_API_KEY')
if not api_key:
    raise ValueError("CKC_PUBLIC_API_KEY environment variable is required")

app.layout = html.Div([
    dash_copilotkit_components.DashCopilotkitComponents(
        id='secure-copilot',
        ui_type='chat',
        public_api_key=api_key,
        instructions='You are a secure AI assistant.'
    )
])
```

## Next Steps

- **[UI Types](../ui-types/chat.md)** - Learn about each interface type
- **[API Reference](../api/props.md)** - Complete prop documentation
- **[Examples](../examples/basic.md)** - See configuration examples in action
