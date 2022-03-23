import os

import soracom_api

from .auth import Coverage, auth


def test_auth():
    assert isinstance(
        auth(
            auth_key=os.environ["SORACOM_AUTH_KEY"],
            auth_key_id=os.environ["SORACOM_AUTH_KEY_ID"],
            coverage=Coverage.JAPAN,
        ),
        soracom_api.Configuration,
    )
