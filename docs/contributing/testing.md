# Testing Guide

Comprehensive testing strategies for Dash CopilotKit Components.

## Testing Overview

Our testing strategy covers:
- Unit tests for individual components
- Integration tests for component interactions
- End-to-end tests for complete workflows
- Performance tests for optimization
- Visual regression tests for UI consistency

## Test Setup

### JavaScript Testing

```bash
# Install testing dependencies
npm install --save-dev \
  jest \
  @testing-library/react \
  @testing-library/jest-dom \
  @testing-library/user-event \
  jest-environment-jsdom
```

### Python Testing

```bash
# Install Python testing dependencies
pip install pytest pytest-dash pytest-cov selenium webdriver-manager
```

### Jest Configuration

```javascript
// jest.config.js
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/tests/setup.js'],
  moduleNameMapping: {
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy'
  },
  collectCoverageFrom: [
    'src/**/*.{js,jsx}',
    '!src/**/*.test.{js,jsx}',
    '!src/index.js'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};
```

### Test Setup File

```javascript
// tests/setup.js
import '@testing-library/jest-dom';

// Mock CopilotKit components for testing
jest.mock('@copilotkit/react-ui', () => ({
  CopilotChat: ({ children, ...props }) => <div data-testid="copilot-chat" {...props}>{children}</div>,
  CopilotPopup: ({ children, ...props }) => <div data-testid="copilot-popup" {...props}>{children}</div>,
  CopilotSidebar: ({ children, ...props }) => <div data-testid="copilot-sidebar" {...props}>{children}</div>,
  CopilotTextarea: ({ children, ...props }) => <textarea data-testid="copilot-textarea" {...props}>{children}</textarea>
}));

jest.mock('@copilotkit/react-core', () => ({
  CopilotKitProvider: ({ children }) => <div data-testid="copilotkit-provider">{children}</div>
}));
```

## Unit Tests

### Component Unit Tests

```javascript
// tests/components/DashCopilotkitComponents.test.js
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import DashCopilotkitComponents from '../../src/lib/components/DashCopilotkitComponents.react';

describe('DashCopilotkitComponents', () => {
  const defaultProps = {
    id: 'test-component',
    ui_type: 'chat',
    public_api_key: 'test-key'
  };

  test('renders chat component by default', () => {
    render(<DashCopilotkitComponents {...defaultProps} />);
    
    expect(screen.getByTestId('copilot-chat')).toBeInTheDocument();
    expect(screen.getByTestId('copilotkit-provider')).toBeInTheDocument();
  });

  test('renders different UI types', () => {
    const { rerender } = render(
      <DashCopilotkitComponents {...defaultProps} ui_type="popup" />
    );
    expect(screen.getByTestId('copilot-popup')).toBeInTheDocument();

    rerender(<DashCopilotkitComponents {...defaultProps} ui_type="sidebar" />);
    expect(screen.getByTestId('copilot-sidebar')).toBeInTheDocument();

    rerender(<DashCopilotkitComponents {...defaultProps} ui_type="textarea" />);
    expect(screen.getByTestId('copilot-textarea')).toBeInTheDocument();
  });

  test('handles prop changes', () => {
    const { rerender } = render(
      <DashCopilotkitComponents {...defaultProps} disabled={false} />
    );
    
    let component = screen.getByTestId('copilot-chat');
    expect(component).not.toHaveAttribute('disabled');

    rerender(<DashCopilotkitComponents {...defaultProps} disabled={true} />);
    component = screen.getByTestId('copilot-chat');
    expect(component).toHaveAttribute('disabled');
  });

  test('calls setProps on value change', async () => {
    const mockSetProps = jest.fn();
    const user = userEvent.setup();

    render(
      <DashCopilotkitComponents
        {...defaultProps}
        ui_type="textarea"
        setProps={mockSetProps}
      />
    );

    const textarea = screen.getByTestId('copilot-textarea');
    await user.type(textarea, 'Hello World');

    await waitFor(() => {
      expect(mockSetProps).toHaveBeenCalledWith({ value: 'Hello World' });
    });
  });

  test('applies custom styling', () => {
    const customStyle = { backgroundColor: 'red', width: '500px' };
    const customClassName = 'custom-class';

    render(
      <DashCopilotkitComponents
        {...defaultProps}
        style={customStyle}
        className={customClassName}
      />
    );

    const container = screen.getByTestId('copilot-chat').closest('div');
    expect(container).toHaveClass(customClassName);
    expect(container).toHaveStyle(customStyle);
  });

  test('validates prop types', () => {
    const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});

    render(
      <DashCopilotkitComponents
        {...defaultProps}
        ui_type="invalid-type"
      />
    );

    expect(consoleSpy).toHaveBeenCalledWith(
      expect.stringContaining('Warning: Failed prop type')
    );

    consoleSpy.mockRestore();
  });
});
```

