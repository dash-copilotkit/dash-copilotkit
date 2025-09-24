# Advanced Examples

Complex integration patterns and advanced use cases for Dash CopilotKit Components.

## Dynamic Component Configuration

### Context-Aware Assistant

```python
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash_copilotkit_components

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Context-Aware AI Assistant"),
    
    dbc.Row([
        dbc.Col([
            html.H3("Current Context"),
            dcc.Dropdown(
                id='context-selector',
                options=[
                    {'label': 'E-commerce Store', 'value': 'ecommerce'},
                    {'label': 'Technical Documentation', 'value': 'technical'},
                    {'label': 'Customer Support', 'value': 'support'},
                    {'label': 'Educational Platform', 'value': 'education'}
                ],
                value='ecommerce'
            ),
            
            html.Div(id='context-info', className="mt-3")
        ], md=4),
        
        dbc.Col([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='context-aware-chat',
                ui_type='chat',
                public_api_key='your-copilotkit-cloud-api-key',
                height='500px'
            )
        ], md=8)
    ])
])

@callback(
    [Output('context-aware-chat', 'instructions'),
     Output('context-aware-chat', 'labels'),
     Output('context-info', 'children')],
    Input('context-selector', 'value')
)
def update_context(context):
    contexts = {
        'ecommerce': {
            'instructions': '''
            You are a helpful e-commerce assistant. Help customers with:
            - Product recommendations and comparisons
            - Order status and shipping information
            - Return and refund policies
            - Payment and checkout assistance
            - Size guides and product specifications
            ''',
            'labels': {
                'title': 'Shopping Assistant',
                'initial': 'Welcome! I can help you find products, track orders, and answer any shopping questions.'
            },
            'info': 'E-commerce context: Product recommendations, order support, shopping assistance'
        },
        'technical': {
            'instructions': '''
            You are a technical documentation assistant. Help users with:
            - API documentation and code examples
            - Troubleshooting technical issues
            - Best practices and implementation guides
            - Architecture and design patterns
            - Performance optimization tips
            ''',
            'labels': {
                'title': 'Technical Assistant',
                'initial': 'Hi! I can help you with technical documentation, APIs, and implementation questions.'
            },
            'info': 'Technical context: API docs, troubleshooting, code examples, best practices'
        },
        'support': {
            'instructions': '''
            You are a customer support specialist. Help customers with:
            - Account issues and billing questions
            - Technical troubleshooting
            - Feature explanations and tutorials
            - Escalation to human agents when needed
            - Feedback collection and issue resolution
            ''',
            'labels': {
                'title': 'Customer Support',
                'initial': 'Hello! I\'m here to help resolve any issues or questions you might have.'
            },
            'info': 'Support context: Issue resolution, account help, technical troubleshooting'
        },
        'education': {
            'instructions': '''
            You are an educational assistant. Help students with:
            - Explaining complex concepts clearly
            - Providing study tips and learning strategies
            - Answering homework and assignment questions
            - Recommending additional resources
            - Encouraging and motivating learners
            ''',
            'labels': {
                'title': 'Learning Assistant',
                'initial': 'Hi there! I\'m here to help you learn and understand new concepts. What can I explain for you?'
            },
            'info': 'Educational context: Concept explanations, study help, learning resources'
        }
    }
    
    config = contexts.get(context, contexts['ecommerce'])
    return config['instructions'], config['labels'], dbc.Alert(config['info'], color="info")

if __name__ == '__main__':
    app.run(debug=True)
```

## Multi-Modal Interface

### Combined Chat and Textarea Workflow

