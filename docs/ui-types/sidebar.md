# Sidebar Chat

The sidebar chat interface slides in from the left or right side of your application. It's perfect for applications where you want a persistent chat option that doesn't take up main content space.

## Features

- **Side Panel Design**: Slides in from left or right side
- **Persistent Access**: Always available without blocking content
- **Configurable Width**: Adjustable sidebar width
- **Smooth Animations**: Elegant slide-in/out transitions
- **Overlay Option**: Optional backdrop overlay when open

## Basic Usage

```python
import dash_copilotkit_components
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    # Your existing app content
    html.H1("My Dashboard"),
    html.Div("Your dashboard content goes here..."),
    
    # Sidebar chat component
    dash_copilotkit_components.DashCopilotkitComponents(
        id='sidebar-copilot',
        ui_type='sidebar',
        public_api_key='your-copilotkit-cloud-api-key',
        position='right'
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
| `ui_type` | string | Must be set to `'sidebar'` |
| `public_api_key` or `api_key` | string | Your CopilotKit API key |

### Optional Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `instructions` | string | "You are a helpful AI assistant." | Custom instructions for the AI |
| `labels` | object | `{}` | Custom labels for title and initial message |
| `position` | string | 'right' | Sidebar position: 'left' or 'right' |
| `show_initially` | boolean | false | Whether sidebar is open on page load |
| `width` | string | '350px' | Width of the sidebar |
| `disabled` | boolean | false | Whether the sidebar is disabled |
| `className` | string | - | Custom CSS class |
| `style` | object | - | Inline styles |

## Advanced Configuration

### Left Side Position

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='sidebar-copilot',
    ui_type='sidebar',
    public_api_key='your-api-key',
    position='left',  # Slides in from left
    width='400px'
)
```

### Custom Width

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='sidebar-copilot',
    ui_type='sidebar',
    public_api_key='your-api-key',
    position='right',
    width='300px',  # Narrower sidebar
    show_initially=True  # Open by default
)
```

### Custom Labels and Instructions

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='sidebar-copilot',
    ui_type='sidebar',
    public_api_key='your-api-key',
    position='right',
    instructions='You are a helpful assistant for this dashboard application.',
    labels={
        'title': 'Dashboard Assistant',
        'initial': 'Hello! I can help you navigate and understand your dashboard.'
    }
)
```

## Use Cases

### Dashboard Assistant
Provide contextual help and insights for dashboard applications.

### Navigation Helper
Guide users through complex applications and workflows.

### Data Analysis Support
Offer AI-powered explanations and insights for data visualizations.

### Documentation Assistant
Provide instant access to help and documentation.

## Integration Patterns

### With Dashboard Applications

```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_copilotkit_components

app = Dash(__name__)

app.layout = html.Div([
    # Main dashboard layout
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("Analytics Dashboard"),
                dcc.Graph(id="main-chart")
            ], width=8),
            dbc.Col([
                html.H3("Key Metrics"),
                html.Div(id="metrics")
            ], width=4)
        ])
    ], fluid=True),
    
    # Sidebar assistant
    dash_copilotkit_components.DashCopilotkitComponents(
        id='dashboard-sidebar',
        ui_type='sidebar',
        public_api_key='your-api-key',
        position='right',
        instructions='''
        You are a dashboard assistant. Help users:
        - Understand chart data and trends
        - Navigate dashboard features
        - Interpret metrics and KPIs
        - Find specific information
        '''
    )
])
```

### With Multi-Page Applications

```python
# Sidebar available across all pages
app.layout = html.Div([
    dcc.Location(id='url'),
    html.Div(id='page-content'),
    
    # Global sidebar assistant
    dash_copilotkit_components.DashCopilotkitComponents(
        id='global-sidebar',
        ui_type='sidebar',
        public_api_key='your-api-key',
        position='left',
        instructions='You are a helpful assistant for this application.'
    )
])
```

## Responsive Design

### Mobile Considerations

```python
# Responsive sidebar that adapts to screen size
dash_copilotkit_components.DashCopilotkitComponents(
    id='responsive-sidebar',
    ui_type='sidebar',
    public_api_key='your-api-key',
    position='right',
    width='min(350px, 90vw)',  # Responsive width
    className='responsive-sidebar'
)
```

### Custom CSS for Responsiveness

```css
/* Responsive sidebar styling */
.responsive-sidebar {
    --sidebar-width: 350px;
}

@media (max-width: 768px) {
    .responsive-sidebar {
        --sidebar-width: 90vw;
        --sidebar-height: 70vh;
    }
}

@media (max-width: 480px) {
    .responsive-sidebar {
        --sidebar-width: 100vw;
        --sidebar-height: 100vh;
    }
}
```

## Best Practices

1. **Choose Appropriate Side**: Consider your app's layout and user flow
2. **Reasonable Width**: Don't make the sidebar too wide (300-400px is good)
3. **Clear Toggle**: Provide obvious ways to open/close the sidebar
4. **Mobile Responsive**: Test on mobile devices and adjust accordingly
5. **Content Awareness**: Make the AI aware of the current page/context

## Styling Tips

### Custom Animations

```css
/* Custom slide animation */
.custom-sidebar {
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.custom-sidebar.open {
    transform: translateX(0);
}

.custom-sidebar.closed {
    transform: translateX(100%);
}
```

### Backdrop Styling

```css
/* Custom backdrop when sidebar is open */
.sidebar-backdrop {
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(2px);
    transition: opacity 0.3s ease;
}
```

## Troubleshooting

### Common Issues

**Sidebar not sliding properly:**
- Check CSS transitions and transforms
- Verify position prop is 'left' or 'right'
- Ensure no conflicting CSS

**Content shifting when sidebar opens:**
- Use absolute positioning for sidebar
- Avoid changing main content layout
- Consider using overlay mode

**Mobile display problems:**
- Test on actual mobile devices
- Adjust width for smaller screens
- Consider full-screen mode on mobile

## Examples

See the [Examples section](../examples/basic.md) for more detailed code examples and integration patterns.