### Hook Tests

```javascript
// tests/hooks/useCopilotState.test.js
import { renderHook, act } from '@testing-library/react';
import { useCopilotState } from '../../src/lib/hooks/useCopilotState';

describe('useCopilotState', () => {
  test('initializes with default value', () => {
    const { result } = renderHook(() => useCopilotState('initial value'));
    
    expect(result.current.value).toBe('initial value');
    expect(result.current.isLoading).toBe(false);
    expect(result.current.error).toBe(null);
  });

  test('updates value and calls setProps', () => {
    const mockSetProps = jest.fn();
    const { result } = renderHook(() => useCopilotState('', mockSetProps));

    act(() => {
      result.current.setValue('new value');
    });

    expect(result.current.value).toBe('new value');
    expect(mockSetProps).toHaveBeenCalledWith({ value: 'new value' });
  });

  test('handles errors correctly', () => {
    const mockSetProps = jest.fn();
    const { result } = renderHook(() => useCopilotState('', mockSetProps));
    const testError = new Error('Test error');

    act(() => {
      result.current.handleError(testError);
    });

    expect(result.current.error).toBe(testError);
    expect(mockSetProps).toHaveBeenCalledWith({ error: 'Test error' });
  });
});
```

## Integration Tests

### Python Integration Tests

```python
# tests/test_integration.py
import pytest
from dash import Dash, html, Input, Output, callback
import dash_copilotkit_components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDashIntegration:
    @pytest.fixture
    def app(self):
        """Create test Dash app"""
        app = Dash(__name__)
        
        app.layout = html.Div([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='test-component',
                ui_type='chat',
                public_api_key='test-key',
                instructions='You are a test assistant.'
            ),
            html.Div(id='output')
        ])
        
        @callback(
            Output('output', 'children'),
            Input('test-component', 'value')
        )
        def update_output(value):
            return f"Value: {value}"
        
        return app

    def test_component_renders(self, app):
        """Test that component renders in Dash app"""
        assert app.layout is not None
        
        # Check component is in layout
        component = None
        for child in app.layout.children:
            if hasattr(child, 'id') and child.id == 'test-component':
                component = child
                break
        
        assert component is not None
        assert component.ui_type == 'chat'
        assert component.public_api_key == 'test-key'

    def test_callback_interaction(self, app):
        """Test callback interactions"""
        # This would require a more complex setup with dash testing utilities
        pass

class TestSeleniumIntegration:
    @pytest.fixture
    def driver(self):
        """Setup Selenium WebDriver"""
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()

    @pytest.fixture
    def dash_app(self):
        """Create and run Dash app for Selenium tests"""
        app = Dash(__name__)
        
        app.layout = html.Div([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='selenium-test',
                ui_type='textarea',
                public_api_key='test-key',
                placeholder='Type here...'
            )
        ])
        
        return app

    def test_component_interaction(self, driver, dash_app):
        """Test component interaction with Selenium"""
        # Start the app (this would need proper setup)
        # driver.get('http://localhost:8050')
        
        # Wait for component to load
        # wait = WebDriverWait(driver, 10)
        # textarea = wait.until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="copilot-textarea"]'))
        # )
        
        # Test interaction
        # textarea.send_keys('Hello World')
        # assert textarea.get_attribute('value') == 'Hello World'
        
        pass  # Placeholder for actual implementation
```

