# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class DashCopilotkitComponents(Component):
    """A DashCopilotkitComponents component.
DashCopilotkitComponents is a comprehensive Dash component for CopilotKit integration.
It supports all 4 UI types: chat, popup, sidebar, and textarea.
The component can use either CopilotKit Cloud API key or bring your own key.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- api_key (string; optional):
    Your API key for the language model (when bringing your own key).

- className (string; optional):
    CSS class name for styling.

- disabled (boolean; default False):
    Whether the component is disabled.

- height (string; default '400px'):
    Height of the component.

- instructions (string; default "You are a helpful AI assistant."):
    Custom instructions for the AI assistant.

- labels (dict; optional):
    Labels configuration for the chat interface.  Should be an object
    with 'title' and 'initial' properties.

- placeholder (string; default "Type your message here..."):
    Placeholder text for textarea mode.

- position (a value equal to: 'left', 'right'; default 'right'):
    Position for sidebar mode ('left' or 'right').

- public_api_key (string; optional):
    Your CopilotKit Cloud public API key.

- runtime_url (string; optional):
    The runtime URL for CopilotKit backend.

- show_initially (boolean; default False):
    Whether to show popup/sidebar initially.

- ui_type (a value equal to: 'chat', 'popup', 'sidebar', 'textarea'; default 'chat'):
    The type of CopilotKit UI to render.  Options: 'chat', 'popup',
    'sidebar', 'textarea'.

- value (string; optional):
    The current value (for textarea mode).

- width (string; default '100%'):
    Width of the component."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_copilotkit_components'
    _type = 'DashCopilotkitComponents'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        ui_type: typing.Optional[Literal["chat", "popup", "sidebar", "textarea"]] = None,
        api_key: typing.Optional[str] = None,
        runtime_url: typing.Optional[str] = None,
        public_api_key: typing.Optional[str] = None,
        instructions: typing.Optional[str] = None,
        labels: typing.Optional[dict] = None,
        placeholder: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        disabled: typing.Optional[bool] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        width: typing.Optional[str] = None,
        height: typing.Optional[str] = None,
        position: typing.Optional[Literal["left", "right"]] = None,
        show_initially: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'api_key', 'className', 'disabled', 'height', 'instructions', 'labels', 'placeholder', 'position', 'public_api_key', 'runtime_url', 'show_initially', 'style', 'ui_type', 'value', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'api_key', 'className', 'disabled', 'height', 'instructions', 'labels', 'placeholder', 'position', 'public_api_key', 'runtime_url', 'show_initially', 'style', 'ui_type', 'value', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashCopilotkitComponents, self).__init__(**args)

setattr(DashCopilotkitComponents, "__init__", _explicitize_args(DashCopilotkitComponents.__init__))
