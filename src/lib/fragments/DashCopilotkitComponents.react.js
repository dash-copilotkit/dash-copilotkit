import React, { useState, useEffect, useMemo } from 'react';
import PropTypes from 'prop-types';
import { CopilotKit } from '@copilotkit/react-core';
import { CopilotChat, CopilotPopup, CopilotSidebar } from '@copilotkit/react-ui';
import { CopilotTextarea } from '@copilotkit/react-textarea';
import '@copilotkit/react-ui/styles.css';

/**
 * DashCopilotkitComponents is a comprehensive Dash component for CopilotKit integration.
 * It supports all 4 UI types: chat, popup, sidebar, and textarea.
 * The component can use either CopilotKit Cloud API key or bring your own key.
 */
const DashCopilotkitComponents = (props) => {
    const {
        id,
        ui_type,
        api_key,
        runtime_url,
        public_api_key,
        instructions,
        labels,
        placeholder,
        value,
        disabled,
        className,
        style,
        width,
        height,
        position,
        show_initially,
        setProps
    } = props;

    // State for textarea value
    const [textareaValue, setTextareaValue] = useState(value || '');

    // Update textarea value when prop changes
    useEffect(() => {
        if (value !== undefined && value !== textareaValue) {
            setTextareaValue(value);
        }
    }, [value]);

    // Handle textarea changes
    const handleTextareaChange = (newValue) => {
        setTextareaValue(newValue);
        if (setProps) {
            setProps({ value: newValue });
        }
    };

    // Prepare CopilotKit configuration
    const copilotConfig = useMemo(() => {
        const config = {};

        if (runtime_url) {
            config.runtimeUrl = runtime_url;
        }

        if (public_api_key) {
            config.publicApiKey = public_api_key;
        }

        if (api_key) {
            config.apiKey = api_key;
        }

        return config;
    }, [runtime_url, public_api_key, api_key]);

    // Prepare labels configuration
    const chatLabels = useMemo(() => {
        const defaultLabels = {
            title: "AI Assistant",
            initial: "Hi! 👋 How can I assist you today?"
        };

        if (labels && typeof labels === 'object') {
            return { ...defaultLabels, ...labels };
        }

        return defaultLabels;
    }, [labels]);

    // Render different UI types
    const renderCopilotUI = () => {
        const commonProps = {
            instructions: instructions || "You are a helpful AI assistant.",
            labels: chatLabels
        };

        switch (ui_type) {
            case 'chat':
                return (
                    <CopilotChat
                        {...commonProps}
                        className={className}
                        style={{
                            width: width || '100%',
                            height: height || '400px',
                            ...style
                        }}
                    />
                );

            case 'popup':
                return (
                    <CopilotPopup
                        {...commonProps}
                        className={className}
                        style={style}
                        defaultOpen={show_initially}
                    />
                );

            case 'sidebar':
                return (
                    <CopilotSidebar
                        {...commonProps}
                        className={className}
                        style={style}
                        defaultOpen={show_initially}
                        position={position || 'right'}
                    />
                );

            case 'textarea':
                return (
                    <CopilotTextarea
                        value={textareaValue}
                        onChange={handleTextareaChange}
                        placeholder={placeholder || "Type your message here..."}
                        disabled={disabled}
                        className={className}
                        style={{
                            width: width || '100%',
                            height: height || '100px',
                            ...style
                        }}
                        instructions={instructions || "Help the user write better content."}
                    />
                );

            default:
                return (
                    <div className="copilot-error">
                        <p>Invalid UI type: {ui_type}. Please use 'chat', 'popup', 'sidebar', or 'textarea'.</p>
                    </div>
                );
        }
    };

    return (
        <div id={id} className="dash-copilotkit-wrapper">
            <CopilotKit {...copilotConfig}>
                {renderCopilotUI()}
            </CopilotKit>
        </div>
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
