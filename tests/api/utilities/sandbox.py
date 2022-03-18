import uuid
from dataclasses import dataclass

import sandbox
from sandbox.api import operator_api
from sandbox.model.sandbox_auth_response import SandboxAuthResponse
from sandbox.model.sandbox_init_request import SandboxInitRequest


@dataclass
class SandboxConfig:
    auth: SandboxAuthResponse
    url: str


def get_sandbox_config(auth_key: str, auth_key_id: str) -> SandboxConfig:
    with sandbox.ApiClient() as api_client:
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
        assert isinstance(api_response.get("api_key"), str)
        assert isinstance(api_response.get("token"), str)
        assert isinstance(api_response.get("operator_id"), str)
        return SandboxConfig(auth=api_response, url=sandbox.Configuration().get_host_settings()[0]["url"])
