# Performance Optimization

Guide for optimizing the performance of Dash CopilotKit Components applications.

## Performance Overview

Optimizing Dash applications with CopilotKit components involves several key areas:
- Component loading and rendering
- API call optimization
- Caching strategies
- Resource management
- Network optimization

## Component Optimization

### Lazy Loading Components

```python
import dash
from dash import html, dcc, callback, Input, Output
import dash_copilotkit_components

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Tabs(id="main-tabs", value="home", children=[
        dcc.Tab(label="Home", value="home"),
        dcc.Tab(label="Chat", value="chat"),
        dcc.Tab(label="Assistant", value="assistant")
    ]),
    html.Div(id="tab-content")
])

@callback(
    Output('tab-content', 'children'),
    Input('main-tabs', 'value')
)
def render_tab_content(active_tab):
    """Lazy load components only when needed"""
    if active_tab == "chat":
        return dash_copilotkit_components.DashCopilotkitComponents(
            id='lazy-chat',
            ui_type='chat',
            public_api_key='your-api-key',
            height='500px'
        )
    elif active_tab == "assistant":
        return dash_copilotkit_components.DashCopilotkitComponents(
            id='lazy-assistant',
            ui_type='sidebar',
            public_api_key='your-api-key',
            position='right'
        )
    else:
        return html.H2("Welcome to the Home Page")
```

### Component Pooling

```python
from typing import Dict, List
import dash_copilotkit_components

class ComponentPool:
    """Pool of reusable CopilotKit components"""
    
    def __init__(self, pool_size: int = 5):
        self.pool_size = pool_size
        self.available_components: List[str] = []
        self.active_components: Dict[str, dict] = {}
        self._initialize_pool()
    
    def _initialize_pool(self):
        """Initialize component pool"""
        for i in range(self.pool_size):
            component_id = f"pooled-component-{i}"
            self.available_components.append(component_id)
    
    def get_component(self, ui_type: str, **kwargs):
        """Get component from pool or create new one"""
        if self.available_components:
            component_id = self.available_components.pop()
            self.active_components[component_id] = kwargs
            
            return dash_copilotkit_components.DashCopilotkitComponents(
                id=component_id,
                ui_type=ui_type,
                **kwargs
            )
        else:
            # Pool exhausted, create new component
            import uuid
            component_id = f"overflow-component-{uuid.uuid4().hex[:8]}"
            return dash_copilotkit_components.DashCopilotkitComponents(
                id=component_id,
                ui_type=ui_type,
                **kwargs
            )
    
    def return_component(self, component_id: str):
        """Return component to pool"""
        if component_id in self.active_components:
            del self.active_components[component_id]
            if len(self.available_components) < self.pool_size:
                self.available_components.append(component_id)

# Global component pool
component_pool = ComponentPool()
```

## Caching Strategies

### Response Caching

```python
from flask_caching import Cache
import hashlib
import json

# Configure cache
cache = Cache(app.server, config={
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': 'redis://localhost:6379',
    'CACHE_DEFAULT_TIMEOUT': 300
})

def cache_key_generator(*args, **kwargs):
    """Generate cache key from arguments"""
    key_data = {
        'args': args,
        'kwargs': {k: v for k, v in kwargs.items() if k != 'n_clicks'}
    }
    key_string = json.dumps(key_data, sort_keys=True)
    return hashlib.md5(key_string.encode()).hexdigest()

@cache.memoize(timeout=300, make_name=cache_key_generator)
def expensive_ai_operation(prompt, context):
    """Cache expensive AI operations"""
    # Simulate expensive operation
    import time
    time.sleep(2)
    return f"AI response for: {prompt}"

@callback(
    Output('ai-response', 'children'),
    Input('submit-btn', 'n_clicks'),
    State('prompt-input', 'value')
)
def handle_ai_request(n_clicks, prompt):
    if not n_clicks or not prompt:
        return ""
    
    # Use cached response if available
    response = expensive_ai_operation(prompt, "context")
    return response
```

### Component State Caching

```python
import dash
from dash import dcc, callback, Input, Output, State
import json

app = dash.Dash(__name__)

# Client-side caching using dcc.Store
app.layout = html.Div([
    dcc.Store(id='component-cache', storage_type='session'),
    dcc.Store(id='user-preferences', storage_type='local'),
    
    dash_copilotkit_components.DashCopilotkitComponents(
        id='cached-copilot',
        ui_type='chat',
        public_api_key='your-api-key'
    )
])

@callback(
    Output('component-cache', 'data'),
    Input('cached-copilot', 'value'),
    State('component-cache', 'data')
)
def cache_component_state(value, cached_data):
    """Cache component state for session persistence"""
    if not cached_data:
        cached_data = {}
    
    cached_data['last_interaction'] = value
    cached_data['timestamp'] = datetime.now().isoformat()
    
    return cached_data
```

## API Optimization

### Request Batching

