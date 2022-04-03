import soracom_api
from soracom_api.api import auth_api
from soracom_api.model.auth_request import AuthRequest
from soracom_api.model.auth_response import AuthResponse

from .types import Coverage


def auth(auth_key: str, auth_key_id: str, coverage: Coverage) -> soracom_api.Configuration:
    with soracom_api.ApiClient(configuration=soracom_api.Configuration(host=coverage.value)) as api_client:
        auth_request = AuthRequest(
            auth_key=auth_key,
            auth_key_id=auth_key_id,
        )
        api_response: AuthResponse = auth_api.AuthApi(api_client).auth(auth_request)

        return soracom_api.Configuration(
            host=coverage.value,
            api_key={"api_key": api_response.get("api_key"), "api_token": api_response.get("token")},
        )
