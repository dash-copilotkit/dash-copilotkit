#!/usr/bin/env python3
"""
Simple test script to verify the Dash CopilotKit component works correctly.
"""

import dash_copilotkit_components
from dash import Dash, html, dcc, callback, Input, Output

def test_component_import():
    """Test that the component can be imported successfully."""
    print("✓ Component imported successfully")
    return True

def test_component_creation():
    """Test that the component can be created with different configurations."""
    
    # Test basic chat component
    chat_component = dash_copilotkit_components.DashCopilotkitComponents(
        id='test-chat',
        ui_type='chat',
        instructions="Test instructions"
    )
    print("✓ Chat component created successfully")
    
    # Test popup component
    popup_component = dash_copilotkit_components.DashCopilotkitComponents(
        id='test-popup',
        ui_type='popup',
        show_initially=False
    )
    print("✓ Popup component created successfully")
    
    # Test sidebar component
    sidebar_component = dash_copilotkit_components.DashCopilotkitComponents(
        id='test-sidebar',
        ui_type='sidebar',
        position='right'
    )
    print("✓ Sidebar component created successfully")
    
    # Test textarea component
    textarea_component = dash_copilotkit_components.DashCopilotkitComponents(
        id='test-textarea',
        ui_type='textarea',
        placeholder='Test placeholder',
        value='Test value'
    )
    print("✓ Textarea component created successfully")
    
    return True

def test_dash_app():
    """Test that a Dash app can be created with the component."""
    
    app = Dash(__name__)
    
    app.layout = html.Div([
        html.H1("CopilotKit Component Test"),
        
        html.Div([
            html.Label("Select UI Type:"),
            dcc.Dropdown(
                id='ui-type-dropdown',
                options=[
                    {'label': 'Chat', 'value': 'chat'},
                    {'label': 'Popup', 'value': 'popup'},
                    {'label': 'Sidebar', 'value': 'sidebar'},
                    {'label': 'Textarea', 'value': 'textarea'}
                ],
                value='chat'
            )
        ], style={'margin': '20px'}),
        
        html.Div(id='component-container'),
        html.Div(id='output')
    ])
    
    @callback(
        Output('component-container', 'children'),
        Input('ui-type-dropdown', 'value')
    )
    def update_component(ui_type):
        return dash_copilotkit_components.DashCopilotkitComponents(
            id='test-component',
            ui_type=ui_type,
            instructions=f"You are a test AI assistant in {ui_type} mode.",
            labels={
                'title': f'Test {ui_type.title()} Assistant',
                'initial': f'Hello from {ui_type} mode!'
            }
        )
    
    @callback(
        Output('output', 'children'),
        Input('test-component', 'value'),
        prevent_initial_call=True
    )
    def display_output(value):
        if value:
            return f'Component value: {value}'
        return ''
    
    print("✓ Dash app created successfully with component")
    return app

def run_tests():
    """Run all tests."""
    print("Running Dash CopilotKit Component Tests...")
    print("=" * 50)
    
    try:
        # Test 1: Import
        test_component_import()
        
        # Test 2: Component creation
        test_component_creation()
        
        # Test 3: Dash app integration
        app = test_dash_app()
        
        print("=" * 50)
        print("✅ All tests passed!")
        print("\nTo test the component interactively:")
        print("1. Run: python test_component.py --interactive")
        print("2. Visit: http://localhost:8050")
        print("3. Try different UI types and configurations")
        
        return app
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == '__main__':
    import sys
    
    app = run_tests()
    
    if app and '--interactive' in sys.argv:
        print("\nStarting interactive test server...")
        app.run(debug=True, port=8050)