```python
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash_copilotkit_components

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("AI-Powered Content Creation Suite"),
    
    dbc.Row([
        dbc.Col([
            html.H3("Content Planning Chat"),
            dash_copilotkit_components.DashCopilotkitComponents(
                id='planning-chat',
                ui_type='chat',
                public_api_key='your-copilotkit-cloud-api-key',
                instructions='''
                You are a content planning assistant. Help users:
                - Brainstorm content ideas and topics
                - Create content outlines and structures
                - Develop content strategies
                - Plan content calendars
                - Research target audiences
                ''',
                labels={
                    'title': 'Content Planner',
                    'initial': 'Let\'s plan some amazing content! What type of content are you looking to create?'
                },
                height='400px'
            ),
            
            dbc.Button("Apply Chat Suggestions", id="apply-suggestions-btn", color="primary", className="mt-2")
        ], md=6),
        
        dbc.Col([
            html.H3("Content Writing"),
            dash_copilotkit_components.DashCopilotkitComponents(
                id='writing-textarea',
                ui_type='textarea',
                public_api_key='your-copilotkit-cloud-api-key',
                instructions='''
                You are a professional content writer. Help create:
                - Engaging and well-structured content
                - Clear and compelling copy
                - SEO-optimized text
                - Brand-appropriate tone and style
                - Error-free grammar and spelling
                ''',
                placeholder='Start writing your content here...',
                height='400px'
            ),
            
            html.Div(id='content-analysis', className="mt-3")
        ], md=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("Content Review and Feedback"),
            dash_copilotkit_components.DashCopilotkitComponents(
                id='review-sidebar',
                ui_type='sidebar',
                public_api_key='your-copilotkit-cloud-api-key',
                position='right',
                instructions='''
                You are a content editor and reviewer. Provide feedback on:
                - Content quality and clarity
                - Structure and organization
                - Tone and style consistency
                - SEO optimization opportunities
                - Areas for improvement
                ''',
                labels={
                    'title': 'Content Reviewer',
                    'initial': 'I can review your content and provide detailed feedback for improvement.'
                },
                width='400px'
            )
        ])
    ], className="mt-4")
])

@callback(
    Output('content-analysis', 'children'),
    Input('writing-textarea', 'value')
)
def analyze_content(content):
    if not content:
        return dbc.Alert("Start writing to see content analysis", color="info")
    
    words = len(content.split())
    chars = len(content)
    paragraphs = len([p for p in content.split('\n\n') if p.strip()])
    
    # Simple readability score (Flesch Reading Ease approximation)
    sentences = len([s for s in content.replace('!', '.').replace('?', '.').split('.') if s.strip()])
    if sentences > 0 and words > 0:
        avg_sentence_length = words / sentences
        readability = max(0, min(100, 206.835 - (1.015 * avg_sentence_length)))
    else:
        readability = 0
    
    return dbc.Card([
        dbc.CardBody([
            html.H5("Content Analysis", className="card-title"),
            html.P(f"Words: {words}"),
            html.P(f"Characters: {chars}"),
            html.P(f"Paragraphs: {paragraphs}"),
            html.P(f"Reading time: {max(1, words // 200)} min"),
            html.P(f"Readability score: {readability:.1f}/100"),
            dbc.Progress(value=readability, color="success" if readability > 60 else "warning")
        ])
    ])

if __name__ == '__main__':
    app.run(debug=True)
```

## Real-time Collaboration

### Shared Document Editor

```python
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash_copilotkit_components
import json
from datetime import datetime

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Simulated shared state (in production, use Redis or database)
shared_document = {
    'content': '',
    'last_modified': None,
    'collaborators': []
}

app.layout = dbc.Container([
    html.H1("Collaborative Document Editor"),
    
    dbc.Row([
        dbc.Col([
            html.H3("Document Editor"),
            dash_copilotkit_components.DashCopilotkitComponents(
                id='collaborative-textarea',
                ui_type='textarea',
                public_api_key='your-copilotkit-cloud-api-key',
                instructions='''
                You are a collaborative writing assistant. Help with:
                - Improving document structure and flow
                - Suggesting better word choices and phrasing
                - Maintaining consistency across sections
                - Collaborative editing best practices
                - Version control and change tracking
                ''',
                placeholder='Start collaborating on this document...',
                height='400px'
            ),
            
            dbc.ButtonGroup([
                dbc.Button("Save", id="save-btn", color="primary"),
                dbc.Button("Load", id="load-btn", color="secondary"),
                dbc.Button("Clear", id="clear-btn", color="danger")
            ], className="mt-2")
        ], md=8),
        
        dbc.Col([
            html.H3("Collaboration Assistant"),
            dash_copilotkit_components.DashCopilotkitComponents(
                id='collaboration-chat',
                ui_type='chat',
                public_api_key='your-copilotkit-cloud-api-key',
                instructions='''
                You are a collaboration facilitator. Help teams:
                - Coordinate editing tasks and responsibilities
                - Resolve conflicts in document changes
                - Suggest workflow improvements
                - Track document progress and milestones
                - Facilitate team communication
                ''',
                labels={
                    'title': 'Collaboration Assistant',
                    'initial': 'I can help coordinate your team\'s collaborative editing. What do you need help with?'
                },
                height='400px'
            ),
            
            html.Div(id='collaboration-status', className="mt-3")
        ], md=4)
    ]),
    
    # Hidden div to store document state
    dcc.Store(id='document-store', data=shared_document)
])

@callback(
    Output('document-store', 'data'),
    [Input('save-btn', 'n_clicks'),
     Input('clear-btn', 'n_clicks')],
    [State('collaborative-textarea', 'value'),
     State('document-store', 'data')]
)
def manage_document(save_clicks, clear_clicks, content, current_doc):
    ctx = dash.callback_context
    if not ctx.triggered:
        return current_doc
    
    trigger = ctx.triggered[0]['prop_id']
    
    if 'save-btn' in trigger and save_clicks:
        current_doc['content'] = content or ''
        current_doc['last_modified'] = datetime.now().isoformat()
        return current_doc
    elif 'clear-btn' in trigger and clear_clicks:
        return {'content': '', 'last_modified': None, 'collaborators': []}
    
    return current_doc

@callback(
    [Output('collaborative-textarea', 'value'),
     Output('collaboration-status', 'children')],
    [Input('load-btn', 'n_clicks'),
     Input('document-store', 'data')]
)
def update_document_view(load_clicks, doc_data):
    status_info = []
    
    if doc_data.get('last_modified'):
        status_info.append(html.P(f"Last saved: {doc_data['last_modified'][:19]}"))
    
    if doc_data.get('content'):
        word_count = len(doc_data['content'].split())
        status_info.append(html.P(f"Document length: {word_count} words"))
    
    status_card = dbc.Card([
        dbc.CardBody([
            html.H5("Document Status"),
            *status_info
        ])
    ]) if status_info else dbc.Alert("No document loaded", color="info")
    
    return doc_data.get('content', ''), status_card

if __name__ == '__main__':
    app.run(debug=True)
```

