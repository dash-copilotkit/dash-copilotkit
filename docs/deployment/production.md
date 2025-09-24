# Production Deployment

Guide for deploying Dash CopilotKit Components applications to production environments.

## Overview

This guide covers best practices for deploying Dash applications with CopilotKit components to various production environments including cloud platforms, containers, and traditional servers.

## Pre-deployment Checklist

### Security
- [ ] Store API keys in environment variables
- [ ] Enable HTTPS/SSL certificates
- [ ] Configure CORS settings appropriately
- [ ] Implement rate limiting
- [ ] Set up authentication if required
- [ ] Review and sanitize user inputs

### Performance
- [ ] Optimize component loading
- [ ] Configure caching strategies
- [ ] Set up CDN for static assets
- [ ] Monitor memory usage
- [ ] Test with expected user load

### Monitoring
- [ ] Set up application logging
- [ ] Configure error tracking
- [ ] Implement health checks
- [ ] Set up performance monitoring
- [ ] Configure alerts

## Environment Configuration

### Environment Variables

Create a `.env` file for local development and configure environment variables in production:

```bash
# API Keys
COPILOTKIT_PUBLIC_API_KEY=ck_pub_your_key_here
OPENAI_API_KEY=sk-your_openai_key_here

# Application Settings
DASH_DEBUG=False
DASH_HOST=0.0.0.0
DASH_PORT=8050

# Database (if using)
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Security
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### Production App Configuration

```python
import os
from dash import Dash
import dash_bootstrap_components as dbc
import dash_copilotkit_components

# Production configuration
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    # Disable dev tools in production
    dev_tools_hot_reload=False,
    dev_tools_ui=False,
    dev_tools_props_check=False
)

# Security headers
app.server.config.update(
    SECRET_KEY=os.environ.get('SECRET_KEY', 'dev-key-change-in-production'),
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax'
)

# Configure component with environment variables
def create_copilot_component():
    return dash_copilotkit_components.DashCopilotkitComponents(
        id='production-copilot',
        ui_type='chat',
        public_api_key=os.environ.get('COPILOTKIT_PUBLIC_API_KEY'),
        # Or use custom runtime
        api_key=os.environ.get('OPENAI_API_KEY'),
        runtime_url=os.environ.get('COPILOTKIT_RUNTIME_URL'),
        instructions='You are a production AI assistant.'
    )

if __name__ == '__main__':
    app.run(
        host=os.environ.get('DASH_HOST', '127.0.0.1'),
        port=int(os.environ.get('DASH_PORT', 8050)),
        debug=os.environ.get('DASH_DEBUG', 'False').lower() == 'true'
    )
```

## Cloud Platform Deployment

### Heroku Deployment

1. **Create required files:**

`requirements.txt`:
```
dash>=2.14.0
dash-bootstrap-components>=1.5.0
dash-copilotkit-components>=0.1.0
gunicorn>=21.2.0
python-dotenv>=1.0.0
```

`Procfile`:
```
web: gunicorn app:server
```

`runtime.txt`:
```
python-3.11.6
```

2. **Update app.py for Heroku:**

```python
import os
from dash import Dash

app = Dash(__name__)
server = app.server  # Expose Flask server for Gunicorn

# Your app layout and callbacks here

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8050)),
        debug=False
    )
```

3. **Deploy to Heroku:**

```bash
# Install Heroku CLI and login
heroku login

# Create Heroku app
heroku create your-app-name

# Set environment variables
heroku config:set COPILOTKIT_PUBLIC_API_KEY=your_key_here

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### AWS Elastic Beanstalk

1. **Create `application.py`:**

```python
from app import app

# EB looks for 'application' variable
application = app.server

if __name__ == '__main__':
    application.run(debug=False)
```

2. **Create `.ebextensions/python.config`:**

```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: application.py
  aws:elasticbeanstalk:application:environment:
    PYTHONPATH: "/var/app/current:$PYTHONPATH"
```

3. **Deploy:**

```bash
# Install EB CLI
pip install awsebcli

# Initialize EB application
eb init

# Create environment and deploy
eb create production-env
eb deploy
```

### Google Cloud Platform (Cloud Run)

1. **Create `Dockerfile`:**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:server"]
```

2. **Create `cloudbuild.yaml`:**

```yaml
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', 'gcr.io/$PROJECT_ID/dash-copilotkit-app', '.']
- name: 'gcr.io/cloud-builders/docker'
  args: ['push', 'gcr.io/$PROJECT_ID/dash-copilotkit-app']
- name: 'gcr.io/cloud-builders/gcloud'
  args: ['run', 'deploy', 'dash-copilotkit-app', 
         '--image', 'gcr.io/$PROJECT_ID/dash-copilotkit-app', 
         '--platform', 'managed', 
         '--region', 'us-central1']
```

3. **Deploy:**

```bash
# Build and deploy
gcloud builds submit --config cloudbuild.yaml

# Set environment variables
gcloud run services update dash-copilotkit-app \
  --set-env-vars COPILOTKIT_PUBLIC_API_KEY=your_key_here
```

## Docker Deployment

### Basic Dockerfile

```dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd --create-home --shell /bin/bash app
USER app

