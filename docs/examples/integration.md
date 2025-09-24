# Integration Examples

Examples of integrating Dash CopilotKit Components with external services and libraries.

## Database Integration

### SQLite Integration

```python
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash_copilotkit_components
import sqlite3
import pandas as pd
from datetime import datetime

# Initialize database
def init_db():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_message TEXT,
            ai_response TEXT,
            session_id TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Chat with Database Integration"),
    
    dbc.Row([
        dbc.Col([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='db-integrated-chat',
                ui_type='chat',
                public_api_key='your-copilotkit-cloud-api-key',
                instructions='''
                You are a helpful assistant with access to conversation history.
                You can reference previous conversations and maintain context.
                ''',
                height='500px'
            )
        ], md=8),
        
        dbc.Col([
            html.H4("Conversation History"),
            html.Div(id='conversation-history'),
            dbc.Button("Clear History", id="clear-history-btn", color="danger", size="sm")
        ], md=4)
    ])
])

@callback(
    Output('conversation-history', 'children'),
    [Input('db-integrated-chat', 'value'),
     Input('clear-history-btn', 'n_clicks')]
)
def update_history(chat_value, clear_clicks):
    if clear_clicks:
        conn = sqlite3.connect('chat_history.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM conversations')
        conn.commit()
        conn.close()
        return dbc.Alert("History cleared", color="info")
    
    # Fetch recent conversations
    conn = sqlite3.connect('chat_history.db')
    df = pd.read_sql_query(
        'SELECT * FROM conversations ORDER BY timestamp DESC LIMIT 10',
        conn
    )
    conn.close()
    
    if df.empty:
        return dbc.Alert("No conversation history yet", color="info")
    
    history_items = []
    for _, row in df.iterrows():
        history_items.append(
            dbc.Card([
                dbc.CardBody([
                    html.Small(row['timestamp'], className="text-muted"),
                    html.P(f"User: {row['user_message'][:50]}...", className="mb-1"),
                    html.P(f"AI: {row['ai_response'][:50]}...", className="mb-0 text-muted")
                ])
            ], className="mb-2")
        )
    
    return history_items

if __name__ == '__main__':
    app.run(debug=True)
```

## API Integration

### REST API Integration

```python
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash_copilotkit_components
import requests
import json

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Weather Assistant with API Integration"),
    
    dbc.Row([
        dbc.Col([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='weather-assistant',
                ui_type='chat',
                public_api_key='your-copilotkit-cloud-api-key',
                instructions='''
                You are a weather assistant with access to real-time weather data.
                Help users with weather information, forecasts, and weather-related advice.
                You can access current weather data for any city.
                ''',
                labels={
                    'title': 'Weather Assistant',
                    'initial': 'Hi! I can help you with weather information. What city would you like to know about?'
                },
                height='500px'
            )
        ], md=8),
        
        dbc.Col([
            html.H4("Weather Data"),
            html.Div(id='weather-display'),
            
            html.Hr(),
            
            html.H5("Quick Weather Check"),
            dbc.InputGroup([
                dbc.Input(id="city-input", placeholder="Enter city name"),
                dbc.Button("Get Weather", id="get-weather-btn", color="primary")
            ]),
            
            html.Div(id='quick-weather', className="mt-3")
        ], md=4)
    ])
])

def get_weather_data(city):
    """Fetch weather data from OpenWeatherMap API"""
    # Replace with your OpenWeatherMap API key
    api_key = "your-openweathermap-api-key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

@callback(
    Output('quick-weather', 'children'),
    Input('get-weather-btn', 'n_clicks'),
    State('city-input', 'value')
)
def display_weather(n_clicks, city):
    if not n_clicks or not city:
        return ""
    
    weather_data = get_weather_data(city)
    
    if not weather_data:
        return dbc.Alert("Could not fetch weather data", color="danger")
    
    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    
    return dbc.Card([
        dbc.CardBody([
            html.H5(f"Weather in {city.title()}"),
            html.P(f"Temperature: {temp}°C"),
            html.P(f"Condition: {description.title()}"),
            html.P(f"Humidity: {humidity}%")
        ])
    ])

if __name__ == '__main__':
    app.run(debug=True)
```

