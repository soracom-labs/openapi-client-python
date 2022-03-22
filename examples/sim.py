from pprint import pprint

import helpers
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.sim import Sim

if __name__ == "__main__":
    config = helpers.get_auth_config()
    with soracom_api.ApiClient(config) as api_client:
        api_instance = sim_api.SimApi(api_client)
        api_response: list[Sim] = api_instance.list_sims(limit=3)
        pprint(api_response)
