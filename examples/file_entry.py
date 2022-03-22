import os
from pprint import pprint

import helpers
import soracom_api
from soracom_api.api import file_entry_api
from soracom_api.model.file_entry import FileEntry

if __name__ == "__main__":
    prefix = os.environ["PREFIX"]

    config = helpers.get_auth_config()
    with soracom_api.ApiClient(config) as api_client:
        api_instance = file_entry_api.FileEntryApi(api_client)
        api_response: list[FileEntry] = api_instance.find_files(
            scope="private",  # str | Scope of the request
            prefix=prefix,
            limit="3",  # str | Num of entries (optional) if omitted the server will use the default value of "10"
        )
        pprint(api_response)
