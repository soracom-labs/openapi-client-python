"""
    SORACOM API

    SORACOM API v1  # noqa: E501

    The version of the OpenAPI document: VERSION_PLACEHOLDER
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from soracom_api.api_client import ApiClient, Endpoint as _Endpoint
from soracom_api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from soracom_api.model.emails_model import EmailsModel
from soracom_api.model.issue_add_email_token_request import IssueAddEmailTokenRequest
from soracom_api.model.verify_add_email_token_request import VerifyAddEmailTokenRequest


class EmailApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_email_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'api_key',
                    'api_token'
                ],
                'endpoint_path': '/operators/{operator_id}/emails/{email_id}',
                'operation_id': 'delete_email',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'operator_id',
                    'email_id',
                ],
                'required': [
                    'operator_id',
                    'email_id',
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
                    'operator_id':
                        (str,),
                    'email_id':
                        (str,),
                },
                'attribute_map': {
                    'operator_id': 'operator_id',
                    'email_id': 'email_id',
                },
                'location_map': {
                    'operator_id': 'path',
                    'email_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_email_endpoint = _Endpoint(
            settings={
                'response_type': (EmailsModel,),
                'auth': [
                    'api_key',
                    'api_token'
                ],
                'endpoint_path': '/operators/{operator_id}/emails/{email_id}',
                'operation_id': 'get_email',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'operator_id',
                    'email_id',
                ],
                'required': [
                    'operator_id',
                    'email_id',
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
                    'operator_id':
                        (str,),
                    'email_id':
                        (str,),
                },
                'attribute_map': {
                    'operator_id': 'operator_id',
                    'email_id': 'email_id',
                },
                'location_map': {
                    'operator_id': 'path',
                    'email_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json;charset=UTF-8'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.issue_add_email_token_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'api_key',
                    'api_token'
                ],
                'endpoint_path': '/operators/add_email_token/issue',
                'operation_id': 'issue_add_email_token',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'issue_add_email_token_request',
                ],
                'required': [
                    'issue_add_email_token_request',
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
                    'issue_add_email_token_request':
                        (IssueAddEmailTokenRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'issue_add_email_token_request': 'body',
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
        self.list_emails_endpoint = _Endpoint(
            settings={
                'response_type': ([EmailsModel],),
                'auth': [
                    'api_key',
                    'api_token'
                ],
                'endpoint_path': '/operators/{operator_id}/emails',
                'operation_id': 'list_emails',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'operator_id',
                ],
                'required': [
                    'operator_id',
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
                    'operator_id':
                        (str,),
                },
                'attribute_map': {
                    'operator_id': 'operator_id',
                },
                'location_map': {
                    'operator_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json;charset=UTF-8'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.verify_add_email_token_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/operators/add_email_token/verify',
                'operation_id': 'verify_add_email_token',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'verify_add_email_token_request',
                ],
                'required': [
                    'verify_add_email_token_request',
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
                    'verify_add_email_token_request':
                        (VerifyAddEmailTokenRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'verify_add_email_token_request': 'body',
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

    def delete_email(
        self,
        operator_id,
        email_id,
        **kwargs
    ):
        """Delete email address  # noqa: E501

        Deletes an email address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_email(operator_id, email_id, async_req=True)
        >>> result = thread.get()

        Args:
            operator_id (str): operator_id
            email_id (str): email_id

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
        kwargs['operator_id'] = \
            operator_id
        kwargs['email_id'] = \
            email_id
        return self.delete_email_endpoint.call_with_http_info(**kwargs)

    def get_email(
        self,
        operator_id,
        email_id,
        **kwargs
    ):
        """Get email address  # noqa: E501

        Returns an email address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_email(operator_id, email_id, async_req=True)
        >>> result = thread.get()

        Args:
            operator_id (str): operator_id
            email_id (str): email_id

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
            EmailsModel
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
        kwargs['operator_id'] = \
            operator_id
        kwargs['email_id'] = \
            email_id
        return self.get_email_endpoint.call_with_http_info(**kwargs)

    def issue_add_email_token(
        self,
        issue_add_email_token_request,
        **kwargs
    ):
        """Issue a token to add an email address  # noqa: E501

        Sends an email with a one-time token for adding an e-mail address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.issue_add_email_token(issue_add_email_token_request, async_req=True)
        >>> result = thread.get()

        Args:
            issue_add_email_token_request (IssueAddEmailTokenRequest): request

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
        kwargs['issue_add_email_token_request'] = \
            issue_add_email_token_request
        return self.issue_add_email_token_endpoint.call_with_http_info(**kwargs)

    def list_emails(
        self,
        operator_id,
        **kwargs
    ):
        """List email addresses  # noqa: E501

        Returns a list of email addresses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_emails(operator_id, async_req=True)
        >>> result = thread.get()

        Args:
            operator_id (str): operator_id

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
            [EmailsModel]
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
        kwargs['operator_id'] = \
            operator_id
        return self.list_emails_endpoint.call_with_http_info(**kwargs)

    def verify_add_email_token(
        self,
        verify_add_email_token_request,
        **kwargs
    ):
        """Verify a token to add an email address  # noqa: E501

        Verifies the token for adding email address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.verify_add_email_token(verify_add_email_token_request, async_req=True)
        >>> result = thread.get()

        Args:
            verify_add_email_token_request (VerifyAddEmailTokenRequest): request

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
        kwargs['verify_add_email_token_request'] = \
            verify_add_email_token_request
        return self.verify_add_email_token_endpoint.call_with_http_info(**kwargs)
