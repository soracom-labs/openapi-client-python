import os
from pprint import pprint

import soracom_api
from soracom_api.api import auth_api, file_entry_api
from soracom_api.model.auth_request import AuthRequest
from soracom_api.model.auth_response import AuthResponse
from soracom_api.model.file_entry import FileEntry


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
    prefix = os.environ["PREFIX"]

    configuration = soracom_api.Configuration(host="https://api.soracom.io/v1")
    configuration.api_key["api_key"], configuration.api_key["api_token"] = auth(auth_key, auth_key_id, configuration)

    with soracom_api.ApiClient(configuration) as api_client:
        api_instance = file_entry_api.FileEntryApi(api_client)
        scope = "private"  # str | Scope of the request
        limit = "10"  # str | Num of entries (optional) if omitted the server will use the default value of "10"

        try:
            api_response: list[FileEntry] = api_instance.find_files(scope, prefix, limit=limit)
            pprint(api_response)
        except soracom_api.ApiException as e:
            print("Exception when calling FileEntryApi->find_files: %s\n" % e)
