# Environment Configuration

Detailed guide for configuring different environments for Dash CopilotKit Components applications.

## Environment Types

### Development Environment
- Local development with hot reload
- Debug mode enabled
- Detailed error messages
- Development API keys

### Staging Environment
- Production-like configuration
- Testing with production data
- Performance monitoring
- Staging API keys

### Production Environment
- Optimized for performance
- Security hardened
- Monitoring and logging
- Production API keys

## Environment Variables

### Required Variables

```bash
# CopilotKit Configuration
COPILOTKIT_PUBLIC_API_KEY=ck_pub_your_key_here
# OR for custom runtime
OPENAI_API_KEY=sk-your_openai_key_here
COPILOTKIT_RUNTIME_URL=https://your-runtime.com/api/copilotkit

# Application Settings
DASH_ENV=production  # development, staging, production
DASH_DEBUG=false
DASH_HOST=0.0.0.0
DASH_PORT=8050

# Security
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

### Optional Variables

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
REDIS_URL=redis://localhost:6379

# Logging
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR
LOG_FORMAT=json  # json, text

# Performance
WORKERS=4
TIMEOUT=30
MAX_REQUESTS=1000

# Monitoring
SENTRY_DSN=https://your-sentry-dsn
DATADOG_API_KEY=your-datadog-key
```

## Configuration Management

### Using python-dotenv

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    COPILOTKIT_PUBLIC_API_KEY = os.environ.get('COPILOTKIT_PUBLIC_API_KEY')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    COPILOTKIT_RUNTIME_URL = os.environ.get('COPILOTKIT_RUNTIME_URL')

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    DASH_ENV = 'development'
    LOG_LEVEL = 'DEBUG'

class StagingConfig(Config):
    """Staging configuration"""
    DEBUG = False
    DASH_ENV = 'staging'
    LOG_LEVEL = 'INFO'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    DASH_ENV = 'production'
    LOG_LEVEL = 'WARNING'

# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

### Environment-specific App Configuration

```python
import os
from dash import Dash
import dash_bootstrap_components as dbc

def create_app():
    """Application factory"""
    env = os.environ.get('DASH_ENV', 'development')
    
    app = Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        suppress_callback_exceptions=True
    )
    
    # Configure based on environment
    if env == 'development':
        app.config.update(
            dev_tools_hot_reload=True,
            dev_tools_ui=True,
            dev_tools_props_check=True
        )
    else:
        app.config.update(
            dev_tools_hot_reload=False,
            dev_tools_ui=False,
            dev_tools_props_check=False
        )
    
    return app

app = create_app()
```

## Development Environment Setup

### Local Development

1. **Create `.env` file:**

```bash
# .env
DASH_ENV=development
DASH_DEBUG=true
COPILOTKIT_PUBLIC_API_KEY=ck_pub_dev_key_here
LOG_LEVEL=DEBUG
```

2. **Install development dependencies:**

```bash
pip install -r requirements-dev.txt
```

3. **Run development server:**

```bash
python app.py
```

### Development with Docker

```dockerfile
# Dockerfile.dev
FROM python:3.11-slim

WORKDIR /app

# Install development dependencies
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

# Copy source code
COPY . .

# Development server with hot reload
CMD ["python", "app.py"]
```

```yaml
# docker-compose.dev.yml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "8050:8050"
    environment:
      - DASH_ENV=development
      - DASH_DEBUG=true
    volumes:
      - .:/app
    env_file:
      - .env.dev
```

## Staging Environment

### Staging Configuration

```bash
# .env.staging
DASH_ENV=staging
DASH_DEBUG=false
COPILOTKIT_PUBLIC_API_KEY=ck_pub_staging_key_here
DATABASE_URL=postgresql://user:pass@staging-db:5432/stagingdb
REDIS_URL=redis://staging-redis:6379
LOG_LEVEL=INFO
SENTRY_DSN=https://staging-sentry-dsn
```

### Staging Deployment

```yaml
# docker-compose.staging.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8050:8050"
    environment:
      - DASH_ENV=staging
    env_file:
      - .env.staging
    depends_on:
      - postgres
      - redis

  postgres:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=stagingdb
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
    volumes:
      - staging_postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    volumes:
      - staging_redis_data:/data

volumes:
  staging_postgres_data:
  staging_redis_data:
```

## Production Environment

### Production Configuration

```bash
# .env.production
DASH_ENV=production
DASH_DEBUG=false
DASH_HOST=0.0.0.0
DASH_PORT=8050

# Security
SECRET_KEY=super-secret-production-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# CopilotKit
COPILOTKIT_PUBLIC_API_KEY=ck_pub_production_key_here

# Database
DATABASE_URL=postgresql://produser:prodpass@prod-db:5432/proddb
REDIS_URL=redis://prod-redis:6379

# Monitoring
LOG_LEVEL=WARNING
SENTRY_DSN=https://production-sentry-dsn
DATADOG_API_KEY=production-datadog-key

# Performance
WORKERS=4
TIMEOUT=30
MAX_REQUESTS=1000
```

### Production Security

```python
import os
from cryptography.fernet import Fernet

class ProductionConfig:
    """Production configuration with enhanced security"""
    
    @staticmethod
    def get_secret_key():
        """Get or generate secret key"""
        key = os.environ.get('SECRET_KEY')
        if not key:
            raise ValueError("SECRET_KEY environment variable is required")
        return key
    
    @staticmethod
    def get_encrypted_api_key():
        """Decrypt API key"""
        encryption_key = os.environ.get('ENCRYPTION_KEY')
        encrypted_key = os.environ.get('ENCRYPTED_COPILOTKIT_KEY')
        
        if encryption_key and encrypted_key:
            cipher = Fernet(encryption_key.encode())
            return cipher.decrypt(encrypted_key.encode()).decode()
        
        return os.environ.get('COPILOTKIT_PUBLIC_API_KEY')
```

