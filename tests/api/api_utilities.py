from dataclasses import dataclass

import api
from api.api import auth_api
from api.model.auth_request import AuthRequest
from api.model.auth_response import AuthResponse


@dataclass
class ApiConfig:
    api_key: str
    token: str


def get_api_config(auth_key: str, auth_key_id: str) -> ApiConfig:
    configuration = api.Configuration(host="https://api.soracom.io/v1")  # toriaezu

    with api.ApiClient(configuration=configuration) as api_client:
        api_instance = auth_api.AuthApi(api_client)
        auth_request = AuthRequest(
            auth_key=auth_key,
            auth_key_id=auth_key_id,
        )

        api_response: AuthResponse = api_instance.auth(auth_request)
        assert isinstance(api_response.get("api_key"), str)
        assert isinstance(api_response.get("token"), str)
        assert isinstance(api_response.get("operator_id"), str)
        return ApiConfig(
            api_response.get("api_key"),
            api_response.get("token"),
        )