## File Upload Integration

### Document Analysis with File Upload

```python
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash_copilotkit_components
import base64
import io
import PyPDF2
import docx

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Document Analysis Assistant"),
    
    dbc.Row([
        dbc.Col([
            dcc.Upload(
                id='upload-document',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                multiple=False
            ),
            
            html.Div(id='file-info'),
            
            dash_copilotkit_components.DashCopilotkitComponents(
                id='document-assistant',
                ui_type='chat',
                public_api_key='your-copilotkit-cloud-api-key',
                instructions='''
                You are a document analysis assistant. Help users:
                - Analyze and summarize uploaded documents
                - Extract key information and insights
                - Answer questions about document content
                - Provide document structure analysis
                - Suggest improvements or actions based on content
                ''',
                labels={
                    'title': 'Document Analyzer',
                    'initial': 'Upload a document and I\'ll help you analyze it!'
                },
                height='400px'
            )
        ], md=8),
        
        dbc.Col([
            html.H4("Document Summary"),
            html.Div(id='document-summary')
        ], md=4)
    ])
])

def parse_document(contents, filename):
    """Parse uploaded document and extract text"""
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    
    try:
        if filename.endswith('.pdf'):
            # Parse PDF
            pdf_file = io.BytesIO(decoded)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        
        elif filename.endswith('.docx'):
            # Parse DOCX
            doc_file = io.BytesIO(decoded)
            doc = docx.Document(doc_file)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text
        
        elif filename.endswith('.txt'):
            # Parse TXT
            return decoded.decode('utf-8')
        
        else:
            return "Unsupported file format"
    
    except Exception as e:
        return f"Error parsing document: {str(e)}"

@callback(
    [Output('file-info', 'children'),
     Output('document-summary', 'children'),
     Output('document-assistant', 'instructions')],
    Input('upload-document', 'contents'),
    State('upload-document', 'filename')
)
def process_uploaded_file(contents, filename):
    if contents is None:
        return "", "", "You are a document analysis assistant."
    
    # Parse document
    document_text = parse_document(contents, filename)
    
    # Create file info
    file_info = dbc.Alert(f"Uploaded: {filename}", color="success")
    
    # Create summary
    word_count = len(document_text.split())
    char_count = len(document_text)
    
    summary = dbc.Card([
        dbc.CardBody([
            html.H5("Document Stats"),
            html.P(f"File: {filename}"),
            html.P(f"Words: {word_count:,}"),
            html.P(f"Characters: {char_count:,}"),
            html.P(f"Preview: {document_text[:200]}...")
        ])
    ])
    
    # Update assistant instructions with document content
    enhanced_instructions = f'''
    You are a document analysis assistant with access to the following document:
    
    Filename: {filename}
    Content: {document_text[:2000]}...
    
    Help users analyze this document by:
    - Summarizing key points and themes
    - Answering questions about the content
    - Extracting important information
    - Providing insights and analysis
    - Suggesting actions based on the content
    '''
    
    return file_info, summary, enhanced_instructions

if __name__ == '__main__':
    app.run(debug=True)
```

## Real-time Data Integration

### Stock Market Assistant

