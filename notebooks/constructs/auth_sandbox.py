import uuid

import soracom_sandbox
from soracom_sandbox.api import operator_api
from soracom_sandbox.model.sandbox_auth_response import SandboxAuthResponse
from soracom_sandbox.model.sandbox_init_request import SandboxInitRequest

from .types import Coverage


def auth_sandbox(auth_key: str, auth_key_id: str) -> soracom_sandbox.Configuration:
    with soracom_sandbox.ApiClient() as api_client:
        api_instance = operator_api.OperatorApi(api_client)
        random_str = uuid.uuid4()
        sandbox_init_request = SandboxInitRequest(
            auth_key=auth_key,
            auth_key_id=auth_key_id,
            coverage_types=[
                "g",
                "jp",
            ],
            email=f"openapi-client-python+{random_str}@soracom.io",
            password=f"Password{random_str}",
            register_payment_method=True,
        )

        api_response: SandboxAuthResponse = api_instance.sandbox_initialize_operator(sandbox_init_request)
        return soracom_sandbox.Configuration(
            host=Coverage.SANDBOX.value,
            api_key={
                "api_key": api_response.get("api_key"),
                "api_token": api_response.get("token"),
            },
        )
