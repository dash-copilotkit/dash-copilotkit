# AI Textarea

The AI textarea provides an intelligent text input field that helps users write better content. It's perfect for forms, content creation, email composition, or any text input that benefits from AI assistance.

## Features

- **AI-Powered Suggestions**: Real-time writing assistance and improvements
- **Auto-completion**: Smart text completion based on context
- **Grammar & Style**: Automatic grammar checking and style suggestions
- **Customizable Placeholder**: Custom placeholder text and instructions
- **Value Tracking**: Monitor and respond to text changes via callbacks

## Basic Usage

```python
import dash_copilotkit_components
from dash import Dash, html, callback, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H1("AI-Powered Text Editor"),
    
    dash_copilotkit_components.DashCopilotkitComponents(
        id='ai-textarea',
        ui_type='textarea',
        public_api_key='your-copilotkit-cloud-api-key',
        placeholder='Start writing your content here...',
        instructions='You are a helpful writing assistant.'
    ),
    
    html.Div(id='content-output')
])

@callback(
    Output('content-output', 'children'),
    Input('ai-textarea', 'value')
)
def display_content(value):
    return f"Current content: {value or 'No content yet...'}"

if __name__ == '__main__':
    app.run(debug=True)
```

## Configuration Options

### Required Props

| Prop | Type | Description |
|------|------|-------------|
| `id` | string | Unique identifier for the component |
| `ui_type` | string | Must be set to `'textarea'` |
| `public_api_key` or `api_key` | string | Your CopilotKit API key |

### Optional Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `instructions` | string | "You are a helpful writing assistant." | Custom instructions for the AI |
| `placeholder` | string | "Type your message here..." | Placeholder text |
| `value` | string | "" | Initial or current text value |
| `disabled` | boolean | false | Whether the textarea is disabled |
| `className` | string | - | Custom CSS class |
| `style` | object | - | Inline styles |
| `width` | string | '100%' | Width of the textarea |
| `height` | string | 'auto' | Height of the textarea |

## Advanced Configuration

### Custom Instructions for Different Use Cases

#### Email Composition
```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='email-textarea',
    ui_type='textarea',
    public_api_key='your-api-key',
    instructions='''
    You are an email writing assistant. Help users write:
    - Professional and clear emails
    - Appropriate tone for business communication
    - Proper email structure and formatting
    - Concise and effective messaging
    ''',
    placeholder='Compose your email here...'
)
```

#### Creative Writing
```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='creative-textarea',
    ui_type='textarea',
    public_api_key='your-api-key',
    instructions='''
    You are a creative writing assistant. Help users with:
    - Story development and plot ideas
    - Character development
    - Descriptive language and imagery
    - Dialogue improvement
    - Creative inspiration
    ''',
    placeholder='Start your creative writing here...'
)
```

#### Technical Documentation
```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='docs-textarea',
    ui_type='textarea',
    public_api_key='your-api-key',
    instructions='''
    You are a technical writing assistant. Help users create:
    - Clear and concise documentation
    - Proper technical terminology
    - Well-structured explanations
    - Code examples and snippets
    - User-friendly instructions
    ''',
    placeholder='Write your documentation here...'
)
```

### With Callbacks for Real-time Processing

```python
from dash import Dash, html, callback, Input, Output, State
import dash_copilotkit_components

app = Dash(__name__)

app.layout = html.Div([
    dash_copilotkit_components.DashCopilotkitComponents(
        id='smart-textarea',
        ui_type='textarea',
        public_api_key='your-api-key',
        placeholder='Start typing...'
    ),
    
    html.Div([
        html.H4("Live Statistics:"),
        html.P(id="word-count"),
        html.P(id="char-count"),
        html.P(id="reading-time")
    ])
])

@callback(
    [Output('word-count', 'children'),
     Output('char-count', 'children'),
     Output('reading-time', 'children')],
    Input('smart-textarea', 'value')
)
def update_stats(value):
    if not value:
        return "Words: 0", "Characters: 0", "Reading time: 0 min"
    
    words = len(value.split())
    chars = len(value)
    reading_time = max(1, words // 200)  # Assume 200 words per minute
    
    return (
        f"Words: {words}",
        f"Characters: {chars}",
        f"Reading time: {reading_time} min"
    )
```