```python
import asyncio
import aiohttp
from typing import List, Dict
import json

class APIBatcher:
    """Batch API requests for better performance"""
    
    def __init__(self, batch_size: int = 10, batch_timeout: float = 1.0):
        self.batch_size = batch_size
        self.batch_timeout = batch_timeout
        self.pending_requests: List[Dict] = []
        self.batch_timer = None
    
    async def add_request(self, request_data: Dict):
        """Add request to batch"""
        self.pending_requests.append(request_data)
        
        if len(self.pending_requests) >= self.batch_size:
            await self.process_batch()
        elif self.batch_timer is None:
            self.batch_timer = asyncio.create_task(
                self.wait_and_process()
            )
    
    async def wait_and_process(self):
        """Wait for timeout then process batch"""
        await asyncio.sleep(self.batch_timeout)
        await self.process_batch()
    
    async def process_batch(self):
        """Process batched requests"""
        if not self.pending_requests:
            return
        
        batch = self.pending_requests.copy()
        self.pending_requests.clear()
        self.batch_timer = None
        
        # Process batch
        async with aiohttp.ClientSession() as session:
            tasks = [
                self.make_request(session, req) 
                for req in batch
            ]
            await asyncio.gather(*tasks)
    
    async def make_request(self, session, request_data):
        """Make individual API request"""
        async with session.post(
            request_data['url'],
            json=request_data['data']
        ) as response:
            return await response.json()

# Global batcher
api_batcher = APIBatcher()
```

### Connection Pooling

```python
import aiohttp
import asyncio
from aiohttp import TCPConnector

class ConnectionManager:
    """Manage HTTP connections efficiently"""
    
    def __init__(self):
        self.connector = TCPConnector(
            limit=100,  # Total connection pool size
            limit_per_host=30,  # Per-host connection limit
            ttl_dns_cache=300,  # DNS cache TTL
            use_dns_cache=True,
            keepalive_timeout=30,
            enable_cleanup_closed=True
        )
        self.session = None
    
    async def get_session(self):
        """Get or create HTTP session"""
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession(
                connector=self.connector,
                timeout=aiohttp.ClientTimeout(total=30)
            )
        return self.session
    
    async def close(self):
        """Close connections"""
        if self.session and not self.session.closed:
            await self.session.close()

# Global connection manager
connection_manager = ConnectionManager()
```

## Memory Optimization

### Memory Monitoring

```python
import psutil
import gc
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def monitor_memory(func):
    """Decorator to monitor memory usage"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Memory before
        process = psutil.Process()
        memory_before = process.memory_info().rss / 1024 / 1024  # MB
        
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            # Memory after
            memory_after = process.memory_info().rss / 1024 / 1024  # MB
            memory_diff = memory_after - memory_before
            
            if memory_diff > 10:  # Log if memory increased by more than 10MB
                logger.warning(
                    f"High memory usage in {func.__name__}: "
                    f"{memory_diff:.2f}MB increase"
                )
            
            # Force garbage collection if memory usage is high
            if memory_after > 500:  # 500MB threshold
                gc.collect()
    
    return wrapper

@monitor_memory
@callback(
    Output('memory-intensive-output', 'children'),
    Input('memory-intensive-input', 'value')
)
def memory_intensive_callback(value):
    # Your callback logic here
    return process_large_data(value)
```

### Object Cleanup

```python
import weakref
from typing import Dict, Any

class ComponentRegistry:
    """Registry for tracking and cleaning up components"""
    
    def __init__(self):
        self._components: Dict[str, Any] = {}
        self._cleanup_callbacks: Dict[str, callable] = {}
    
    def register(self, component_id: str, component: Any, cleanup_callback: callable = None):
        """Register component with optional cleanup callback"""
        self._components[component_id] = weakref.ref(
            component, 
            lambda ref: self._cleanup(component_id)
        )
        
        if cleanup_callback:
            self._cleanup_callbacks[component_id] = cleanup_callback
    
    def _cleanup(self, component_id: str):
        """Cleanup component resources"""
        if component_id in self._cleanup_callbacks:
            try:
                self._cleanup_callbacks[component_id]()
            except Exception as e:
                logger.error(f"Error cleaning up component {component_id}: {e}")
            finally:
                del self._cleanup_callbacks[component_id]
        
        if component_id in self._components:
            del self._components[component_id]
    
    def cleanup_all(self):
        """Cleanup all registered components"""
        for component_id in list(self._cleanup_callbacks.keys()):
            self._cleanup(component_id)

# Global registry
component_registry = ComponentRegistry()
```

## Network Optimization

### Request Compression

```python
from flask_compress import Compress
import gzip
import json

# Enable compression
Compress(app.server)

# Custom compression for API responses
@app.server.after_request
def compress_response(response):
    """Compress large responses"""
    if (response.content_length and 
        response.content_length > 1024 and  # Only compress if > 1KB
        'gzip' in request.headers.get('Accept-Encoding', '')):
        
        response.data = gzip.compress(response.data)
        response.headers['Content-Encoding'] = 'gzip'
        response.headers['Content-Length'] = len(response.data)
    
    return response
```