```python
import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import dash_copilotkit_components
import plotly.graph_objs as go
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Stock Market Assistant"),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='stock-chart'),
            
            dbc.InputGroup([
                dbc.Input(id="stock-symbol", placeholder="Enter stock symbol (e.g., AAPL)", value="AAPL"),
                dbc.Button("Update Chart", id="update-chart-btn", color="primary")
            ], className="mt-3")
        ], md=8),
        
        dbc.Col([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='stock-assistant',
                ui_type='sidebar',
                public_api_key='your-copilotkit-cloud-api-key',
                position='right',
                instructions='''
                You are a stock market analysis assistant with access to real-time stock data.
                Help users with:
                - Stock price analysis and trends
                - Market insights and explanations
                - Investment education and guidance
                - Risk assessment and portfolio advice
                - Technical analysis interpretation
                
                Current stock data will be provided in context.
                ''',
                labels={
                    'title': 'Stock Advisor',
                    'initial': 'I can help you analyze stocks and understand market trends. What would you like to know?'
                },
                width='400px',
                show_initially=True
            )
        ], md=4)
    ]),
    
    # Store for stock data
    dcc.Store(id='stock-data-store')
])

@callback(
    [Output('stock-chart', 'figure'),
     Output('stock-data-store', 'data'),
     Output('stock-assistant', 'instructions')],
    [Input('update-chart-btn', 'n_clicks')],
    [dash.State('stock-symbol', 'value')]
)
def update_stock_data(n_clicks, symbol):
    if not symbol:
        symbol = 'AAPL'
    
    try:
        # Fetch stock data
        stock = yf.Ticker(symbol.upper())
        hist = stock.history(period="1mo")
        info = stock.info
        
        # Create chart
        fig = go.Figure()
        fig.add_trace(go.Candlestick(
            x=hist.index,
            open=hist['Open'],
            high=hist['High'],
            low=hist['Low'],
            close=hist['Close'],
            name=symbol.upper()
        ))
        
        fig.update_layout(
            title=f'{symbol.upper()} Stock Price (Last 30 Days)',
            yaxis_title='Price ($)',
            xaxis_title='Date',
            height=400
        )
        
        # Prepare data for assistant
        current_price = hist['Close'].iloc[-1]
        price_change = hist['Close'].iloc[-1] - hist['Close'].iloc[-2]
        percent_change = (price_change / hist['Close'].iloc[-2]) * 100
        
        stock_data = {
            'symbol': symbol.upper(),
            'current_price': current_price,
            'price_change': price_change,
            'percent_change': percent_change,
            'volume': hist['Volume'].iloc[-1],
            'market_cap': info.get('marketCap', 'N/A'),
            'pe_ratio': info.get('trailingPE', 'N/A')
        }
        
        # Enhanced instructions with current data
        enhanced_instructions = f'''
        You are a stock market analysis assistant with access to current stock data for {symbol.upper()}:
        
        Current Stock Information:
        - Symbol: {symbol.upper()}
        - Current Price: ${current_price:.2f}
        - Price Change: ${price_change:.2f} ({percent_change:.2f}%)
        - Volume: {stock_data['volume']:,}
        - Market Cap: {stock_data['market_cap']}
        - P/E Ratio: {stock_data['pe_ratio']}
        
        Help users with:
        - Analysis of this stock's performance
        - Market trends and insights
        - Investment education and guidance
        - Risk assessment and portfolio advice
        - Technical analysis interpretation
        
        Always provide educational content and remind users that this is not financial advice.
        '''
        
        return fig, stock_data, enhanced_instructions
    
    except Exception as e:
        # Return empty chart and error message
        fig = go.Figure()
        fig.add_annotation(text=f"Error loading data for {symbol}", 
                          xref="paper", yref="paper", x=0.5, y=0.5)
        
        return fig, {}, "You are a stock market assistant. Please enter a valid stock symbol."

if __name__ == '__main__':
    app.run(debug=True)
```

## Authentication Integration

### User Authentication with Sessions

