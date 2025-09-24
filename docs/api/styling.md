# Styling

Learn how to customize the appearance of Dash CopilotKit Components with CSS classes, inline styles, and theming.

## Overview

Dash CopilotKit Components can be styled using:

- **CSS Classes**: Apply custom CSS classes via the `className` prop
- **Inline Styles**: Use the `style` prop for direct styling
- **CSS Variables**: Customize component themes with CSS custom properties
- **Global Styles**: Apply styles through external stylesheets

## Basic Styling

### Using className

```python
import dash_copilotkit_components

# Apply a custom CSS class
dash_copilotkit_components.DashCopilotkitComponents(
    id='styled-chat',
    ui_type='chat',
    public_api_key='your-api-key',
    className='custom-chat-style'
)
```

```css
/* In your CSS file or <style> tag */
.custom-chat-style {
    border: 2px solid #007bff;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 123, 255, 0.15);
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
}
```

### Using Inline Styles

```python
dash_copilotkit_components.DashCopilotkitComponents(
    id='inline-styled-chat',
    ui_type='chat',
    public_api_key='your-api-key',
    style={
        'border': '2px solid #28a745',
        'borderRadius': '15px',
        'boxShadow': '0 6px 20px rgba(40, 167, 69, 0.2)',
        'backgroundColor': '#f8fff9',
        'fontFamily': 'Inter, sans-serif'
    }
)
```

## CSS Variables and Theming

### Available CSS Variables

The component supports CSS custom properties for consistent theming:

```css
:root {
    /* Colors */
    --copilot-primary-color: #007bff;
    --copilot-secondary-color: #6c757d;
    --copilot-background-color: #ffffff;
    --copilot-text-color: #212529;
    --copilot-border-color: #dee2e6;
    
    /* Typography */
    --copilot-font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --copilot-font-size: 14px;
    --copilot-line-height: 1.5;
    
    /* Spacing */
    --copilot-padding: 16px;
    --copilot-margin: 8px;
    --copilot-border-radius: 8px;
    
    /* Shadows */
    --copilot-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    --copilot-shadow-hover: 0 4px 16px rgba(0, 0, 0, 0.15);
}
```

### Dark Theme Example

```css
/* Dark theme */
.dark-theme {
    --copilot-primary-color: #0d6efd;
    --copilot-secondary-color: #6c757d;
    --copilot-background-color: #212529;
    --copilot-text-color: #ffffff;
    --copilot-border-color: #495057;
}

.dark-theme .copilot-component {
    background-color: var(--copilot-background-color);
    color: var(--copilot-text-color);
    border-color: var(--copilot-border-color);
}
```

## UI Type Specific Styling

### Chat Interface

```css
.chat-interface {
    /* Chat container */
    max-width: 800px;
    margin: 0 auto;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    overflow: hidden;
}

.chat-interface .chat-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 16px;
    font-weight: 600;
}

.chat-interface .chat-messages {
    max-height: 400px;
    overflow-y: auto;
    padding: 16px;
}

.chat-interface .chat-input {
    border-top: 1px solid #e0e0e0;
    padding: 16px;
    background: #f8f9fa;
}
```

### Popup Chat

```css
.popup-chat {
    /* Popup positioning */
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 350px;
    max-height: 500px;
    z-index: 1000;
    
    /* Styling */
    background: white;
    border-radius: 16px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
    border: 1px solid rgba(0, 0, 0, 0.08);
}

.popup-chat .popup-trigger {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: #007bff;
    color: white;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 16px rgba(0, 123, 255, 0.3);
    transition: all 0.3s ease;
}

.popup-chat .popup-trigger:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 20px rgba(0, 123, 255, 0.4);
}
```

### Sidebar Chat

```css
.sidebar-chat {
    /* Sidebar positioning */
    position: fixed;
    top: 0;
    right: -350px; /* Hidden by default */
    width: 350px;
    height: 100vh;
    background: white;
    box-shadow: -4px 0 16px rgba(0, 0, 0, 0.1);
    transition: right 0.3s ease;
    z-index: 1000;
}

.sidebar-chat.open {
    right: 0; /* Slide in */
}

.sidebar-chat.left {
    left: -350px;
    right: auto;
    box-shadow: 4px 0 16px rgba(0, 0, 0, 0.1);
}

.sidebar-chat.left.open {
    left: 0;
}

/* Backdrop */
.sidebar-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
    z-index: 999;
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
}

.sidebar-backdrop.visible {
    opacity: 1;
    visibility: visible;
}
```

### AI Textarea

```css
.ai-textarea {
    /* Textarea styling */
    width: 100%;
    min-height: 120px;
    padding: 16px;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    font-family: inherit;
    font-size: 14px;
    line-height: 1.5;
    resize: vertical;
    transition: border-color 0.2s ease;
}

.ai-textarea:focus {
    outline: none;
    border-color: #007bff;
    box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.1);
}

.ai-textarea::placeholder {
    color: #6c757d;
    font-style: italic;
}

/* AI suggestions indicator */
.ai-textarea.ai-active {
    border-color: #28a745;
    background: linear-gradient(90deg, #f8fff9 0%, #ffffff 100%);
}
```