### Component Interaction Tests

```python
# tests/test_component_interactions.py
import pytest
from dash import Dash, html, dcc, Input, Output, State, callback
import dash_copilotkit_components

def test_multiple_components():
    """Test multiple CopilotKit components in one app"""
    app = Dash(__name__)
    
    app.layout = html.Div([
        dash_copilotkit_components.DashCopilotkitComponents(
            id='chat-component',
            ui_type='chat',
            public_api_key='test-key'
        ),
        dash_copilotkit_components.DashCopilotkitComponents(
            id='textarea-component',
            ui_type='textarea',
            public_api_key='test-key'
        ),
        html.Div(id='output')
    ])
    
    @callback(
        Output('output', 'children'),
        [Input('chat-component', 'value'),
         Input('textarea-component', 'value')]
    )
    def update_output(chat_value, textarea_value):
        return f"Chat: {chat_value}, Textarea: {textarea_value}"
    
    # Test that app initializes without errors
    assert app.layout is not None

def test_dynamic_component_creation():
    """Test dynamically creating components"""
    app = Dash(__name__)
    
    app.layout = html.Div([
        dcc.Dropdown(
            id='ui-type-dropdown',
            options=[
                {'label': 'Chat', 'value': 'chat'},
                {'label': 'Popup', 'value': 'popup'},
                {'label': 'Sidebar', 'value': 'sidebar'},
                {'label': 'Textarea', 'value': 'textarea'}
            ],
            value='chat'
        ),
        html.Div(id='dynamic-component')
    ])
    
    @callback(
        Output('dynamic-component', 'children'),
        Input('ui-type-dropdown', 'value')
    )
    def create_component(ui_type):
        return dash_copilotkit_components.DashCopilotkitComponents(
            id=f'dynamic-{ui_type}',
            ui_type=ui_type,
            public_api_key='test-key'
        )
    
    assert app.layout is not None
```

## Performance Tests

### Load Testing

```python
# tests/test_performance.py
import time
import pytest
from dash import Dash, html
import dash_copilotkit_components
import psutil
import threading

class TestPerformance:
    def test_component_creation_time(self):
        """Test component creation performance"""
        start_time = time.time()
        
        for i in range(100):
            component = dash_copilotkit_components.DashCopilotkitComponents(
                id=f'perf-test-{i}',
                ui_type='chat',
                public_api_key='test-key'
            )
        
        end_time = time.time()
        creation_time = end_time - start_time
        
        # Should create 100 components in less than 1 second
        assert creation_time < 1.0

    def test_memory_usage(self):
        """Test memory usage with multiple components"""
        process = psutil.Process()
        initial_memory = process.memory_info().rss
        
        components = []
        for i in range(50):
            component = dash_copilotkit_components.DashCopilotkitComponents(
                id=f'memory-test-{i}',
                ui_type='chat',
                public_api_key='test-key'
            )
            components.append(component)
        
        final_memory = process.memory_info().rss
        memory_increase = final_memory - initial_memory
        
        # Memory increase should be reasonable (less than 50MB)
        assert memory_increase < 50 * 1024 * 1024

    def test_concurrent_component_usage(self):
        """Test concurrent component operations"""
        def create_components():
            for i in range(10):
                component = dash_copilotkit_components.DashCopilotkitComponents(
                    id=f'concurrent-{threading.current_thread().ident}-{i}',
                    ui_type='chat',
                    public_api_key='test-key'
                )
        
        threads = []
        start_time = time.time()
        
        for i in range(5):
            thread = threading.Thread(target=create_components)
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        end_time = time.time()
        total_time = end_time - start_time
        
        # Should complete in reasonable time
        assert total_time < 5.0
```

### Benchmark Tests

