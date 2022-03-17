import soracom_api
from soracom_api.api import auth_api
from soracom_api.model.auth_request import AuthRequest
from soracom_api.model.auth_response import AuthResponse

from .sandbox import get_sandbox_config
from .types import Coverage


def get_api_config_on_production(auth_key: str, auth_key_id: str, coverage: Coverage) -> soracom_api.Configuration:
    configuration = soracom_api.Configuration()
    configuration.host = configuration.get_host_settings()[coverage.value]["url"]

    with soracom_api.ApiClient(configuration=configuration) as api_client:
        api_instance = auth_api.AuthApi(api_client)
        auth_request = AuthRequest(
            auth_key=auth_key,
            auth_key_id=auth_key_id,
        )

        api_response: AuthResponse = api_instance.auth(auth_request)
        assert isinstance(api_response.get("api_key"), str)
        assert isinstance(api_response.get("token"), str)
        assert isinstance(api_response.get("operator_id"), str)

        configuration.api_key["api_key"] = api_response.get("api_key")
        configuration.api_key["api_token"] = api_response.get("token")
        return configuration


def get_api_config_on_sandbox(auth_key: str, auth_key_id: str) -> soracom_api.Configuration:
    sandbox_config = get_sandbox_config(auth_key, auth_key_id)
    return soracom_api.Configuration(
        host=sandbox_config.url,
        api_key={
            "api_key": sandbox_config.auth.get("api_key"),
            "api_token": sandbox_config.auth.get("token"),
        },
    )
