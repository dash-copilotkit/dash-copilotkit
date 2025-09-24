# Chat Interface

The chat interface provides a full-featured chat experience embedded directly in your Dash application. It's perfect for customer support, interactive assistants, or any conversational AI use case.

## Features

- **Full Chat Experience**: Complete chat interface with message history
- **Customizable Styling**: Control appearance with CSS classes and inline styles
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Real-time Interaction**: Instant AI responses with typing indicators
- **Message Persistence**: Chat history maintained during session

## Basic Usage

```python
import dash_copilotkit_components
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    dash_copilotkit_components.DashCopilotkitComponents(
        id='chat-copilot',
        ui_type='chat',
        public_api_key='your-copilotkit-cloud-api-key',
        instructions='You are a helpful AI assistant.',
        height='500px'
    )
])

if __name__ == '__main__':
    app.run(debug=True)
```

## Configuration Options

### Required Props

| Prop | Type | Description |
|------|------|-------------|
| `id` | string | Unique identifier for the component |
| `ui_type` | string | Must be set to `'chat'` |
| `public_api_key` or `api_key` | string | Your CopilotKit API key |

### Optional Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `instructions` | string | "You are a helpful AI assistant." | Custom instructions for the AI |
| `labels` | object | `{}` | Custom labels for title and initial message |
| `height` | string | '400px' | Height of the chat interface |
| `width` | string | '100%' | Width of the chat interface |
| `disabled` | boolean | false | Whether the chat is disabled |
| `className` | string | - | Custom CSS class |
| `style` | object | - | Inline styles |

## Advanced Configuration

### Custom Labels

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='chat-copilot',
    ui_type='chat',
    public_api_key='your-api-key',
    labels={
        'title': 'Customer Support',
        'initial': 'Hello! How can I help you today?'
    }
)
```

### Custom Styling

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='chat-copilot',
    ui_type='chat',
    public_api_key='your-api-key',
    height='600px',
    width='100%',
    className='custom-chat',
    style={
        'border': '2px solid #007bff',
        'borderRadius': '10px',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'
    }
)
```

### Custom Instructions

```python
instructions = """
You are a customer support assistant for TechCorp.
- Be friendly and professional
- Help with product questions, orders, and technical issues
- If you can't help, direct users to human support
- Keep responses concise but helpful
- Use the customer's name when possible
"""

dash_copilotkit_components.DashCopilotkitComponents(
    id='support-chat',
    ui_type='chat',
    public_api_key='your-api-key',
    instructions=instructions
)
```

## Use Cases

### Customer Support
Perfect for providing 24/7 customer support with AI assistance.

### Interactive Documentation
Help users navigate and understand your application or documentation.

### Data Analysis Assistant
Provide AI-powered insights and explanations for data visualizations.

### Educational Tutor
Create interactive learning experiences with personalized AI tutoring.

## Best Practices

1. **Clear Instructions**: Provide specific, detailed instructions for the AI's role
2. **Appropriate Height**: Set a comfortable height (400-600px) for desktop use
3. **Mobile Responsive**: Test on mobile devices and adjust styling as needed
4. **Error Handling**: Always validate API keys and handle connection errors
5. **User Feedback**: Provide clear feedback when the chat is loading or unavailable

## Troubleshooting

### Common Issues

**Chat not loading:**
- Verify your API key is correct
- Check network connectivity
- Ensure the component has a valid `id`

**Styling issues:**
- Use browser developer tools to inspect CSS
- Check for conflicting styles
- Validate CSS syntax in `style` prop

**Mobile display problems:**
- Test responsive design on different screen sizes
- Consider using percentage-based widths
- Adjust height for mobile viewports

## Examples

See the [Examples section](../examples/basic.md) for more detailed code examples and integration patterns.