## Use Cases

### Content Management Systems
Help users create better blog posts, articles, and web content.

### Email Platforms
Assist with professional email composition and communication.

### Documentation Tools
Support technical writers with clear, structured documentation.

### Educational Platforms
Help students improve their writing skills and assignments.

### Customer Support
Assist support agents in crafting better responses to customers.

### Social Media Management
Help create engaging posts and captions for social platforms.

## Integration Patterns

### Form Integration

```python
from dash import Dash, html, dbc, callback, Input, Output, State
import dash_copilotkit_components

app = Dash(__name__)

app.layout = dbc.Container([
    dbc.Form([
        dbc.Row([
            dbc.Label("Subject", html_for="subject", width=2),
            dbc.Col([
                dbc.Input(id="subject", type="text", placeholder="Email subject")
            ], width=10)
        ], className="mb-3"),
        
        dbc.Row([
            dbc.Label("Message", html_for="message", width=2),
            dbc.Col([
                dash_copilotkit_components.DashCopilotkitComponents(
                    id='message-textarea',
                    ui_type='textarea',
                    public_api_key='your-api-key',
                    instructions='Help write professional emails',
                    placeholder='Write your message here...'
                )
            ], width=10)
        ], className="mb-3"),
        
        dbc.Button("Send Email", color="primary", id="send-btn")
    ])
])
```

### Multi-step Content Creation

```python
app.layout = html.Div([
    dcc.Tabs(id="content-tabs", value="outline", children=[
        dcc.Tab(label="Outline", value="outline"),
        dcc.Tab(label="Draft", value="draft"),
        dcc.Tab(label="Review", value="review")
    ]),
    
    html.Div(id="tab-content")
])

@callback(
    Output('tab-content', 'children'),
    Input('content-tabs', 'value')
)
def render_tab(active_tab):
    if active_tab == "outline":
        return dash_copilotkit_components.DashCopilotkitComponents(
            id='outline-textarea',
            ui_type='textarea',
            public_api_key='your-api-key',
            instructions='Help create article outlines and structure',
            placeholder='Create your article outline...'
        )
    elif active_tab == "draft":
        return dash_copilotkit_components.DashCopilotkitComponents(
            id='draft-textarea',
            ui_type='textarea',
            public_api_key='your-api-key',
            instructions='Help write engaging article content',
            placeholder='Write your article draft...'
        )
    # ... etc
```

## Best Practices

1. **Clear Instructions**: Provide specific, contextual instructions for the AI
2. **Appropriate Placeholder**: Use descriptive placeholder text
3. **Value Management**: Use callbacks to track and process text changes
4. **User Feedback**: Provide visual feedback during AI processing
5. **Error Handling**: Handle cases where AI assistance is unavailable

## Styling Tips

### Custom Textarea Styling

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='styled-textarea',
    ui_type='textarea',
    public_api_key='your-api-key',
    className='custom-textarea',
    style={
        'minHeight': '200px',
        'border': '2px solid #e0e0e0',
        'borderRadius': '8px',
        'padding': '12px',
        'fontSize': '16px',
        'lineHeight': '1.5'
    }
)
```

### CSS for Enhanced Appearance

```css
.custom-textarea {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    transition: border-color 0.2s ease;
}

.custom-textarea:focus {
    border-color: #007bff;
    box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.1);
    outline: none;
}

.custom-textarea::placeholder {
    color: #6c757d;
    font-style: italic;
}
```

## Troubleshooting

### Common Issues

**AI suggestions not appearing:**
- Verify API key is correct and active
- Check network connectivity
- Ensure instructions are clear and specific

**Textarea not updating:**
- Check callback connections
- Verify component ID matches
- Ensure proper value prop handling

**Styling not applied:**
- Check CSS syntax and selectors
- Verify className prop is set
- Use browser dev tools to debug

## Examples

See the [Examples section](../examples/basic.md) for more detailed code examples and integration patterns.