# Expose port
EXPOSE 8050

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8050/_dash-layout || exit 1

# Run application
CMD ["gunicorn", "--bind", "0.0.0.0:8050", "--workers", "4", "app:server"]
```

### Docker Compose for Development

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8050:8050"
    environment:
      - COPILOTKIT_PUBLIC_API_KEY=${COPILOTKIT_PUBLIC_API_KEY}
      - DASH_DEBUG=True
    volumes:
      - .:/app
    depends_on:
      - redis
      - postgres

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  postgres:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=dashapp
      - POSTGRES_USER=dashuser
      - POSTGRES_PASSWORD=dashpass
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Production Docker Compose

```yaml
version: '3.8'

services:
  app:
    build: .
    restart: unless-stopped
    ports:
      - "8050:8050"
    environment:
      - COPILOTKIT_PUBLIC_API_KEY=${COPILOTKIT_PUBLIC_API_KEY}
      - DATABASE_URL=postgresql://dashuser:dashpass@postgres:5432/dashapp
      - REDIS_URL=redis://redis:6379
    depends_on:
      - redis
      - postgres
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8050/_dash-layout"]
      interval: 30s
      timeout: 10s
      retries: 3

  nginx:
    image: nginx:alpine
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - app

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    volumes:
      - redis_data:/data

  postgres:
    image: postgres:15-alpine
    restart: unless-stopped
    environment:
      - POSTGRES_DB=dashapp
      - POSTGRES_USER=dashuser
      - POSTGRES_PASSWORD=dashpass
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  redis_data:
  postgres_data:
```

## Load Balancing and Scaling

### Nginx Configuration

```nginx
upstream dash_app {
    server app1:8050;
    server app2:8050;
    server app3:8050;
}

server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com;

    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;

    location / {
        proxy_pass http://dash_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    # Static files caching
    location /assets/ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

## Monitoring and Logging

### Application Logging

```python
import logging
import os
from pythonjsonlogger import jsonlogger

# Configure logging
log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.basicConfig(level=getattr(logging, log_level))

# JSON formatter for structured logging
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(logHandler)

# Log CopilotKit interactions
@app.callback(
    Output('log-store', 'data'),
    Input('copilot-component', 'value')
)
def log_copilot_interaction(value):
    logger.info("CopilotKit interaction", extra={
        'component_id': 'copilot-component',
        'value_length': len(value) if value else 0,
        'timestamp': datetime.utcnow().isoformat()
    })
    return {}
```

### Health Check Endpoint

```python
from flask import jsonify
import psutil

@app.server.route('/health')
def health_check():
    try:
        # Check system resources
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent
        
        # Check external dependencies
        # Add your checks here (database, APIs, etc.)
        
        status = {
            'status': 'healthy',
            'timestamp': datetime.utcnow().isoformat(),
            'system': {
                'cpu_percent': cpu_percent,
                'memory_percent': memory_percent
            }
        }
        
        return jsonify(status), 200
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.utcnow().isoformat()
        }), 500
```

## Security Best Practices

### API Key Management

```python
import os
from cryptography.fernet import Fernet

class SecureConfig:
    def __init__(self):
        self.encryption_key = os.environ.get('ENCRYPTION_KEY')
        if self.encryption_key:
            self.cipher = Fernet(self.encryption_key.encode())
    
    def get_api_key(self):
        encrypted_key = os.environ.get('ENCRYPTED_COPILOTKIT_KEY')
        if encrypted_key and self.cipher:
            return self.cipher.decrypt(encrypted_key.encode()).decode()
        return os.environ.get('COPILOTKIT_PUBLIC_API_KEY')

config = SecureConfig()
```

### Rate Limiting

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app.server,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.server.route('/api/copilot')
@limiter.limit("10 per minute")
def copilot_api():
    # Your API endpoint
    pass
```

## Performance Optimization

### Caching

```python
from flask_caching import Cache

cache = Cache(app.server, config={
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'redis://localhost:6379')
})

@cache.memoize(timeout=300)
def expensive_computation(params):
    # Cache expensive operations
    pass
```

### Asset Optimization

```python
# Compress assets
app.server.config['COMPRESS_MIMETYPES'] = [
    'text/html', 'text/css', 'text/xml',
    'application/json', 'application/javascript'
]

# Enable gzip compression
from flask_compress import Compress
Compress(app.server)
```

## Troubleshooting

### Common Issues

1. **Memory leaks**: Monitor memory usage and implement proper cleanup
2. **Slow loading**: Optimize component loading and use lazy loading
3. **API rate limits**: Implement proper rate limiting and caching
4. **SSL certificate issues**: Ensure proper certificate configuration
5. **Database connections**: Use connection pooling and proper cleanup

### Debugging in Production

```python
# Enable debug mode safely
if os.environ.get('ENABLE_DEBUG') == 'true':
    app.run(debug=True)
else:
    # Production logging
    import logging
    logging.basicConfig(level=logging.INFO)
```

## Next Steps

- [Environment Configuration](environment.md) - Detailed environment setup
- [Performance Optimization](performance.md) - Advanced performance tuning
- [Monitoring Guide](../contributing/testing.md) - Testing and monitoring strategies
