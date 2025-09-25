% Auto-generated: do not edit by hand
\name{'ckc'DashCopilotkitComponents}

\alias{'ckc'DashCopilotkitComponents}

\title{DashCopilotkitComponents component}

\description{
DashCopilotkitComponents is a comprehensive Dash component for CopilotKit integration. It supports all 4 UI types: chat, popup, sidebar, and textarea. The component can use either CopilotKit Cloud API key or bring your own key.
}

\usage{
'ckc'DashCopilotkitComponents(id=NULL, api_key=NULL, className=NULL, disabled=NULL,
height=NULL, instructions=NULL, labels=NULL,
placeholder=NULL, position=NULL, public_api_key=NULL,
runtime_url=NULL, show_initially=NULL, style=NULL,
ui_type=NULL, value=NULL, width=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{api_key}{Character. Your API key for the language model (when bringing your own key).}

\item{className}{Character. CSS class name for styling.}

\item{disabled}{Logical. Whether the component is disabled.}

\item{height}{Character. Height of the component.}

\item{instructions}{Character. Custom instructions for the AI assistant.}

\item{labels}{Named list. Labels configuration for the chat interface.
Should be an object with 'title' and 'initial' properties.}

\item{placeholder}{Character. Placeholder text for textarea mode.}

\item{position}{A value equal to: 'left', 'right'. Position for sidebar mode ('left' or 'right').}

\item{public_api_key}{Character. Your CopilotKit Cloud public API key.}

\item{runtime_url}{Character. The runtime URL for CopilotKit backend.}

\item{show_initially}{Logical. Whether to show popup/sidebar initially.}

\item{style}{Named list. Inline styles object.}

\item{ui_type}{A value equal to: 'chat', 'popup', 'sidebar', 'textarea'. The type of CopilotKit UI to render.
Options: 'chat', 'popup', 'sidebar', 'textarea'}

\item{value}{Character. The current value (for textarea mode).}

\item{width}{Character. Width of the component.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