## Responsive Design

### Mobile-First Approach

```css
/* Mobile styles (default) */
.copilot-component {
    width: 100%;
    max-width: none;
    margin: 0;
    border-radius: 0;
}

/* Tablet styles */
@media (min-width: 768px) {
    .copilot-component {
        max-width: 600px;
        margin: 0 auto;
        border-radius: 12px;
    }
    
    .popup-chat {
        width: 400px;
        max-height: 600px;
    }
    
    .sidebar-chat {
        width: 400px;
    }
}

/* Desktop styles */
@media (min-width: 1024px) {
    .copilot-component {
        max-width: 800px;
    }
    
    .chat-interface {
        height: 500px;
    }
}
```

### Mobile-Specific Adjustments

```css
@media (max-width: 767px) {
    /* Full-screen popup on mobile */
    .popup-chat {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        width: 100vw;
        height: 100vh;
        max-height: none;
        border-radius: 0;
    }
    
    /* Full-width sidebar on mobile */
    .sidebar-chat {
        width: 100vw;
        left: -100vw;
        right: auto;
    }
    
    .sidebar-chat.open {
        left: 0;
    }
    
    /* Larger touch targets */
    .chat-input button {
        min-height: 44px;
        min-width: 44px;
    }
}
```

## Animation and Transitions

### Smooth Animations

```css
.copilot-component {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Fade in animation */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.copilot-component.animate-in {
    animation: fadeIn 0.5s ease-out;
}

/* Slide animations for sidebar */
@keyframes slideInRight {
    from {
        transform: translateX(100%);
    }
    to {
        transform: translateX(0);
    }
}

.sidebar-chat.animate-slide {
    animation: slideInRight 0.3s ease-out;
}
```

### Loading States

```css
.copilot-loading {
    position: relative;
    opacity: 0.7;
    pointer-events: none;
}

.copilot-loading::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 20px;
    height: 20px;
    margin: -10px 0 0 -10px;
    border: 2px solid #f3f3f3;
    border-top: 2px solid #007bff;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
```

## Integration with CSS Frameworks

### Bootstrap Integration

```python
import dash_bootstrap_components as dbc
import dash_copilotkit_components

# Using Bootstrap classes
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dash_copilotkit_components.DashCopilotkitComponents(
                id='bootstrap-chat',
                ui_type='chat',
                public_api_key='your-api-key',
                className='shadow-lg border-0 rounded-3'
            )
        ], md=8, className='mx-auto')
    ])
])
```

### Tailwind CSS Integration

```python
# Using Tailwind classes
dash_copilotkit_components.DashCopilotkitComponents(
    id='tailwind-chat',
    ui_type='chat',
    public_api_key='your-api-key',
    className='shadow-xl border-0 rounded-xl bg-white max-w-2xl mx-auto'
)
```

## Custom Themes

### Corporate Theme

```css
.corporate-theme {
    --copilot-primary-color: #003366;
    --copilot-secondary-color: #666666;
    --copilot-background-color: #ffffff;
    --copilot-text-color: #333333;
    --copilot-border-color: #cccccc;
    --copilot-font-family: 'Roboto', sans-serif;
    --copilot-border-radius: 4px;
}

.corporate-theme .copilot-component {
    font-family: var(--copilot-font-family);
    border: 1px solid var(--copilot-border-color);
    border-radius: var(--copilot-border-radius);
}
```

### Playful Theme

```css
.playful-theme {
    --copilot-primary-color: #ff6b6b;
    --copilot-secondary-color: #4ecdc4;
    --copilot-background-color: #fff9f9;
    --copilot-text-color: #2c3e50;
    --copilot-border-color: #ffb3b3;
    --copilot-font-family: 'Comic Sans MS', cursive;
    --copilot-border-radius: 20px;
}

.playful-theme .copilot-component {
    background: linear-gradient(135deg, #fff9f9 0%, #f0f8ff 100%);
    border: 3px solid var(--copilot-border-color);
    border-radius: var(--copilot-border-radius);
}
```

## Best Practices

1. **Use CSS Variables**: For consistent theming across components
2. **Mobile-First**: Design for mobile devices first, then enhance for larger screens
3. **Accessibility**: Ensure sufficient color contrast and focus indicators
4. **Performance**: Avoid complex animations on mobile devices
5. **Consistency**: Maintain consistent styling across all UI types

## Troubleshooting

### Common Issues

**Styles not applying:**
- Check CSS selector specificity
- Ensure className prop is set correctly
- Verify CSS is loaded after component styles

**Mobile display issues:**
- Test on actual devices, not just browser dev tools
- Use appropriate viewport meta tag
- Consider touch target sizes (minimum 44px)

**Animation performance:**
- Use `transform` and `opacity` for smooth animations
- Avoid animating layout properties like `width` and `height`
- Use `will-change` property sparingly

## Next Steps

- [Examples](../examples/styling.md) - See styling examples in action
- [Contributing](../contributing/development.md) - Learn about component development
