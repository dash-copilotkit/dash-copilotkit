"""
Basic unit tests for Dash CopilotKit Components without browser dependencies.
"""
import pytest
import dash
from dash import html
import dash_copilotkit_components


class TestBasicComponent:
    """Basic tests for DashCopilotkitComponents."""

    def test_component_import(self):
        """Test that the component can be imported successfully."""
        assert hasattr(dash_copilotkit_components, 'DashCopilotkitComponents')
        component_class = dash_copilotkit_components.DashCopilotkitComponents
        assert component_class is not None

    def test_component_instantiation_default(self):
        """Test component instantiation with default props."""
        component = dash_copilotkit_components.DashCopilotkitComponents(
            id='test-component'
        )
        
        assert component.id == 'test-component'
        # Note: Default values are set in React component, not Python
        # So we can't test them here directly

    def test_component_instantiation_chat(self):
        """Test component instantiation with chat UI type."""
        component = dash_copilotkit_components.DashCopilotkitComponents(
            id='chat-component',
            ui_type='chat',
            public_api_key='test-key',
            instructions='You are a chat assistant.',
            labels={'title': 'Chat Bot', 'initial': 'Hello!'}
        )
        
        assert component.id == 'chat-component'
        assert component.ui_type == 'chat'
        assert component.public_api_key == 'test-key'
        assert component.instructions == 'You are a chat assistant.'
        assert component.labels == {'title': 'Chat Bot', 'initial': 'Hello!'}

    def test_component_instantiation_popup(self):
        """Test component instantiation with popup UI type."""
        component = dash_copilotkit_components.DashCopilotkitComponents(
            id='popup-component',
            ui_type='popup',
            public_api_key='test-key',
            show_initially=True
        )
        
        assert component.id == 'popup-component'
        assert component.ui_type == 'popup'
        assert component.show_initially is True

    def test_component_instantiation_sidebar(self):
        """Test component instantiation with sidebar UI type."""
        component = dash_copilotkit_components.DashCopilotkitComponents(
            id='sidebar-component',
            ui_type='sidebar',
            position='left',
            show_initially=True,
            width='300px'
        )
        
        assert component.id == 'sidebar-component'
        assert component.ui_type == 'sidebar'
        assert component.position == 'left'
        assert component.show_initially is True
        assert component.width == '300px'

    def test_component_instantiation_textarea(self):
        """Test component instantiation with textarea UI type."""
        component = dash_copilotkit_components.DashCopilotkitComponents(
            id='textarea-component',
            ui_type='textarea',
            placeholder='Start typing...',
            value='Initial text',
            height='200px'
        )
        
        assert component.id == 'textarea-component'
        assert component.ui_type == 'textarea'
        assert component.placeholder == 'Start typing...'
        assert component.value == 'Initial text'
        assert component.height == '200px'

    def test_component_with_custom_styling(self):
        """Test component with custom styling."""
        custom_style = {'backgroundColor': 'blue', 'border': '1px solid red'}
        component = dash_copilotkit_components.DashCopilotkitComponents(
            id='styled-component',
            className='custom-class',
            style=custom_style
        )
        
        assert component.className == 'custom-class'
        assert component.style == custom_style

    def test_component_with_api_configurations(self):
        """Test component with different API configurations."""
        # Test with public API key
        component1 = dash_copilotkit_components.DashCopilotkitComponents(
            id='component1',
            public_api_key='public-key-123'
        )
        assert component1.public_api_key == 'public-key-123'
        
        # Test with custom API key
        component2 = dash_copilotkit_components.DashCopilotkitComponents(
            id='component2',
            api_key='custom-api-key'
        )
        assert component2.api_key == 'custom-api-key'
        
        # Test with runtime URL
        component3 = dash_copilotkit_components.DashCopilotkitComponents(
            id='component3',
            runtime_url='https://custom-runtime.com'
        )
        assert component3.runtime_url == 'https://custom-runtime.com'

    def test_component_in_dash_app(self):
        """Test component integration in a Dash app."""
        app = dash.Dash(__name__)
        
        app.layout = html.Div([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='app-component',
                ui_type='chat',
                public_api_key='test-key'
            ),
            html.Div(id='output')
        ])
        
        # Test that app layout is created successfully
        assert app.layout is not None
        assert len(app.layout.children) == 2

    def test_component_with_all_props(self):
        """Test component with all possible props."""
        component = dash_copilotkit_components.DashCopilotkitComponents(
            id='full-component',
            ui_type='textarea',
            api_key='api-key',
            runtime_url='https://runtime.com',
            public_api_key='public-key',
            instructions='Custom instructions',
            labels={'title': 'Test', 'initial': 'Hi'},
            placeholder='Type here',
            value='Initial value',
            disabled=False,
            className='test-class',
            style={'color': 'red'},
            width='500px',
            height='300px',
            position='left',
            show_initially=True
        )
        
        # Verify all props are set correctly
        assert component.id == 'full-component'
        assert component.ui_type == 'textarea'
        assert component.api_key == 'api-key'
        assert component.runtime_url == 'https://runtime.com'
        assert component.public_api_key == 'public-key'
        assert component.instructions == 'Custom instructions'
        assert component.labels == {'title': 'Test', 'initial': 'Hi'}
        assert component.placeholder == 'Type here'
        assert component.value == 'Initial value'
        assert component.disabled is False
        assert component.className == 'test-class'
        assert component.style == {'color': 'red'}
        assert component.width == '500px'
        assert component.height == '300px'
        assert component.position == 'left'
        assert component.show_initially is True

    def test_multiple_components_in_app(self):
        """Test multiple components in the same app."""
        app = dash.Dash(__name__)
        
        app.layout = html.Div([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='chat-comp',
                ui_type='chat'
            ),
            dash_copilotkit_components.DashCopilotkitComponents(
                id='textarea-comp',
                ui_type='textarea'
            ),
            dash_copilotkit_components.DashCopilotkitComponents(
                id='sidebar-comp',
                ui_type='sidebar'
            )
        ])
        
        assert len(app.layout.children) == 3

    def test_component_props_types(self):
        """Test component prop types."""
        component = dash_copilotkit_components.DashCopilotkitComponents(
            id='type-test',
            ui_type='chat',
            disabled=False,
            show_initially=True,
            width='100%',
            height='400px'
        )
        
        # Test that boolean props are actually boolean
        assert isinstance(component.disabled, bool)
        assert isinstance(component.show_initially, bool)
        
        # Test that string props are strings
        assert isinstance(component.ui_type, str)
        assert isinstance(component.width, str)
        assert isinstance(component.height, str)

    def test_component_namespace(self):
        """Test component namespace and type."""
        component = dash_copilotkit_components.DashCopilotkitComponents(
            id='namespace-test'
        )
        
        # Check component metadata
        assert hasattr(component, '_namespace')
        assert hasattr(component, '_type')
        assert component._namespace == 'dash_copilotkit_components'
        assert component._type == 'DashCopilotkitComponents'

    def test_component_available_properties(self):
        """Test that component has expected available properties."""
        component = dash_copilotkit_components.DashCopilotkitComponents(
            id='props-test'
        )
        
        expected_props = [
            'id', 'ui_type', 'api_key', 'runtime_url', 'public_api_key',
            'instructions', 'labels', 'placeholder', 'value', 'disabled',
            'className', 'style', 'width', 'height', 'position', 'show_initially'
        ]
        
        for prop in expected_props:
            assert prop in component.available_properties, f"Property '{prop}' not found in available_properties"


if __name__ == '__main__':
    pytest.main([__file__])
