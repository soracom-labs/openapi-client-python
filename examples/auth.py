import os

import soracom_api
from soracom_api.api import auth_api
from soracom_api.model.auth_request import AuthRequest
from soracom_api.model.auth_response import AuthResponse

if __name__ == "__main__":
    auth_key = os.environ["SORACOM_AUTH_KEY"]
    auth_key_id = os.environ["SORACOM_AUTH_KEY_ID"]
    configuration = soracom_api.Configuration(host="https://api.soracom.io/v1")

    with soracom_api.ApiClient(configuration=configuration) as api_client:
        auth_request = AuthRequest(
            auth_key=auth_key,
            auth_key_id=auth_key_id,
        )
        api_response: AuthResponse = auth_api.AuthApi(api_client).auth(auth_request)
        print(f"api_key: {api_response.get('api_key')}")
        print(f"api_token: {api_response.get('token')}")
