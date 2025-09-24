# AUTO GENERATED FILE - DO NOT EDIT

#' @export
'ckc'DashCopilotkitComponents <- function(id=NULL, label=NULL, value=NULL) {
    
    props <- list(id=id, label=label, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashCopilotkitComponents',
        namespace = 'dash_copilotkit_components',
        propNames = c('id', 'label', 'value'),
        package = 'dashCopilotkitComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
