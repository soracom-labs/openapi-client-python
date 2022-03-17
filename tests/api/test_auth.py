import os

import api_utilities
import sandbox_utilities


def test_sandbox_auth():
    auth_key = os.environ.get("SORACOM_AUTH_KEY")
    auth_key_id = os.environ.get("SORACOM_AUTH_KEY_ID")
    sandbox_utilities.get_sandbox_config(auth_key, auth_key_id)


def test_auth():
    auth_key = os.environ.get("SORACOM_AUTH_KEY")
    auth_key_id = os.environ.get("SORACOM_AUTH_KEY_ID")
    api_utilities.get_api_config(auth_key, auth_key_id)
