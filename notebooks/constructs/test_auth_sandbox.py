import os

import soracom_sandbox

from .auth_sandbox import auth_sandbox


def test_auth():
    assert isinstance(
        auth_sandbox(
            auth_key=os.environ["SORACOM_AUTH_KEY"],
            auth_key_id=os.environ["SORACOM_AUTH_KEY_ID"],
        ),
        soracom_sandbox.Configuration,
    )
