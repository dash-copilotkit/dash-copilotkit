import React from 'react';
import PropTypes from 'prop-types';
import { DashCopilotkitComponents as RealComponent } from '../LazyLoader';

/**
 * DashCopilotkitComponents is a comprehensive Dash component for CopilotKit integration.
 * It supports all 4 UI types: chat, popup, sidebar, and textarea.
 * The component can use either CopilotKit Cloud API key or bring your own key.
 */
const DashCopilotkitComponents = (props) => {
    return (
        <React.Suspense fallback={<div>Loading CopilotKit...</div>}>
            <RealComponent {...props}/>
        </React.Suspense>
    );
};

DashCopilotkitComponents.defaultProps = {
    ui_type: 'chat',
    instructions: "You are a helpful AI assistant.",
    placeholder: "Type your message here...",
    disabled: false,
    position: 'right',
    show_initially: false,
    width: '100%',
    height: '400px'
};

DashCopilotkitComponents.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The type of CopilotKit UI to render.
     * Options: 'chat', 'popup', 'sidebar', 'textarea'
     */
    ui_type: PropTypes.oneOf(['chat', 'popup', 'sidebar', 'textarea']),

    /**
     * Your API key for the language model (when bringing your own key).
     */
    api_key: PropTypes.string,

    /**
     * The runtime URL for CopilotKit backend.
     */
    runtime_url: PropTypes.string,

    /**
     * Your CopilotKit Cloud public API key.
     */
    public_api_key: PropTypes.string,

    /**
     * Custom instructions for the AI assistant.
     */
    instructions: PropTypes.string,

    /**
     * Labels configuration for the chat interface.
     * Should be an object with 'title' and 'initial' properties.
     */
    labels: PropTypes.object,

    /**
     * Placeholder text for textarea mode.
     */
    placeholder: PropTypes.string,

    /**
     * The current value (for textarea mode).
     */
    value: PropTypes.string,

    /**
     * Whether the component is disabled.
     */
    disabled: PropTypes.bool,

    /**
     * CSS class name for styling.
     */
    className: PropTypes.string,

    /**
     * Inline styles object.
     */
    style: PropTypes.object,

    /**
     * Width of the component.
     */
    width: PropTypes.string,

    /**
     * Height of the component.
     */
    height: PropTypes.string,

    /**
     * Position for sidebar mode ('left' or 'right').
     */
    position: PropTypes.oneOf(['left', 'right']),

    /**
     * Whether to show popup/sidebar initially.
     */
    show_initially: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default DashCopilotkitComponents;

export const defaultProps = DashCopilotkitComponents.defaultProps;
export const propTypes = DashCopilotkitComponents.propTypes;
