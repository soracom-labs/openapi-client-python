"""
    SORACOM API

    SORACOM API v1  # noqa: E501

    The version of the OpenAPI document: VERSION_PLACEHOLDER
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from api.api_client import ApiClient, Endpoint as _Endpoint
from api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from api.model.auth_request import AuthRequest
from api.model.auth_response import AuthResponse
from api.model.issue_password_reset_token_request import IssuePasswordResetTokenRequest
from api.model.verify_password_reset_token_request import VerifyPasswordResetTokenRequest


class AuthApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.auth_endpoint = _Endpoint(
            settings={
                'response_type': (AuthResponse,),
                'auth': [],
                'endpoint_path': '/auth',
                'operation_id': 'auth',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'auth_request',
                ],
                'required': [
                    'auth_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'auth_request':
                        (AuthRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'auth_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.issue_password_reset_token_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/auth/password_reset_token/issue',
                'operation_id': 'issue_password_reset_token',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'issue_password_reset_token_request',
                ],
                'required': [
                    'issue_password_reset_token_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'issue_password_reset_token_request':
                        (IssuePasswordResetTokenRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'issue_password_reset_token_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.verify_password_reset_token_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/auth/password_reset_token/verify',
                'operation_id': 'verify_password_reset_token',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'verify_password_reset_token_request',
                ],
                'required': [
                    'verify_password_reset_token_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'verify_password_reset_token_request':
                        (VerifyPasswordResetTokenRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'verify_password_reset_token_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def auth(
        self,
        auth_request,
        **kwargs
    ):
        """Performs authentication to access to the SORACOM API.  # noqa: E501

        Performs authentication to access to the SORACOM API. To perform authentication by a root account, specify `email` and `password`. To perform authentication by an AuthKey, specify `authKeyId` and `authKey`. To perform authentication by a SAM user, specify `operatorId`, `userName` and `password`. An API Key and an API Token will be included in the response if successful. Specify the API Key and the API Token to requests afterwards  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auth(auth_request, async_req=True)
        >>> result = thread.get()

        Args:
            auth_request (AuthRequest): Authentication request.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AuthResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['auth_request'] = \
            auth_request
        return self.auth_endpoint.call_with_http_info(**kwargs)

    def issue_password_reset_token(
        self,
        issue_password_reset_token_request,
        **kwargs
    ):
        """Issues a password reset token for the operator.  # noqa: E501

        Generates a password reset token and send it to the operator's mail address. After receiving the password reset token, call /v1/auth/password_reset_token/verify API with the token to update operator's password.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.issue_password_reset_token(issue_password_reset_token_request, async_req=True)
        >>> result = thread.get()

        Args:
            issue_password_reset_token_request (IssuePasswordResetTokenRequest): email address

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['issue_password_reset_token_request'] = \
            issue_password_reset_token_request
        return self.issue_password_reset_token_endpoint.call_with_http_info(**kwargs)

    def verify_password_reset_token(
        self,
        verify_password_reset_token_request,
        **kwargs
    ):
        """Verifies the password reset token and updates password.  # noqa: E501

        Updates the operator's password if the password reset token is verified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.verify_password_reset_token(verify_password_reset_token_request, async_req=True)
        >>> result = thread.get()

        Args:
            verify_password_reset_token_request (VerifyPasswordResetTokenRequest): token, password

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['verify_password_reset_token_request'] = \
            verify_password_reset_token_request
        return self.verify_password_reset_token_endpoint.call_with_http_info(**kwargs)
