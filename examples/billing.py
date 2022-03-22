from pprint import pprint

import helpers
import soracom_api
from soracom_api.api import billing_api
from soracom_api.model.get_billing_history_response import GetBillingHistoryResponse

if __name__ == "__main__":
    config = helpers.get_auth_config()
    with soracom_api.ApiClient(config) as api_client:
        api_instance = billing_api.BillingApi(api_client)
        api_response: GetBillingHistoryResponse = api_instance.get_billing_history()
        pprint(api_response)