## Environment Validation

### Configuration Validator

```python
import os
import sys
from typing import List, Optional

class ConfigValidator:
    """Validate environment configuration"""
    
    REQUIRED_VARS = [
        'COPILOTKIT_PUBLIC_API_KEY',
        'SECRET_KEY'
    ]
    
    PRODUCTION_REQUIRED = [
        'DATABASE_URL',
        'REDIS_URL',
        'SENTRY_DSN'
    ]
    
    @classmethod
    def validate(cls, env: str = None) -> List[str]:
        """Validate configuration and return list of errors"""
        errors = []
        env = env or os.environ.get('DASH_ENV', 'development')
        
        # Check required variables
        for var in cls.REQUIRED_VARS:
            if not os.environ.get(var):
                errors.append(f"Missing required environment variable: {var}")
        
        # Check production-specific variables
        if env == 'production':
            for var in cls.PRODUCTION_REQUIRED:
                if not os.environ.get(var):
                    errors.append(f"Missing production environment variable: {var}")
        
        # Validate API key format
        api_key = os.environ.get('COPILOTKIT_PUBLIC_API_KEY')
        if api_key and not api_key.startswith('ck_pub_'):
            errors.append("COPILOTKIT_PUBLIC_API_KEY should start with 'ck_pub_'")
        
        return errors
    
    @classmethod
    def validate_or_exit(cls, env: str = None):
        """Validate configuration and exit if errors found"""
        errors = cls.validate(env)
        if errors:
            print("Configuration errors found:")
            for error in errors:
                print(f"  - {error}")
            sys.exit(1)
        print("Configuration validation passed")

# Validate on import
if __name__ == "__main__":
    ConfigValidator.validate_or_exit()
```

## Environment-specific Features

### Feature Flags

```python
import os

class FeatureFlags:
    """Environment-based feature flags"""
    
    @staticmethod
    def is_development():
        return os.environ.get('DASH_ENV') == 'development'
    
    @staticmethod
    def is_production():
        return os.environ.get('DASH_ENV') == 'production'
    
    @staticmethod
    def enable_debug_tools():
        return FeatureFlags.is_development()
    
    @staticmethod
    def enable_analytics():
        return not FeatureFlags.is_development()
    
    @staticmethod
    def enable_error_reporting():
        return os.environ.get('SENTRY_DSN') is not None

# Usage in app
if FeatureFlags.enable_debug_tools():
    app.config.update(dev_tools_ui=True)

if FeatureFlags.enable_analytics():
    # Initialize analytics
    pass
```

### Environment-specific Components

```python
import dash_copilotkit_components
from config import FeatureFlags

def create_copilot_component():
    """Create CopilotKit component with environment-specific config"""
    
    base_config = {
        'id': 'main-copilot',
        'ui_type': 'chat',
        'height': '500px'
    }
    
    if FeatureFlags.is_development():
        # Development configuration
        base_config.update({
            'public_api_key': os.environ.get('COPILOTKIT_PUBLIC_API_KEY'),
            'instructions': 'You are a development assistant with debug capabilities.'
        })
    else:
        # Production configuration
        base_config.update({
            'public_api_key': os.environ.get('COPILOTKIT_PUBLIC_API_KEY'),
            'instructions': 'You are a professional assistant.'
        })
    
    return dash_copilotkit_components.DashCopilotkitComponents(**base_config)
```

## Environment Migration

### Database Migrations

```python
import os
from alembic import command
from alembic.config import Config

def run_migrations():
    """Run database migrations based on environment"""
    env = os.environ.get('DASH_ENV', 'development')
    
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", os.environ.get('DATABASE_URL'))
    
    if env == 'production':
        # Production migrations with backup
        print("Running production migrations...")
        command.upgrade(alembic_cfg, "head")
    else:
        # Development migrations
        command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    run_migrations()
```

## Troubleshooting

### Common Environment Issues

1. **Missing environment variables**: Use validation scripts
2. **Wrong API keys**: Check key format and permissions
3. **Database connection issues**: Verify connection strings
4. **Port conflicts**: Check port availability
5. **Permission issues**: Verify file and directory permissions

### Environment Debugging

```python
import os
import json

def debug_environment():
    """Debug environment configuration"""
    env_vars = {
        'DASH_ENV': os.environ.get('DASH_ENV'),
        'DASH_DEBUG': os.environ.get('DASH_DEBUG'),
        'DASH_HOST': os.environ.get('DASH_HOST'),
        'DASH_PORT': os.environ.get('DASH_PORT'),
        'COPILOTKIT_PUBLIC_API_KEY': 'SET' if os.environ.get('COPILOTKIT_PUBLIC_API_KEY') else 'NOT SET',
        'DATABASE_URL': 'SET' if os.environ.get('DATABASE_URL') else 'NOT SET',
        'REDIS_URL': 'SET' if os.environ.get('REDIS_URL') else 'NOT SET'
    }
    
    print("Environment Configuration:")
    print(json.dumps(env_vars, indent=2))

if __name__ == "__main__":
    debug_environment()
```

## Next Steps

- [Production Deployment](production.md) - Deploy to production
- [Performance Optimization](performance.md) - Optimize for production
- [Monitoring](../contributing/testing.md) - Monitor your application
