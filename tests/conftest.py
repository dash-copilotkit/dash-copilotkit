"""
Pytest configuration and fixtures for Dash CopilotKit Components tests.
"""
import pytest
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import dash testing utilities
try:
    from dash.testing.application_runners import import_app
    from dash.testing.composite import DashComposite
    DASH_TESTING_AVAILABLE = True
except ImportError:
    DASH_TESTING_AVAILABLE = False

# Import selenium for browser testing
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False


@pytest.fixture(scope="session")
def dash_duo():
    """
    Fixture for Dash testing with browser automation.
    Only available if dash testing and selenium are installed.
    """
    if not DASH_TESTING_AVAILABLE:
        pytest.skip("Dash testing utilities not available")
    
    if not SELENIUM_AVAILABLE:
        pytest.skip("Selenium not available for browser testing")
    
    from dash.testing.composite import DashComposite
    
    # Configure Chrome options for headless testing
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Create DashComposite instance
    dash_duo = DashComposite(
        selenium_grid_url=None,
        remote_url=None,
        headless=True,
        options=chrome_options
    )
    
    yield dash_duo
    
    # Cleanup
    dash_duo.driver.quit()


@pytest.fixture
def chrome_driver():
    """
    Fixture for Chrome WebDriver.
    Only available if selenium is installed.
    """
    if not SELENIUM_AVAILABLE:
        pytest.skip("Selenium not available")
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    # Use webdriver-manager to handle ChromeDriver installation
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    yield driver
    
    driver.quit()


@pytest.fixture
def sample_api_key():
    """Fixture providing a sample API key for testing."""
    return "test-api-key-12345"


@pytest.fixture
def sample_labels():
    """Fixture providing sample labels configuration."""
    return {
        "title": "Test Assistant",
        "initial": "Hello! This is a test assistant."
    }


@pytest.fixture
def sample_instructions():
    """Fixture providing sample instructions."""
    return "You are a helpful test assistant. Respond to user queries in a friendly manner."


@pytest.fixture(params=['chat', 'popup', 'sidebar', 'textarea'])
def ui_type(request):
    """Parametrized fixture for testing all UI types."""
    return request.param


@pytest.fixture(params=['left', 'right'])
def sidebar_position(request):
    """Parametrized fixture for testing sidebar positions."""
    return request.param


@pytest.fixture
def component_props():
    """Fixture providing common component props."""
    return {
        'public_api_key': 'test-key',
        'instructions': 'You are a test assistant.',
        'placeholder': 'Type your message here...',
        'disabled': False,
        'width': '100%',
        'height': '400px'
    }


@pytest.fixture
def custom_style():
    """Fixture providing custom styling for components."""
    return {
        'backgroundColor': '#f0f0f0',
        'border': '1px solid #ccc',
        'borderRadius': '8px',
        'padding': '10px'
    }


# Pytest configuration
def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "browser: mark test as requiring browser automation"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test names."""
    for item in items:
        # Add markers based on test file names
        if "test_dash_copilotkit_components" in item.nodeid:
            item.add_marker(pytest.mark.unit)
        
        if "test_component_rendering" in item.nodeid:
            item.add_marker(pytest.mark.integration)
            item.add_marker(pytest.mark.browser)
        
        # Mark browser tests as slow
        if "browser" in item.keywords:
            item.add_marker(pytest.mark.slow)


# Skip browser tests if dependencies are not available
def pytest_runtest_setup(item):
    """Setup function to skip tests based on available dependencies."""
    if "browser" in item.keywords:
        if not SELENIUM_AVAILABLE or not DASH_TESTING_AVAILABLE:
            pytest.skip("Browser testing dependencies not available")


# Environment variables for testing
@pytest.fixture(autouse=True)
def setup_test_environment():
    """Setup test environment variables."""
    # Set test environment
    os.environ['TESTING'] = 'true'
    
    # Disable Dash dev tools in tests
    os.environ['DASH_DEBUG'] = 'false'
    
    yield
    
    # Cleanup
    if 'TESTING' in os.environ:
        del os.environ['TESTING']
    if 'DASH_DEBUG' in os.environ:
        del os.environ['DASH_DEBUG']


# Custom assertions for component testing
class ComponentAssertions:
    """Custom assertions for component testing."""
    
    @staticmethod
    def assert_component_props(component, expected_props):
        """Assert that component has expected props."""
        for prop, expected_value in expected_props.items():
            actual_value = getattr(component, prop, None)
            assert actual_value == expected_value, f"Expected {prop}={expected_value}, got {actual_value}"
    
    @staticmethod
    def assert_component_in_layout(layout, component_id):
        """Assert that component with given ID exists in layout."""
        def find_component(children, target_id):
            if hasattr(children, 'id') and children.id == target_id:
                return True
            if hasattr(children, 'children'):
                if isinstance(children.children, list):
                    return any(find_component(child, target_id) for child in children.children)
                else:
                    return find_component(children.children, target_id)
            return False
        
        assert find_component(layout, component_id), f"Component with id '{component_id}' not found in layout"


@pytest.fixture
def component_assertions():
    """Fixture providing custom component assertions."""
    return ComponentAssertions()


# Performance testing utilities
@pytest.fixture
def performance_timer():
    """Fixture for measuring test performance."""
    import time
    
    class Timer:
        def __init__(self):
            self.start_time = None
            self.end_time = None
        
        def start(self):
            self.start_time = time.time()
        
        def stop(self):
            self.end_time = time.time()
        
        @property
        def elapsed(self):
            if self.start_time and self.end_time:
                return self.end_time - self.start_time
            return None
    
    return Timer()


# Mock data for testing
@pytest.fixture
def mock_copilotkit_response():
    """Fixture providing mock CopilotKit API response."""
    return {
        "choices": [
            {
                "message": {
                    "content": "This is a mock response from the AI assistant.",
                    "role": "assistant"
                }
            }
        ]
    }


# Test data generators
@pytest.fixture
def generate_test_components():
    """Fixture that generates test components with various configurations."""
    import dash_copilotkit_components
    
    def _generate(count=5, ui_type='chat'):
        components = []
        for i in range(count):
            component = dash_copilotkit_components.DashCopilotkitComponents(
                id=f'test-component-{i}',
                ui_type=ui_type,
                public_api_key=f'test-key-{i}',
                instructions=f'You are test assistant number {i}.'
            )
            components.append(component)
        return components
    
    return _generate
