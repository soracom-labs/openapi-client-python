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
from soracom_api.model.set_system_notifications_request import SetSystemNotificationsRequest
from soracom_api.model.system_notifications_model import SystemNotificationsModel


class SystemNotificationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_system_notification_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'api_key',
                    'api_token'
                ],
                'endpoint_path': '/operators/{operator_id}/system_notifications/{type}',
                'operation_id': 'delete_system_notification',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'operator_id',
                    'type',
                ],
                'required': [
                    'operator_id',
                    'type',
                ],
                'nullable': [
                ],
                'enum': [
                    'type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('type',): {

                        "RECOVERY": "recovery",
                        "BILLING": "billing",
                        "SUPPORT": "support"
                    },
                },
                'openapi_types': {
                    'operator_id':
                        (str,),
                    'type':
                        (str,),
                },
                'attribute_map': {
                    'operator_id': 'operator_id',
                    'type': 'type',
                },
                'location_map': {
                    'operator_id': 'path',
                    'type': 'path',
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
        self.get_system_notification_endpoint = _Endpoint(
            settings={
                'response_type': (SystemNotificationsModel,),
                'auth': [
                    'api_key',
                    'api_token'
                ],
                'endpoint_path': '/operators/{operator_id}/system_notifications/{type}',
                'operation_id': 'get_system_notification',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'operator_id',
                    'type',
                ],
                'required': [
                    'operator_id',
                    'type',
                ],
                'nullable': [
                ],
                'enum': [
                    'type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('type',): {

                        "PRIMARY": "primary",
                        "RECOVERY": "recovery",
                        "BILLING": "billing",
                        "SUPPORT": "support"
                    },
                },
                'openapi_types': {
                    'operator_id':
                        (str,),
                    'type':
                        (str,),
                },
                'attribute_map': {
                    'operator_id': 'operator_id',
                    'type': 'type',
                },
                'location_map': {
                    'operator_id': 'path',
                    'type': 'path',
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
        self.list_system_notifications_endpoint = _Endpoint(
            settings={
                'response_type': ([SystemNotificationsModel],),
                'auth': [
                    'api_key',
                    'api_token'
                ],
                'endpoint_path': '/operators/{operator_id}/system_notifications',
                'operation_id': 'list_system_notifications',
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
        self.set_system_notification_endpoint = _Endpoint(
            settings={
                'response_type': (SystemNotificationsModel,),
                'auth': [
                    'api_key',
                    'api_token'
                ],
                'endpoint_path': '/operators/{operator_id}/system_notifications/{type}',
                'operation_id': 'set_system_notification',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'operator_id',
                    'type',
                    'set_system_notifications_request',
                ],
                'required': [
                    'operator_id',
                    'type',
                    'set_system_notifications_request',
                ],
                'nullable': [
                ],
                'enum': [
                    'type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('type',): {

                        "PRIMARY": "primary",
                        "RECOVERY": "recovery",
                        "BILLING": "billing",
                        "SUPPORT": "support"
                    },
                },
                'openapi_types': {
                    'operator_id':
                        (str,),
                    'type':
                        (str,),
                    'set_system_notifications_request':
                        (SetSystemNotificationsRequest,),
                },
                'attribute_map': {
                    'operator_id': 'operator_id',
                    'type': 'type',
                },
                'location_map': {
                    'operator_id': 'path',
                    'type': 'path',
                    'set_system_notifications_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json;charset=UTF-8'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def delete_system_notification(
        self,
        operator_id,
        type,
        **kwargs
    ):
        """Delete system notification  # noqa: E501

        Deletes a system notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_system_notification(operator_id, type, async_req=True)
        >>> result = thread.get()

        Args:
            operator_id (str): operator_id
            type (str): system notification type

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
        kwargs['type'] = \
            type
        return self.delete_system_notification_endpoint.call_with_http_info(**kwargs)

    def get_system_notification(
        self,
        operator_id,
        type,
        **kwargs
    ):
        """Get system notification  # noqa: E501

        Returns a system notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_system_notification(operator_id, type, async_req=True)
        >>> result = thread.get()

        Args:
            operator_id (str): operator_id
            type (str): system notification type

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
            SystemNotificationsModel
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
        kwargs['type'] = \
            type
        return self.get_system_notification_endpoint.call_with_http_info(**kwargs)

    def list_system_notifications(
        self,
        operator_id,
        **kwargs
    ):
        """List system notifications  # noqa: E501

        Returns a list of system notifications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_system_notifications(operator_id, async_req=True)
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
            [SystemNotificationsModel]
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
        return self.list_system_notifications_endpoint.call_with_http_info(**kwargs)

    def set_system_notification(
        self,
        operator_id,
        type,
        set_system_notifications_request,
        **kwargs
    ):
        """Set system notification  # noqa: E501

        Sets a system notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_system_notification(operator_id, type, set_system_notifications_request, async_req=True)
        >>> result = thread.get()

        Args:
            operator_id (str): operator_id
            type (str): system notification type
            set_system_notifications_request (SetSystemNotificationsRequest): request

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
            SystemNotificationsModel
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
        kwargs['type'] = \
            type
        kwargs['set_system_notifications_request'] = \
            set_system_notifications_request
        return self.set_system_notification_endpoint.call_with_http_info(**kwargs)

