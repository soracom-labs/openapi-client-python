import os
import time
from pprint import pprint

import soracom_api
from soracom_api.api import auth_api, data_entry_api
from soracom_api.model.auth_request import AuthRequest
from soracom_api.model.auth_response import AuthResponse
from soracom_api.model.data_entry import DataEntry


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
    imsi = os.environ["IMSI"]

    configuration = soracom_api.Configuration(host="https://api.soracom.io/v1")
    configuration.api_key["api_key"], configuration.api_key["api_token"] = auth(auth_key, auth_key_id, configuration)

    with soracom_api.ApiClient(configuration) as api_client:
        api_instance = data_entry_api.DataEntryApi(api_client)
        resource_type = "Subscriber"
        resource_id = imsi
        to = int(time.time() * 1000)  # (unixtime in milliseconds)
        _from = to - 1000 * 60 * 60 * 24 * 7  # 1 week ago
        sort = "desc"
        limit = 3

        try:
            api_response: list[DataEntry] = api_instance.get_data_entries(
                resource_type, resource_id, _from=_from, to=to, sort=sort, limit=limit
            )
            pprint(api_response)
        except soracom_api.ApiException as e:
            print("Exception when calling DataEntryApi->get_data_entries: %s\n" % e)
