"""
Integration tests for component rendering and behavior.
"""
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import dash
from dash import html, Input, Output, callback
import dash_copilotkit_components


class TestComponentRendering:
    """Test component rendering in browser."""

    @pytest.fixture
    def simple_app(self):
        """Create a simple test app."""
        app = dash.Dash(__name__)
        app.layout = html.Div([
            html.H1("Test App"),
            dash_copilotkit_components.DashCopilotkitComponents(
                id='test-component',
                ui_type='chat',
                public_api_key='test-key',
                instructions='You are a test assistant.'
            )
        ])
        return app

    @pytest.fixture
    def textarea_app(self):
        """Create a textarea test app."""
        app = dash.Dash(__name__)
        app.layout = html.Div([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='textarea-test',
                ui_type='textarea',
                public_api_key='test-key',
                placeholder='Type here for testing...',
                value=''
            ),
            html.Div(id='output')
        ])
        
        @callback(
            Output('output', 'children'),
            Input('textarea-test', 'value')
        )
        def update_output(value):
            return f"Current: {value or 'Empty'}"
        
        return app

    def test_component_loads_in_browser(self, dash_duo, simple_app):
        """Test that component loads successfully in browser."""
        dash_duo.start_server(simple_app)
        
        # Wait for the page to load
        dash_duo.wait_for_element("h1", timeout=10)
        
        # Check that the title is rendered
        title = dash_duo.find_element("h1")
        assert title.text == "Test App"
        
        # Check that the component wrapper is present
        component_wrapper = dash_duo.wait_for_element(".dash-copilotkit-wrapper", timeout=10)
        assert component_wrapper is not None

    def test_textarea_component_interaction(self, dash_duo, textarea_app):
        """Test textarea component interaction."""
        dash_duo.start_server(textarea_app)
        
        # Wait for component to load
        dash_duo.wait_for_element(".dash-copilotkit-wrapper", timeout=10)
        
        # Check initial output
        output = dash_duo.wait_for_element("#output", timeout=5)
        assert "Empty" in output.text

    def test_component_with_different_ui_types(self, dash_duo):
        """Test different UI types render correctly."""
        ui_types = ['chat', 'popup', 'sidebar', 'textarea']
        
        for ui_type in ui_types:
            app = dash.Dash(__name__)
            app.layout = html.Div([
                html.H1(f"Testing {ui_type}"),
                dash_copilotkit_components.DashCopilotkitComponents(
                    id=f'{ui_type}-component',
                    ui_type=ui_type,
                    public_api_key='test-key'
                )
            ])
            
            dash_duo.start_server(app)
            
            # Wait for component to load
            dash_duo.wait_for_element(".dash-copilotkit-wrapper", timeout=10)
            
            # Verify the component is present
            component = dash_duo.find_element(".dash-copilotkit-wrapper")
            assert component is not None

    def test_component_error_handling(self, dash_duo):
        """Test component error handling for invalid configurations."""
        app = dash.Dash(__name__)
        app.layout = html.Div([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='error-component',
                ui_type='chat',
                # No API key provided - should handle gracefully
            ),
            html.Div(id='error-output')
        ])
        
        dash_duo.start_server(app)
        
        # Component should still render even without API key
        dash_duo.wait_for_element(".dash-copilotkit-wrapper", timeout=10)

    def test_component_styling(self, dash_duo):
        """Test component custom styling."""
        app = dash.Dash(__name__)
        app.layout = html.Div([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='styled-component',
                ui_type='chat',
                public_api_key='test-key',
                className='custom-class',
                style={
                    'border': '2px solid red',
                    'backgroundColor': 'lightblue',
                    'width': '500px',
                    'height': '300px'
                }
            )
        ])
        
        dash_duo.start_server(app)
        
        # Wait for component to load
        component = dash_duo.wait_for_element(".dash-copilotkit-wrapper", timeout=10)
        
        # Check that custom class is applied
        assert 'custom-class' in component.get_attribute('class')

    def test_component_responsiveness(self, dash_duo):
        """Test component responsiveness to window size changes."""
        app = dash.Dash(__name__)
        app.layout = html.Div([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='responsive-component',
                ui_type='chat',
                public_api_key='test-key',
                width='100%',
                height='50vh'
            )
        ])
        
        dash_duo.start_server(app)
        
        # Wait for component to load
        component = dash_duo.wait_for_element(".dash-copilotkit-wrapper", timeout=10)
        
        # Get initial size
        initial_width = component.size['width']
        
        # Resize window
        dash_duo.driver.set_window_size(800, 600)
        time.sleep(1)  # Allow time for resize
        
        # Component should adapt to new size
        new_width = component.size['width']
        assert new_width <= 800  # Should fit within new window width


