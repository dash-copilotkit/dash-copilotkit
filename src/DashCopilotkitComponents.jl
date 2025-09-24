
module DashCopilotkitComponents
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/ckc_dashcopilotkitcomponents.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_copilotkit_components",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "async-DashCopilotkitComponents.js",
    external_url = "https://unpkg.com/dash_copilotkit_components@0.0.1/dash_copilotkit_components/async-DashCopilotkitComponents.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DashCopilotkitComponents.js.map",
    external_url = "https://unpkg.com/dash_copilotkit_components@0.0.1/dash_copilotkit_components/async-DashCopilotkitComponents.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_copilotkit_components.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_copilotkit_components.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