```javascript
// tests/benchmark.test.js
import { performance } from 'perf_hooks';
import React from 'react';
import { render, cleanup } from '@testing-library/react';
import DashCopilotkitComponents from '../src/lib/components/DashCopilotkitComponents.react';

describe('Performance Benchmarks', () => {
  afterEach(cleanup);

  test('component render time', () => {
    const iterations = 100;
    const times = [];

    for (let i = 0; i < iterations; i++) {
      const start = performance.now();
      
      render(
        <DashCopilotkitComponents
          id={`benchmark-${i}`}
          ui_type="chat"
          public_api_key="test-key"
        />
      );
      
      const end = performance.now();
      times.push(end - start);
      cleanup();
    }

    const averageTime = times.reduce((a, b) => a + b, 0) / times.length;
    const maxTime = Math.max(...times);

    // Average render time should be less than 10ms
    expect(averageTime).toBeLessThan(10);
    // Max render time should be less than 50ms
    expect(maxTime).toBeLessThan(50);
  });

  test('memory usage during renders', () => {
    const initialMemory = process.memoryUsage().heapUsed;
    
    // Render many components
    for (let i = 0; i < 1000; i++) {
      render(
        <DashCopilotkitComponents
          id={`memory-test-${i}`}
          ui_type="chat"
          public_api_key="test-key"
        />
      );
      cleanup();
    }

    // Force garbage collection if available
    if (global.gc) {
      global.gc();
    }

    const finalMemory = process.memoryUsage().heapUsed;
    const memoryIncrease = finalMemory - initialMemory;

    // Memory increase should be minimal (less than 10MB)
    expect(memoryIncrease).toBeLessThan(10 * 1024 * 1024);
  });
});
```

## Visual Regression Tests

### Screenshot Testing

```javascript
// tests/visual.test.js
import puppeteer from 'puppeteer';
import { toMatchImageSnapshot } from 'jest-image-snapshot';

expect.extend({ toMatchImageSnapshot });

describe('Visual Regression Tests', () => {
  let browser;
  let page;

  beforeAll(async () => {
    browser = await puppeteer.launch({ headless: true });
    page = await browser.newPage();
    await page.setViewport({ width: 1200, height: 800 });
  });

  afterAll(async () => {
    await browser.close();
  });

  test('chat component visual', async () => {
    // Navigate to test page with chat component
    await page.goto('http://localhost:8050/test-chat');
    
    // Wait for component to load
    await page.waitForSelector('[data-testid="copilot-chat"]');
    
    // Take screenshot
    const screenshot = await page.screenshot();
    
    expect(screenshot).toMatchImageSnapshot({
      threshold: 0.2,
      thresholdType: 'percent'
    });
  });

  test('popup component visual', async () => {
    await page.goto('http://localhost:8050/test-popup');
    await page.waitForSelector('[data-testid="copilot-popup"]');
    
    const screenshot = await page.screenshot();
    expect(screenshot).toMatchImageSnapshot();
  });
});
```

## Test Automation

### GitHub Actions

```yaml
# .github/workflows/test.yml
name: Test Suite

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        npm ci
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Run JavaScript tests
      run: npm test -- --coverage --watchAll=false
    
    - name: Run Python tests
      run: pytest tests/ --cov=dash_copilotkit_components --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        files: ./coverage/lcov.info,./coverage.xml
```

### Test Scripts

```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "test:ci": "jest --coverage --watchAll=false",
    "test:visual": "jest --testPathPattern=visual",
    "test:performance": "jest --testPathPattern=performance"
  }
}
```

## Test Best Practices

### Writing Good Tests

1. **Test behavior, not implementation**
2. **Use descriptive test names**
3. **Keep tests isolated and independent**
4. **Mock external dependencies**
5. **Test edge cases and error conditions**

### Test Organization

```
tests/
├── components/          # Component unit tests
├── hooks/              # Hook tests
├── integration/        # Integration tests
├── performance/        # Performance tests
├── visual/            # Visual regression tests
├── fixtures/          # Test data and fixtures
├── utils/             # Test utilities
└── setup.js           # Test setup
```

## Next Steps

- [Development Guide](development.md) - Development workflow
- [Building Guide](building.md) - Build process
- [Deployment](../deployment/production.md) - Deploy tested components