## Advanced Analytics Integration

### AI-Powered Data Analysis

```python
import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import dash_copilotkit_components
import plotly.express as px
import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=100, freq='D')
data = pd.DataFrame({
    'date': dates,
    'sales': np.random.normal(1000, 200, 100).cumsum(),
    'visitors': np.random.normal(500, 100, 100),
    'conversion_rate': np.random.normal(0.05, 0.01, 100)
})

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("AI-Powered Analytics Dashboard"),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='sales-chart',
                figure=px.line(data, x='date', y='sales', title='Sales Over Time')
            )
        ], md=6),
        
        dbc.Col([
            dcc.Graph(
                id='visitors-chart',
                figure=px.bar(data.tail(30), x='date', y='visitors', title='Recent Visitors')
            )
        ], md=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='conversion-chart',
                figure=px.scatter(data, x='visitors', y='conversion_rate', 
                                title='Conversion Rate vs Visitors')
            )
        ], md=8),
        
        dbc.Col([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='analytics-assistant',
                ui_type='sidebar',
                public_api_key='your-copilotkit-cloud-api-key',
                position='right',
                instructions=f'''
                You are an analytics expert assistant. Help users understand this dashboard data:
                
                Current Data Summary:
                - Total Sales: ${data['sales'].iloc[-1]:,.2f}
                - Average Daily Visitors: {data['visitors'].mean():.0f}
                - Average Conversion Rate: {data['conversion_rate'].mean():.2%}
                - Data Period: {data['date'].min().strftime('%Y-%m-%d')} to {data['date'].max().strftime('%Y-%m-%d')}
                
                Help with:
                - Interpreting trends and patterns in the data
                - Identifying opportunities for improvement
                - Explaining statistical concepts and metrics
                - Suggesting actionable insights
                - Answering questions about the visualizations
                ''',
                labels={
                    'title': 'Analytics Expert',
                    'initial': 'I can help you understand and analyze your dashboard data. What insights are you looking for?'
                },
                width='400px',
                show_initially=True
            )
        ], md=4)
    ], className="mt-4")
])

if __name__ == '__main__':
    app.run(debug=True)
```

## Custom Workflow Integration

### Task Management with AI