```python
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash_copilotkit_components
import hashlib
import secrets
from datetime import datetime, timedelta

# Simple in-memory user store (use database in production)
users_db = {
    'demo@example.com': {
        'password_hash': hashlib.sha256('password123'.encode()).hexdigest(),
        'name': 'Demo User',
        'role': 'user'
    },
    'admin@example.com': {
        'password_hash': hashlib.sha256('admin123'.encode()).hexdigest(),
        'name': 'Admin User',
        'role': 'admin'
    }
}

sessions = {}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

def create_login_layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H3("Login", className="text-center mb-4"),
                        dbc.Form([
                            dbc.Row([
                                dbc.Label("Email", width=3),
                                dbc.Col([
                                    dbc.Input(id="login-email", type="email", placeholder="Enter email")
                                ], width=9)
                            ], className="mb-3"),
                            
                            dbc.Row([
                                dbc.Label("Password", width=3),
                                dbc.Col([
                                    dbc.Input(id="login-password", type="password", placeholder="Enter password")
                                ], width=9)
                            ], className="mb-3"),
                            
                            dbc.Button("Login", id="login-btn", color="primary", className="w-100")
                        ]),
                        
                        html.Div(id="login-message", className="mt-3"),
                        
                        html.Hr(),
                        html.P("Demo credentials:", className="text-muted"),
                        html.P("User: demo@example.com / password123", className="small text-muted"),
                        html.P("Admin: admin@example.com / admin123", className="small text-muted")
                    ])
                ])
            ], md=6, className="mx-auto")
        ], className="mt-5")
    ])

def create_dashboard_layout(user_info):
    return dbc.Container([
        dbc.Navbar([
            dbc.NavbarBrand(f"Welcome, {user_info['name']}"),
            dbc.Nav([
                dbc.Button("Logout", id="logout-btn", color="outline-light", size="sm")
            ], className="ms-auto")
        ], color="primary", dark=True, className="mb-4"),
        
        dbc.Row([
            dbc.Col([
                html.H2("Personalized AI Assistant"),
                dash_copilotkit_components.DashCopilotkitComponents(
                    id='personalized-assistant',
                    ui_type='chat',
                    public_api_key='your-copilotkit-cloud-api-key',
                    instructions=f'''
                    You are a personalized assistant for {user_info['name']} (Role: {user_info['role']}).
                    
                    User Profile:
                    - Name: {user_info['name']}
                    - Role: {user_info['role']}
                    - Access Level: {'Full access' if user_info['role'] == 'admin' else 'Standard access'}
                    
                    Provide personalized assistance based on their role and preferences.
                    {'You have administrative privileges and can help with system management.' if user_info['role'] == 'admin' else 'You have standard user access.'}
                    ''',
                    labels={
                        'title': f"Personal Assistant for {user_info['name']}",
                        'initial': f"Hello {user_info['name']}! How can I help you today?"
                    },
                    height='500px'
                )
            ], md=8),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("User Profile"),
                        html.P(f"Name: {user_info['name']}"),
                        html.P(f"Role: {user_info['role'].title()}"),
                        html.P(f"Login Time: {datetime.now().strftime('%H:%M:%S')}")
                    ])
                ])
            ], md=4)
        ])
    ])

app.layout = html.Div([
    dcc.Store(id='session-store'),
    html.Div(id='page-content')
])

@callback(
    [Output('page-content', 'children'),
     Output('session-store', 'data')],
    [Input('login-btn', 'n_clicks'),
     Input('logout-btn', 'n_clicks')],
    [State('login-email', 'value'),
     State('login-password', 'value'),
     State('session-store', 'data')]
)
def handle_auth(login_clicks, logout_clicks, email, password, session_data):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        return create_login_layout(), None
    
    trigger = ctx.triggered[0]['prop_id']
    
    if 'login-btn' in trigger and login_clicks:
        if email and password:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            
            if email in users_db and users_db[email]['password_hash'] == password_hash:
                # Create session
                session_id = secrets.token_urlsafe(32)
                sessions[session_id] = {
                    'user': users_db[email],
                    'email': email,
                    'login_time': datetime.now()
                }
                
                return create_dashboard_layout(users_db[email]), {'session_id': session_id}
            else:
                login_layout = create_login_layout()
                # Add error message (would need to modify layout to show this)
                return login_layout, None
        else:
            return create_login_layout(), None
    
    elif 'logout-btn' in trigger and logout_clicks:
        if session_data and session_data.get('session_id') in sessions:
            del sessions[session_data['session_id']]
        return create_login_layout(), None
    
    # Check existing session
    if session_data and session_data.get('session_id') in sessions:
        user_info = sessions[session_data['session_id']]['user']
        return create_dashboard_layout(user_info), session_data
    
    return create_login_layout(), None

if __name__ == '__main__':
    app.run(debug=True)
```

## Next Steps

- [Advanced Examples](advanced.md) - Complex integration patterns
- [API Reference](../api/props.md) - Complete API documentation
- [Deployment](../deployment/production.md) - Production deployment guide
