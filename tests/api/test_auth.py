import os
import typing

import api
import pytest
import utilities
from api.api import sim_api
from api.model.sim import Sim


def test_sandbox():
    auth_key = os.environ["SORACOM_AUTH_KEY"]
    auth_key_id = os.environ["SORACOM_AUTH_KEY_ID"]
    config = utilities.get_api_config_on_sandbox(auth_key, auth_key_id)
    _test_body(config)


@pytest.mark.skip(reason="Comment out this line to test, since production APIs shouldn't be called on CI")
def test_production():
    auth_key = os.environ["SORACOM_AUTH_KEY"]
    auth_key_id = os.environ["SORACOM_AUTH_KEY_ID"]
    config = utilities.get_api_config_on_production(auth_key, auth_key_id, utilities.Coverage.JAPAN)
    _test_body(config)


def _test_body(config: api.Configuration):
    with api.ApiClient(config) as api_client:
        api_instance = sim_api.SimApi(api_client)
        limit = 2
        api_response: typing.List[Sim] = api_instance.list_sims(
            limit=limit,
        )
        for idx, sim in enumerate(api_response):
            print(f"{idx}: {sim.__class__}")
        assert len(api_response) <= limit
