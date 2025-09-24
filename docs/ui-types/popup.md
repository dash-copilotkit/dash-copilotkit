# Popup Chat

The popup chat interface provides a toggleable chat window that appears over your application. It's perfect for customer support or help systems where you want the chat to be available but not always visible.

## Features

- **Non-Intrusive**: Appears as a floating button until activated
- **Overlay Design**: Opens over existing content without navigation
- **Customizable Position**: Can be positioned in any corner
- **Toggle Functionality**: Easy open/close with smooth animations
- **Persistent State**: Remembers open/closed state during session

## Basic Usage

```python
import dash_copilotkit_components
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    # Your existing app content
    html.H1("My Application"),
    html.P("Your app content goes here..."),
    
    # Popup chat component
    dash_copilotkit_components.DashCopilotkitComponents(
        id='popup-copilot',
        ui_type='popup',
        public_api_key='your-copilotkit-cloud-api-key',
        show_initially=False
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
| `ui_type` | string | Must be set to `'popup'` |
| `public_api_key` or `api_key` | string | Your CopilotKit API key |

### Optional Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `instructions` | string | "You are a helpful AI assistant." | Custom instructions for the AI |
| `labels` | object | `{}` | Custom labels for title and initial message |
| `show_initially` | boolean | false | Whether popup is open on page load |
| `disabled` | boolean | false | Whether the popup is disabled |
| `className` | string | - | Custom CSS class |
| `style` | object | - | Inline styles |

## Advanced Configuration

### Custom Labels

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='popup-copilot',
    ui_type='popup',
    public_api_key='your-api-key',
    labels={
        'title': 'Help Assistant',
        'initial': 'Hi! Need help with anything?'
    }
)
```

### Show Initially

```python
# Popup opens automatically when page loads
dash_copilotkit_components.DashCopilotkitComponents(
    id='popup-copilot',
    ui_type='popup',
    public_api_key='your-api-key',
    show_initially=True
)
```

### Custom Styling

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='popup-copilot',
    ui_type='popup',
    public_api_key='your-api-key',
    className='custom-popup',
    style={
        'zIndex': '9999',
        'borderRadius': '15px'
    }
)
```

## Use Cases

### Customer Support
Provide instant help without disrupting the user's workflow.

### Onboarding Assistant
Guide new users through your application features.

### Help System
Offer contextual help and documentation assistance.

### Feedback Collection
Gather user feedback and suggestions through conversational interface.

## Integration Patterns

### With Existing Applications

```python
from dash import Dash, html, dcc
import dash_copilotkit_components

app = Dash(__name__)

app.layout = html.Div([
    # Your existing navigation
    html.Nav([
        html.A("Home", href="/"),
        html.A("Products", href="/products"),
        html.A("Contact", href="/contact")
    ]),
    
    # Main content area
    html.Main([
        html.H1("Welcome to Our Store"),
        dcc.Graph(id="sales-chart"),
        # ... other content
    ]),
    
    # Popup chat - doesn't interfere with layout
    dash_copilotkit_components.DashCopilotkitComponents(
        id='support-popup',
        ui_type='popup',
        public_api_key='your-api-key',
        instructions='You are a helpful e-commerce assistant.',
        labels={
            'title': 'Shopping Assistant',
            'initial': 'Hi! Need help finding something?'
        }
    )
])
```

### Multiple Popups

```python
# You can have multiple popups for different purposes
app.layout = html.Div([
    # Main support popup
    dash_copilotkit_components.DashCopilotkitComponents(
        id='support-popup',
        ui_type='popup',
        public_api_key='your-api-key',
        instructions='You are a customer support assistant.'
    ),
    
    # Technical help popup (could be triggered by specific pages)
    dash_copilotkit_components.DashCopilotkitComponents(
        id='tech-popup',
        ui_type='popup',
        public_api_key='your-api-key',
        instructions='You are a technical support specialist.',
        show_initially=False
    )
])
```

## Best Practices

1. **Don't Show Initially**: Let users choose when to open the popup
2. **Clear Purpose**: Make it obvious what the popup chat is for
3. **Appropriate Timing**: Consider showing after user inactivity or on specific pages
4. **Mobile Friendly**: Ensure popup works well on mobile devices
5. **Escape Routes**: Always provide clear ways to close the popup

## Styling Tips

### Custom CSS

```css
/* Custom popup styling */
.custom-popup {
    --popup-border-radius: 20px;
    --popup-shadow: 0 10px 30px rgba(0,0,0,0.2);
    --popup-max-width: 400px;
}

/* Mobile responsive */
@media (max-width: 768px) {
    .custom-popup {
        --popup-max-width: 90vw;
        --popup-margin: 10px;
    }
}
```

## Troubleshooting

### Common Issues

**Popup not appearing:**
- Check if `show_initially` is set correctly
- Verify the popup trigger button is visible
- Ensure no CSS is hiding the popup

**Popup behind other elements:**
- Increase `zIndex` in the style prop
- Check for competing z-index values in your CSS

**Mobile display issues:**
- Test on actual mobile devices
- Adjust popup size for smaller screens
- Ensure touch targets are large enough

## Examples

See the [Examples section](../examples/basic.md) for more detailed code examples and integration patterns.