```python
import dash
from dash import html, dcc, callback, Input, Output, State, ALL
import dash_bootstrap_components as dbc
import dash_copilotkit_components
from datetime import datetime, timedelta
import uuid

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample tasks
initial_tasks = [
    {'id': str(uuid.uuid4()), 'title': 'Review project proposal', 'status': 'pending', 'priority': 'high'},
    {'id': str(uuid.uuid4()), 'title': 'Update documentation', 'status': 'in_progress', 'priority': 'medium'},
    {'id': str(uuid.uuid4()), 'title': 'Schedule team meeting', 'status': 'completed', 'priority': 'low'}
]

app.layout = dbc.Container([
    html.H1("AI-Powered Task Management"),
    
    dbc.Row([
        dbc.Col([
            html.H3("Task List"),
            html.Div(id='task-list'),
            
            dbc.Card([
                dbc.CardBody([
                    html.H5("Add New Task"),
                    dbc.Input(id='new-task-input', placeholder='Enter task description...'),
                    dbc.Button("Add Task", id='add-task-btn', color="primary", className="mt-2")
                ])
            ], className="mt-3")
        ], md=6),
        
        dbc.Col([
            html.H3("AI Task Assistant"),
            dash_copilotkit_components.DashCopilotkitComponents(
                id='task-assistant',
                ui_type='chat',
                public_api_key='your-copilotkit-cloud-api-key',
                instructions='''
                You are a productivity and task management assistant. Help users:
                - Prioritize tasks based on importance and urgency
                - Break down complex tasks into smaller steps
                - Suggest time estimates for task completion
                - Recommend task scheduling and organization
                - Provide productivity tips and best practices
                - Help with project planning and milestone setting
                ''',
                labels={
                    'title': 'Task Assistant',
                    'initial': 'Hi! I can help you manage your tasks more effectively. What would you like help with?'
                },
                height='500px'
            )
        ], md=6)
    ]),
    
    # Store for tasks
    dcc.Store(id='tasks-store', data=initial_tasks)
])

@callback(
    Output('task-list', 'children'),
    Input('tasks-store', 'data')
)
def render_task_list(tasks):
    if not tasks:
        return dbc.Alert("No tasks yet. Add some tasks to get started!", color="info")
    
    task_cards = []
    for task in tasks:
        color = {
            'completed': 'success',
            'in_progress': 'warning',
            'pending': 'light'
        }.get(task['status'], 'light')
        
        priority_badge = dbc.Badge(
            task['priority'].title(),
            color={'high': 'danger', 'medium': 'warning', 'low': 'info'}.get(task['priority'], 'secondary')
        )
        
        task_cards.append(
            dbc.Card([
                dbc.CardBody([
                    html.H6([task['title'], " ", priority_badge]),
                    html.P(f"Status: {task['status'].replace('_', ' ').title()}", className="text-muted"),
                    dbc.ButtonGroup([
                        dbc.Button("Complete", size="sm", color="success", 
                                 id={'type': 'complete-btn', 'index': task['id']}),
                        dbc.Button("Delete", size="sm", color="danger",
                                 id={'type': 'delete-btn', 'index': task['id']})
                    ])
                ])
            ], color=color, outline=True, className="mb-2")
        )
    
    return task_cards

@callback(
    Output('tasks-store', 'data'),
    [Input('add-task-btn', 'n_clicks'),
     Input({'type': 'complete-btn', 'index': ALL}, 'n_clicks'),
     Input({'type': 'delete-btn', 'index': ALL}, 'n_clicks')],
    [State('new-task-input', 'value'),
     State('tasks-store', 'data')]
)
def manage_tasks(add_clicks, complete_clicks, delete_clicks, new_task, current_tasks):
    ctx = dash.callback_context
    if not ctx.triggered:
        return current_tasks
    
    trigger = ctx.triggered[0]
    
    if 'add-task-btn' in trigger['prop_id'] and add_clicks and new_task:
        new_task_obj = {
            'id': str(uuid.uuid4()),
            'title': new_task,
            'status': 'pending',
            'priority': 'medium'
        }
        return current_tasks + [new_task_obj]
    
    elif 'complete-btn' in trigger['prop_id']:
        task_id = eval(trigger['prop_id'].split('.')[0])['index']
        for task in current_tasks:
            if task['id'] == task_id:
                task['status'] = 'completed'
        return current_tasks
    
    elif 'delete-btn' in trigger['prop_id']:
        task_id = eval(trigger['prop_id'].split('.')[0])['index']
        return [task for task in current_tasks if task['id'] != task_id]
    
    return current_tasks

if __name__ == '__main__':
    app.run(debug=True)
```

## Next Steps

- [Integration Examples](integration.md) - Integration with external services
- [Styling Examples](styling.md) - Advanced styling and theming
- [API Reference](../api/props.md) - Complete API documentation
