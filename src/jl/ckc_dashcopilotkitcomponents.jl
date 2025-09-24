# AUTO GENERATED FILE - DO NOT EDIT

export ckc_dashcopilotkitcomponents

"""
    ckc_dashcopilotkitcomponents(;kwargs...)

A DashCopilotkitComponents component.
DashCopilotkitComponents is a comprehensive Dash component for CopilotKit integration.
It supports all 4 UI types: chat, popup, sidebar, and textarea.
The component can use either CopilotKit Cloud API key or bring your own key.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `api_key` (String; optional): Your API key for the language model (when bringing your own key).
- `className` (String; optional): CSS class name for styling.
- `disabled` (Bool; optional): Whether the component is disabled.
- `height` (String; optional): Height of the component.
- `instructions` (String; optional): Custom instructions for the AI assistant.
- `labels` (Dict; optional): Labels configuration for the chat interface.
Should be an object with 'title' and 'initial' properties.
- `placeholder` (String; optional): Placeholder text for textarea mode.
- `position` (a value equal to: 'left', 'right'; optional): Position for sidebar mode ('left' or 'right').
- `public_api_key` (String; optional): Your CopilotKit Cloud public API key.
- `runtime_url` (String; optional): The runtime URL for CopilotKit backend.
- `show_initially` (Bool; optional): Whether to show popup/sidebar initially.
- `style` (Dict; optional): Inline styles object.
- `ui_type` (a value equal to: 'chat', 'popup', 'sidebar', 'textarea'; optional): The type of CopilotKit UI to render.
Options: 'chat', 'popup', 'sidebar', 'textarea'
- `value` (String; optional): The current value (for textarea mode).
- `width` (String; optional): Width of the component.
"""
function ckc_dashcopilotkitcomponents(; kwargs...)
        available_props = Symbol[:id, :api_key, :className, :disabled, :height, :instructions, :labels, :placeholder, :position, :public_api_key, :runtime_url, :show_initially, :style, :ui_type, :value, :width]
        wild_props = Symbol[]
        return Component("ckc_dashcopilotkitcomponents", "DashCopilotkitComponents", "dash_copilotkit_components", available_props, wild_props; kwargs...)
end