class TestComponentCallbacks:
    """Test component callback functionality."""

    def test_textarea_value_callback(self, dash_duo):
        """Test textarea value updates through callbacks."""
        app = dash.Dash(__name__)
        app.layout = html.Div([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='callback-textarea',
                ui_type='textarea',
                public_api_key='test-key',
                value='initial'
            ),
            html.Div(id='callback-output'),
            html.Button('Update', id='update-btn')
        ])
        
        @callback(
            Output('callback-output', 'children'),
            Input('callback-textarea', 'value')
        )
        def display_value(value):
            return f"Value: {value}"
        
        @callback(
            Output('callback-textarea', 'value'),
            Input('update-btn', 'n_clicks'),
            prevent_initial_call=True
        )
        def update_value(n_clicks):
            return f"Updated {n_clicks} times"
        
        dash_duo.start_server(app)
        
        # Wait for initial render
        output = dash_duo.wait_for_element("#callback-output", timeout=10)
        assert "Value: initial" in output.text
        
        # Click update button
        update_btn = dash_duo.find_element("#update-btn")
        update_btn.click()
        
        # Wait for callback to execute
        dash_duo.wait_for_text_to_equal("#callback-output", "Value: Updated 1 times", timeout=5)

    def test_multiple_component_callbacks(self, dash_duo):
        """Test multiple components with independent callbacks."""
        app = dash.Dash(__name__)
        app.layout = html.Div([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='comp1',
                ui_type='textarea',
                public_api_key='test-key',
                value='comp1'
            ),
            dash_copilotkit_components.DashCopilotkitComponents(
                id='comp2',
                ui_type='textarea',
                public_api_key='test-key',
                value='comp2'
            ),
            html.Div(id='output1'),
            html.Div(id='output2')
        ])
        
        @callback(
            Output('output1', 'children'),
            Input('comp1', 'value')
        )
        def update_output1(value):
            return f"Component 1: {value}"
        
        @callback(
            Output('output2', 'children'),
            Input('comp2', 'value')
        )
        def update_output2(value):
            return f"Component 2: {value}"
        
        dash_duo.start_server(app)
        
        # Wait for both outputs to render
        dash_duo.wait_for_text_to_equal("#output1", "Component 1: comp1", timeout=10)
        dash_duo.wait_for_text_to_equal("#output2", "Component 2: comp2", timeout=10)


class TestComponentPerformance:
    """Test component performance characteristics."""

    def test_component_load_time(self, dash_duo):
        """Test component loading performance."""
        app = dash.Dash(__name__)
        app.layout = html.Div([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='perf-component',
                ui_type='chat',
                public_api_key='test-key'
            )
        ])
        
        start_time = time.time()
        dash_duo.start_server(app)
        
        # Wait for component to load
        dash_duo.wait_for_element(".dash-copilotkit-wrapper", timeout=10)
        load_time = time.time() - start_time
        
        # Component should load within reasonable time (10 seconds)
        assert load_time < 10

    def test_multiple_components_performance(self, dash_duo):
        """Test performance with multiple components."""
        app = dash.Dash(__name__)
        
        # Create multiple components
        components = []
        for i in range(5):
            components.append(
                dash_copilotkit_components.DashCopilotkitComponents(
                    id=f'perf-comp-{i}',
                    ui_type='chat',
                    public_api_key='test-key'
                )
            )
        
        app.layout = html.Div(components)
        
        start_time = time.time()
        dash_duo.start_server(app)
        
        # Wait for all components to load
        for i in range(5):
            dash_duo.wait_for_element(f"#perf-comp-{i}", timeout=15)
        
        load_time = time.time() - start_time
        
        # Multiple components should still load within reasonable time
        assert load_time < 20


if __name__ == '__main__':
    pytest.main([__file__])