### CDN Integration

```python
import os

class CDNConfig:
    """CDN configuration for static assets"""
    
    CDN_DOMAIN = os.environ.get('CDN_DOMAIN', '')
    
    @staticmethod
    def get_asset_url(asset_path: str) -> str:
        """Get CDN URL for asset"""
        if CDNConfig.CDN_DOMAIN:
            return f"https://{CDNConfig.CDN_DOMAIN}/{asset_path}"
        return f"/assets/{asset_path}"

# Configure Dash to use CDN
if CDNConfig.CDN_DOMAIN:
    app.config.external_stylesheets = [
        CDNConfig.get_asset_url('css/bootstrap.min.css'),
        CDNConfig.get_asset_url('css/custom.css')
    ]
```

## Database Optimization

### Connection Pooling

```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
import os

# Optimized database connection
engine = create_engine(
    os.environ.get('DATABASE_URL'),
    poolclass=QueuePool,
    pool_size=20,  # Number of connections to maintain
    max_overflow=30,  # Additional connections when pool is full
    pool_pre_ping=True,  # Validate connections before use
    pool_recycle=3600,  # Recycle connections every hour
    echo=False  # Disable SQL logging in production
)
```

### Query Optimization

```python
from sqlalchemy.orm import sessionmaker, joinedload
from contextlib import contextmanager

Session = sessionmaker(bind=engine)

@contextmanager
def get_db_session():
    """Context manager for database sessions"""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def get_user_data_optimized(user_id: int):
    """Optimized query with eager loading"""
    with get_db_session() as session:
        return session.query(User)\
            .options(joinedload(User.preferences))\
            .filter(User.id == user_id)\
            .first()
```

## Performance Monitoring

### Real-time Metrics

```python
import time
from collections import defaultdict, deque
from threading import Lock
import psutil

class PerformanceMonitor:
    """Monitor application performance metrics"""
    
    def __init__(self, window_size: int = 100):
        self.window_size = window_size
        self.metrics = defaultdict(lambda: deque(maxlen=window_size))
        self.lock = Lock()
    
    def record_metric(self, name: str, value: float):
        """Record a performance metric"""
        with self.lock:
            self.metrics[name].append({
                'value': value,
                'timestamp': time.time()
            })
    
    def get_average(self, name: str) -> float:
        """Get average value for metric"""
        with self.lock:
            values = [m['value'] for m in self.metrics[name]]
            return sum(values) / len(values) if values else 0
    
    def get_system_metrics(self) -> dict:
        """Get current system metrics"""
        process = psutil.Process()
        return {
            'cpu_percent': psutil.cpu_percent(),
            'memory_percent': psutil.virtual_memory().percent,
            'process_memory_mb': process.memory_info().rss / 1024 / 1024,
            'open_files': len(process.open_files()),
            'connections': len(process.connections())
        }

# Global monitor
perf_monitor = PerformanceMonitor()

# Decorator for timing functions
def time_function(metric_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                return func(*args, **kwargs)
            finally:
                duration = time.time() - start_time
                perf_monitor.record_metric(metric_name, duration)
        return wrapper
    return decorator
```

### Performance Dashboard

```python
@app.callback(
    Output('performance-metrics', 'children'),
    Input('metrics-interval', 'n_intervals')
)
def update_performance_metrics(n_intervals):
    """Update performance metrics display"""
    system_metrics = perf_monitor.get_system_metrics()
    
    return dbc.Card([
        dbc.CardBody([
            html.H5("System Performance"),
            html.P(f"CPU: {system_metrics['cpu_percent']:.1f}%"),
            html.P(f"Memory: {system_metrics['memory_percent']:.1f}%"),
            html.P(f"Process Memory: {system_metrics['process_memory_mb']:.1f}MB"),
            html.P(f"Open Files: {system_metrics['open_files']}"),
            html.P(f"Connections: {system_metrics['connections']}")
        ])
    ])
```

## Best Practices

### Performance Checklist

- [ ] Use lazy loading for components
- [ ] Implement caching for expensive operations
- [ ] Optimize database queries
- [ ] Use connection pooling
- [ ] Monitor memory usage
- [ ] Compress responses
- [ ] Use CDN for static assets
- [ ] Implement request batching
- [ ] Monitor performance metrics
- [ ] Regular performance testing

### Common Performance Issues

1. **Memory leaks**: Monitor and cleanup unused objects
2. **Slow database queries**: Use indexing and query optimization
3. **Large payloads**: Implement compression and pagination
4. **Too many connections**: Use connection pooling
5. **Blocking operations**: Use async/await patterns

## Next Steps

- [Production Deployment](production.md) - Deploy optimized application
- [Environment Configuration](environment.md) - Configure for performance
- [Monitoring](../contributing/testing.md) - Monitor performance in production
