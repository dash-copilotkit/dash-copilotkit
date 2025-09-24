# AUTO GENERATED FILE - DO NOT EDIT

#' @export
ckcDashCopilotkitComponents <- function(id=NULL, api_key=NULL, className=NULL, disabled=NULL, height=NULL, instructions=NULL, labels=NULL, placeholder=NULL, position=NULL, public_api_key=NULL, runtime_url=NULL, show_initially=NULL, style=NULL, ui_type=NULL, value=NULL, width=NULL) {
    
    props <- list(id=id, api_key=api_key, className=className, disabled=disabled, height=height, instructions=instructions, labels=labels, placeholder=placeholder, position=position, public_api_key=public_api_key, runtime_url=runtime_url, show_initially=show_initially, style=style, ui_type=ui_type, value=value, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashCopilotkitComponents',
        namespace = 'dash_copilotkit_components',
        propNames = c('id', 'api_key', 'className', 'disabled', 'height', 'instructions', 'labels', 'placeholder', 'position', 'public_api_key', 'runtime_url', 'show_initially', 'style', 'ui_type', 'value', 'width'),
        package = 'dashCopilotkitComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
