# Callbacks

Learn how to interact with Dash CopilotKit Components using Dash callbacks.

## Overview

Dash CopilotKit Components integrate seamlessly with Dash's callback system, allowing you to:

- React to user interactions
- Update component properties dynamically
- Process AI-generated content
- Create interactive workflows

## Available Callback Properties

### Input Properties

These properties can be used as `Input` in callbacks:

#### `value`
- **Type**: `string`
- **Description**: Current text content (primarily for textarea UI type)
- **Triggers**: When user types or AI modifies content
- **Example**:
  ```python
  @callback(
      Output('output', 'children'),
      Input('textarea-copilot', 'value')
  )
  def display_content(value):
      return f"Content: {value}"
  ```

### Output Properties

These properties can be updated via callbacks:

#### `value`
- **Type**: `string`
- **Description**: Set or update the text content
- **Example**:
  ```python
  @callback(
      Output('textarea-copilot', 'value'),
      Input('clear-button', 'n_clicks')
  )
  def clear_content(n_clicks):
      if n_clicks:
          return ""
      return dash.no_update
  ```

#### `disabled`
- **Type**: `boolean`
- **Description**: Enable or disable the component
- **Example**:
  ```python
  @callback(
      Output('chat-copilot', 'disabled'),
      Input('toggle-button', 'n_clicks')
  )
  def toggle_chat(n_clicks):
      return n_clicks % 2 == 1 if n_clicks else False
  ```

#### `instructions`
- **Type**: `string`
- **Description**: Update AI instructions dynamically
- **Example**:
  ```python
  @callback(
      Output('copilot', 'instructions'),
      Input('mode-dropdown', 'value')
  )
  def update_instructions(mode):
      instructions = {
          'support': 'You are a customer support assistant.',
          'sales': 'You are a sales assistant.',
          'technical': 'You are a technical support specialist.'
      }
      return instructions.get(mode, 'You are a helpful assistant.')
  ```

## Common Callback Patterns

### Real-time Content Processing

Monitor and process content as users type:

```python
from dash import Dash, html, callback, Input, Output
import dash_copilotkit_components

app = Dash(__name__)

app.layout = html.Div([
    dash_copilotkit_components.DashCopilotkitComponents(
        id='content-textarea',
        ui_type='textarea',
        public_api_key='your-api-key'
    ),
    
    html.Div([
        html.H4("Live Statistics"),
        html.P(id="word-count"),
        html.P(id="char-count"),
        html.P(id="sentiment")
    ])
])

@callback(
    [Output('word-count', 'children'),
     Output('char-count', 'children'),
     Output('sentiment', 'children')],
    Input('content-textarea', 'value')
)
def analyze_content(content):
    if not content:
        return "Words: 0", "Characters: 0", "Sentiment: Neutral"
    
    words = len(content.split())
    chars = len(content)
    
    # Simple sentiment analysis (you could use a real library)
    positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful']
    negative_words = ['bad', 'terrible', 'awful', 'horrible', 'disappointing']
    
    content_lower = content.lower()
    pos_count = sum(word in content_lower for word in positive_words)
    neg_count = sum(word in content_lower for word in negative_words)
    
    if pos_count > neg_count:
        sentiment = "Positive"
    elif neg_count > pos_count:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return f"Words: {words}", f"Characters: {chars}", f"Sentiment: {sentiment}"
```

### Dynamic Configuration

Update component settings based on user selections:

```python
from dash import Dash, html, dcc, callback, Input, Output
import dash_copilotkit_components

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='assistant-type',
        options=[
            {'label': 'Customer Support', 'value': 'support'},
            {'label': 'Technical Help', 'value': 'technical'},
            {'label': 'Sales Assistant', 'value': 'sales'}
        ],
        value='support'
    ),
    
    dash_copilotkit_components.DashCopilotkitComponents(
        id='dynamic-copilot',
        ui_type='chat',
        public_api_key='your-api-key'
    )
])

@callback(
    [Output('dynamic-copilot', 'instructions'),
     Output('dynamic-copilot', 'labels')],
    Input('assistant-type', 'value')
)
def update_assistant_config(assistant_type):
    configs = {
        'support': {
            'instructions': 'You are a friendly customer support assistant. Help users with their questions and issues.',
            'labels': {
                'title': 'Customer Support',
                'initial': 'Hi! How can I help you today?'
            }
        },
        'technical': {
            'instructions': 'You are a technical support specialist. Help users with technical issues and troubleshooting.',
            'labels': {
                'title': 'Technical Support',
                'initial': 'Hello! I can help you with technical issues.'
            }
        },
        'sales': {
            'instructions': 'You are a sales assistant. Help users learn about products and make purchasing decisions.',
            'labels': {
                'title': 'Sales Assistant',
                'initial': 'Welcome! How can I help you find the perfect product?'
            }
        }
    }
    
    config = configs.get(assistant_type, configs['support'])
    return config['instructions'], config['labels']
```

### Form Integration

Integrate with forms and validation:

```python
from dash import Dash, html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash_copilotkit_components

app = Dash(__name__)

app.layout = dbc.Container([
    dbc.Form([
        dbc.Row([
            dbc.Label("Email Subject", width=2),
            dbc.Col([
                dbc.Input(id="email-subject", type="text")
            ], width=10)
        ], className="mb-3"),
        
        dbc.Row([
            dbc.Label("Email Body", width=2),
            dbc.Col([
                dash_copilotkit_components.DashCopilotkitComponents(
                    id='email-body',
                    ui_type='textarea',
                    public_api_key='your-api-key',
                    instructions='Help write professional emails'
                )
            ], width=10)
        ], className="mb-3"),
        
        dbc.Button("Send Email", id="send-btn", color="primary"),
        html.Div(id="form-output")
    ])
])

@callback(
    Output('form-output', 'children'),
    Input('send-btn', 'n_clicks'),
    [State('email-subject', 'value'),
     State('email-body', 'value')]
)
def process_email(n_clicks, subject, body):
    if not n_clicks:
        return ""
    
    if not subject or not body:
        return dbc.Alert("Please fill in both subject and body", color="warning")
    
    # Process the email (send, save, etc.)
    return dbc.Alert(f"Email sent! Subject: {subject}", color="success")
```

### Multi-Component Coordination

Coordinate multiple CopilotKit components:

```python
from dash import Dash, html, callback, Input, Output, State
import dash_copilotkit_components

app = Dash(__name__)

app.layout = html.Div([
    html.H2("Content Creation Workflow"),
    
    html.H3("1. Create Outline"),
    dash_copilotkit_components.DashCopilotkitComponents(
        id='outline-textarea',
        ui_type='textarea',
        public_api_key='your-api-key',
        instructions='Help create article outlines',
        placeholder='Create your article outline...'
    ),
    
    html.Button("Generate Draft from Outline", id="generate-btn"),
    
    html.H3("2. Write Draft"),
    dash_copilotkit_components.DashCopilotkitComponents(
        id='draft-textarea',
        ui_type='textarea',
        public_api_key='your-api-key',
        instructions='Help write article content based on the outline',
        placeholder='Article draft will appear here...'
    ),
    
    html.H3("3. Get Feedback"),
    dash_copilotkit_components.DashCopilotkitComponents(
        id='feedback-chat',
        ui_type='chat',
        public_api_key='your-api-key',
        instructions='Provide feedback and suggestions for improving the article'
    )
])

@callback(
    Output('draft-textarea', 'value'),
    Input('generate-btn', 'n_clicks'),
    State('outline-textarea', 'value')
)
def generate_draft_from_outline(n_clicks, outline):
    if not n_clicks or not outline:
        return ""
    
    # In a real app, you might use the outline to generate a draft
    # For now, we'll just provide a template
    return f"Draft based on outline:\n\n{outline}\n\n[Content will be generated here...]"

@callback(
    Output('feedback-chat', 'instructions'),
    Input('draft-textarea', 'value')
)
def update_feedback_context(draft):
    if not draft:
        return "Provide feedback and suggestions for improving articles."
    
    return f"""
    Provide feedback and suggestions for improving this article draft:
    
    {draft[:500]}...
    
    Focus on:
    - Content structure and flow
    - Clarity and readability
    - Areas that need more detail
    - Suggestions for improvement
    """
```

## Advanced Patterns

### Conditional Component Updates

```python
@callback(
    [Output('copilot', 'disabled'),
     Output('copilot', 'instructions')],
    [Input('user-role', 'value'),
     Input('api-status', 'data')]
)
def update_based_on_conditions(user_role, api_status):
    # Disable if API is down
    if not api_status.get('available', True):
        return True, "Service temporarily unavailable"
    
    # Different instructions based on user role
    if user_role == 'admin':
        return False, "You are an admin assistant with full access"
    elif user_role == 'user':
        return False, "You are a user assistant with limited access"
    else:
        return True, "Please log in to use the assistant"
```

### Error Handling

```python
@callback(
    Output('error-display', 'children'),
    Input('copilot', 'value'),
    prevent_initial_call=True
)
def handle_errors(value):
    try:
        # Process the value
        if value and len(value) > 10000:
            return dbc.Alert("Content too long! Please keep under 10,000 characters.", color="warning")
        
        # Validate content
        if value and any(word in value.lower() for word in ['spam', 'inappropriate']):
            return dbc.Alert("Content contains inappropriate language.", color="danger")
        
        return ""  # No errors
        
    except Exception as e:
        return dbc.Alert(f"Error processing content: {str(e)}", color="danger")
```

## Best Practices

1. **Use `prevent_initial_call=True`** when you don't want callbacks to fire on page load
2. **Handle empty values** gracefully in your callbacks
3. **Use `dash.no_update`** when you don't want to update an output
4. **Validate inputs** before processing to avoid errors
5. **Provide user feedback** for long-running operations
6. **Use `State` instead of `Input`** when you don't want to trigger on every change

## Troubleshooting

### Common Issues

**Callback not firing:**
- Check that component IDs match exactly
- Ensure the component exists in the layout
- Verify the property name is correct

**Infinite callback loops:**
- Avoid updating the same property you're listening to
- Use `prevent_initial_call=True` when appropriate
- Check for circular dependencies

**Performance issues:**
- Use `State` instead of `Input` for frequently changing values
- Debounce user inputs when possible
- Avoid heavy computations in callbacks

## Next Steps

- [Styling](styling.md) - Learn about styling and theming
- [Examples](../examples/basic.md) - See callbacks in action
