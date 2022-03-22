import os

import soracom_api
from helpers import Coverage, auth, get_auth_config


def test_auth():
    assert isinstance(
        auth(
            auth_key=os.environ["SORACOM_AUTH_KEY"],
            auth_key_id=os.environ["SORACOM_AUTH_KEY_ID"],
            coverage=Coverage.JAPAN,
        ),
        soracom_api.Configuration,
    )


def test_get_auth_config():
    assert isinstance(get_auth_config(), soracom_api.Configuration)
