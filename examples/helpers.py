import os
from enum import Enum

import soracom_api
from soracom_api.api import auth_api
from soracom_api.model.auth_request import AuthRequest
from soracom_api.model.auth_response import AuthResponse


class Coverage(Enum):
    JAPAN = "https://api.soracom.io/v1"
    GLOBAL = "https://g.api.soracom.io/v1"


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


def get_auth_config() -> soracom_api.Configuration:
    auth_key = os.environ["SORACOM_AUTH_KEY"]
    auth_key_id = os.environ["SORACOM_AUTH_KEY_ID"]
    return auth(
        auth_key=auth_key,
        auth_key_id=auth_key_id,
        coverage=Coverage.JAPAN,
    )
