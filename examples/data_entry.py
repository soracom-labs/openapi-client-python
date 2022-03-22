import os
import time
from pprint import pprint

import helpers
import soracom_api
from soracom_api.api import data_entry_api
from soracom_api.model.data_entry import DataEntry

if __name__ == "__main__":
    imsi = os.environ["SORACOM_IMSI"]
    now = int(time.time() * 1000)  # (unixtime in milliseconds)

    config = helpers.get_auth_config()
    with soracom_api.ApiClient(config) as api_client:
        api_instance = data_entry_api.DataEntryApi(api_client)
        api_response: list[DataEntry] = api_instance.get_data_entries(
            resource_type="Subscriber",
            resource_id=imsi,
            _from=now - 1000 * 60 * 60 * 24 * 7,  # 1 week ago
            to=now,
            sort="desc",
            limit=3,
        )
        pprint(api_response)
