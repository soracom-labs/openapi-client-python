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
from soracom_api.model.api_audit_log_entry import APIAuditLogEntry
from soracom_api.model.napter_audit_log_entry import NapterAuditLogEntry


class AuditLogApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_api_audit_logs_endpoint = _Endpoint(
            settings={
                'response_type': ([APIAuditLogEntry],),
                'auth': [
                    'api_key',
                    'api_token'
                ],
                'endpoint_path': '/audit_logs/api',
                'operation_id': 'get_api_audit_logs',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'api_kind',
                    'from_epoch_ms',
                    'to_epoch_ms',
                    'limit',
                    'last_evaluated_key',
                ],
                'required': [],
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
                    'api_kind':
                        (str,),
                    'from_epoch_ms':
                        (int,),
                    'to_epoch_ms':
                        (int,),
                    'limit':
                        (int,),
                    'last_evaluated_key':
                        (str,),
                },
                'attribute_map': {
                    'api_kind': 'api_kind',
                    'from_epoch_ms': 'from_epoch_ms',
                    'to_epoch_ms': 'to_epoch_ms',
                    'limit': 'limit',
                    'last_evaluated_key': 'last_evaluated_key',
                },
                'location_map': {
                    'api_kind': 'query',
                    'from_epoch_ms': 'query',
                    'to_epoch_ms': 'query',
                    'limit': 'query',
                    'last_evaluated_key': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_napter_audit_logs_endpoint = _Endpoint(
            settings={
                'response_type': ([NapterAuditLogEntry],),
                'auth': [
                    'api_key',
                    'api_token'
                ],
                'endpoint_path': '/audit_logs/napter',
                'operation_id': 'get_napter_audit_logs',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'resource_type',
                    'resource_id',
                    '_from',
                    'to',
                    'limit',
                    'last_evaluated_key',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'resource_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('resource_type',): {

                        "SUBSCRIBER": "Subscriber"
                    },
                },
                'openapi_types': {
                    'resource_type':
                        (str,),
                    'resource_id':
                        (str,),
                    '_from':
                        (int,),
                    'to':
                        (int,),
                    'limit':
                        (int,),
                    'last_evaluated_key':
                        (str,),
                },
                'attribute_map': {
                    'resource_type': 'resource_type',
                    'resource_id': 'resource_id',
                    '_from': 'from',
                    'to': 'to',
                    'limit': 'limit',
                    'last_evaluated_key': 'last_evaluated_key',
                },
                'location_map': {
                    'resource_type': 'query',
                    'resource_id': 'query',
                    '_from': 'query',
                    'to': 'query',
                    'limit': 'query',
                    'last_evaluated_key': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_api_audit_logs(
        self,
        **kwargs
    ):
        """Retrieve audit logs for API calls  # noqa: E501

        Retrieve audit logs for API calls.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_api_audit_logs(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            api_kind (str): Filter item for audit log retrieval by API kind (e.g. `/v1/auth`).. [optional]
            from_epoch_ms (int): Start time for the log search range (unixtime milliseconds).. [optional]
            to_epoch_ms (int): End time for the log search range (unixtime milliseconds).. [optional]
            limit (int): Maximum number of log entries to retrieve.. [optional]
            last_evaluated_key (str): The value of `requestedTimeEpochMs` in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward.. [optional]
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
            [APIAuditLogEntry]
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
        return self.get_api_audit_logs_endpoint.call_with_http_info(**kwargs)

    def get_napter_audit_logs(
        self,
        **kwargs
    ):
        """Retrieve audit logs for Napter  # noqa: E501

        Retrieve audit logs for Napter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_napter_audit_logs(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            resource_type (str): Type of the target resource to query Napter audit log entries.. [optional] if omitted the server will use the default value of "Subscriber"
            resource_id (str): Identity of the target resource to query log entries.. [optional]
            _from (int): Start time for the log search range (unixtime milliseconds).. [optional]
            to (int): End time for the log search range (unixtime milliseconds).. [optional]
            limit (int): Maximum number of log entries to retrieve.. [optional]
            last_evaluated_key (str): The value of `time` in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward.. [optional]
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
            [NapterAuditLogEntry]
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
        return self.get_napter_audit_logs_endpoint.call_with_http_info(**kwargs)

