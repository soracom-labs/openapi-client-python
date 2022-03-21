import os
from pprint import pprint

import soracom_api
from soracom_api.api import auth_api, sim_api
from soracom_api.model.auth_request import AuthRequest
from soracom_api.model.auth_response import AuthResponse
from soracom_api.model.sim import Sim


def auth(auth_key: str, auth_key_id: str, configuration: soracom_api.Configuration) -> tuple[str, str]:
    with soracom_api.ApiClient(configuration=configuration) as api_client:
        auth_request = AuthRequest(
            auth_key=auth_key,
            auth_key_id=auth_key_id,
        )
        api_response: AuthResponse = auth_api.AuthApi(api_client).auth(auth_request)
        return api_response.get("api_key"), api_response.get("token")


if __name__ == "__main__":
    auth_key = os.environ["SORACOM_AUTH_KEY"]
    auth_key_id = os.environ["SORACOM_AUTH_KEY_ID"]

    configuration = soracom_api.Configuration(host="https://api.soracom.io/v1")
    configuration.api_key["api_key"], configuration.api_key["api_token"] = auth(auth_key, auth_key_id, configuration)

    with soracom_api.ApiClient(configuration) as api_client:
        api_instance = sim_api.SimApi(api_client)
        limit = 3

        try:
            api_response: list[Sim] = api_instance.list_sims(limit=limit)
            pprint(api_response)
        except soracom_api.ApiException as e:
            print("Exception when calling SimApi->list_sims: %s\n" % e)
