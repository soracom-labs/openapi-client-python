"""
    SORACOM API

    SORACOM API v1  # noqa: E501

    The version of the OpenAPI document: VERSION_PLACEHOLDER
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from api.exceptions import ApiAttributeError


def lazy_import():
    from api.model.imei_lock import ImeiLock
    from api.model.previous_session_status import PreviousSessionStatus
    from api.model.session_status import SessionStatus
    from api.model.tag_set import TagSet
    globals()['ImeiLock'] = ImeiLock
    globals()['PreviousSessionStatus'] = PreviousSessionStatus
    globals()['SessionStatus'] = SessionStatus
    globals()['TagSet'] = TagSet


class Subscriber(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('expiry_action',): {
            'DONOTHING': "doNothing",
            'DELETESESSION': "deleteSession",
            'DEACTIVATE': "deactivate",
            'SUSPEND': "suspend",
            'TERMINATE': "terminate",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'apn': (str,),  # noqa: E501
            'bundles': ([str],),  # noqa: E501
            'created_at': (int,),  # noqa: E501
            'expired_at': (int,),  # noqa: E501
            'expired_time': (int,),  # noqa: E501
            'expiry_action': (str,),  # noqa: E501
            'group_id': (str,),  # noqa: E501
            'iccid': (str,),  # noqa: E501
            'imei_lock': (ImeiLock,),  # noqa: E501
            'imsi': (str,),  # noqa: E501
            'ip_address': (str,),  # noqa: E501
            'last_modified_at': (int,),  # noqa: E501
            'last_port_mapping_created_time': (int,),  # noqa: E501
            'module_type': (str,),  # noqa: E501
            'msisdn': (str,),  # noqa: E501
            'operator_id': (str,),  # noqa: E501
            'plan': (int,),  # noqa: E501
            'previous_session': (PreviousSessionStatus,),  # noqa: E501
            'registered_time': (int,),  # noqa: E501
            'serial_number': (str,),  # noqa: E501
            'session_status': (SessionStatus,),  # noqa: E501
            'sim_id': (str,),  # noqa: E501
            'speed_class': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'subscription': (str,),  # noqa: E501
            'tags': (TagSet,),  # noqa: E501
            'termination_enabled': (bool,),  # noqa: E501
            'type': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'apn': 'apn',  # noqa: E501
        'bundles': 'bundles',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'expired_at': 'expiredAt',  # noqa: E501
        'expired_time': 'expiredTime',  # noqa: E501
        'expiry_action': 'expiryAction',  # noqa: E501
        'group_id': 'groupId',  # noqa: E501
        'iccid': 'iccid',  # noqa: E501
        'imei_lock': 'imeiLock',  # noqa: E501
        'imsi': 'imsi',  # noqa: E501
        'ip_address': 'ipAddress',  # noqa: E501
        'last_modified_at': 'lastModifiedAt',  # noqa: E501
        'last_port_mapping_created_time': 'lastPortMappingCreatedTime',  # noqa: E501
        'module_type': 'moduleType',  # noqa: E501
        'msisdn': 'msisdn',  # noqa: E501
        'operator_id': 'operatorId',  # noqa: E501
        'plan': 'plan',  # noqa: E501
        'previous_session': 'previousSession',  # noqa: E501
        'registered_time': 'registeredTime',  # noqa: E501
        'serial_number': 'serialNumber',  # noqa: E501
        'session_status': 'sessionStatus',  # noqa: E501
        'sim_id': 'simId',  # noqa: E501
        'speed_class': 'speedClass',  # noqa: E501
        'status': 'status',  # noqa: E501
        'subscription': 'subscription',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'termination_enabled': 'terminationEnabled',  # noqa: E501
        'type': 'type',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Subscriber - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            apn (str): The Access Point Name configured.. [optional]  # noqa: E501
            bundles ([str]): [optional]  # noqa: E501
            created_at (int): The timestamp that the SIM was created.. [optional]  # noqa: E501
            expired_at (int): The timestamp of a date and time where the SIM was expired.. [optional]  # noqa: E501
            expired_time (int): The timestamp of a date and time where the SIM was expired.. [optional]  # noqa: E501
            expiry_action (str): [optional]  # noqa: E501
            group_id (str): The SIM group ID where the SIM belongs to.. [optional]  # noqa: E501
            iccid (str): The ICCID of the SIM.. [optional]  # noqa: E501
            imei_lock (ImeiLock): [optional]  # noqa: E501
            imsi (str): The IMSI of the SIM.. [optional]  # noqa: E501
            ip_address (str): [optional]  # noqa: E501
            last_modified_at (int): The timestamp when the SIM information was modified.. [optional]  # noqa: E501
            last_port_mapping_created_time (int): The timestamp (in Unix milliseconds) of the last instance where the Napter On-Demand Remote Access service was used with the subscriber. If Napter has never been used with the subscriber, null is returned.. [optional]  # noqa: E501
            module_type (str): The form factor of the physical SIM. Possible values are \"mini\" for 2FF SIM card, \"micro\" for 3FF SIM card, \"nano\" for 4FF SIM card, \"trio\" for a Universal 3-in-1 (2FF/3FF/4FF) SIM card, or \"embedded\" for MFF2 or Embedded SIM (eSIM).. [optional]  # noqa: E501
            msisdn (str): The MSISDN of the SIM.. [optional]  # noqa: E501
            operator_id (str): The Operator ID of the SIM.. [optional]  # noqa: E501
            plan (int): Whether or not the subscription supports SMS functionality. 0 = SMS not supported; 1 = SMS supported.. [optional]  # noqa: E501
            previous_session (PreviousSessionStatus): [optional]  # noqa: E501
            registered_time (int): The timestamp (in Unix milliseconds) that the subscriber was manually registered to your account. When purchasing SIMs directly through the User Console, SIMs will automatically be registered to your account, and null is returned.. [optional]  # noqa: E501
            serial_number (str): The serial number of the SIM.. [optional]  # noqa: E501
            session_status (SessionStatus): [optional]  # noqa: E501
            sim_id (str): The SIM ID of the SIM.. [optional]  # noqa: E501
            speed_class (str): The speed class of the SIM.. [optional]  # noqa: E501
            status (str): The subscription status of the subscriber. Possible values are \"ready\", \"active\", \"inactive\", \"standby\", \"suspended\", or \"terminated\".. [optional]  # noqa: E501
            subscription (str): The name of the subscription for the SIM.. [optional]  # noqa: E501
            tags (TagSet): [optional]  # noqa: E501
            termination_enabled (bool): [optional]  # noqa: E501
            type (str): The speed class of the SIM.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Subscriber - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            apn (str): The Access Point Name configured.. [optional]  # noqa: E501
            bundles ([str]): [optional]  # noqa: E501
            created_at (int): The timestamp that the SIM was created.. [optional]  # noqa: E501
            expired_at (int): The timestamp of a date and time where the SIM was expired.. [optional]  # noqa: E501
            expired_time (int): The timestamp of a date and time where the SIM was expired.. [optional]  # noqa: E501
            expiry_action (str): [optional]  # noqa: E501
            group_id (str): The SIM group ID where the SIM belongs to.. [optional]  # noqa: E501
            iccid (str): The ICCID of the SIM.. [optional]  # noqa: E501
            imei_lock (ImeiLock): [optional]  # noqa: E501
            imsi (str): The IMSI of the SIM.. [optional]  # noqa: E501
            ip_address (str): [optional]  # noqa: E501
            last_modified_at (int): The timestamp when the SIM information was modified.. [optional]  # noqa: E501
            last_port_mapping_created_time (int): The timestamp (in Unix milliseconds) of the last instance where the Napter On-Demand Remote Access service was used with the subscriber. If Napter has never been used with the subscriber, null is returned.. [optional]  # noqa: E501
            module_type (str): The form factor of the physical SIM. Possible values are \"mini\" for 2FF SIM card, \"micro\" for 3FF SIM card, \"nano\" for 4FF SIM card, \"trio\" for a Universal 3-in-1 (2FF/3FF/4FF) SIM card, or \"embedded\" for MFF2 or Embedded SIM (eSIM).. [optional]  # noqa: E501
            msisdn (str): The MSISDN of the SIM.. [optional]  # noqa: E501
            operator_id (str): The Operator ID of the SIM.. [optional]  # noqa: E501
            plan (int): Whether or not the subscription supports SMS functionality. 0 = SMS not supported; 1 = SMS supported.. [optional]  # noqa: E501
            previous_session (PreviousSessionStatus): [optional]  # noqa: E501
            registered_time (int): The timestamp (in Unix milliseconds) that the subscriber was manually registered to your account. When purchasing SIMs directly through the User Console, SIMs will automatically be registered to your account, and null is returned.. [optional]  # noqa: E501
            serial_number (str): The serial number of the SIM.. [optional]  # noqa: E501
            session_status (SessionStatus): [optional]  # noqa: E501
            sim_id (str): The SIM ID of the SIM.. [optional]  # noqa: E501
            speed_class (str): The speed class of the SIM.. [optional]  # noqa: E501
            status (str): The subscription status of the subscriber. Possible values are \"ready\", \"active\", \"inactive\", \"standby\", \"suspended\", or \"terminated\".. [optional]  # noqa: E501
            subscription (str): The name of the subscription for the SIM.. [optional]  # noqa: E501
            tags (TagSet): [optional]  # noqa: E501
            termination_enabled (bool): [optional]  # noqa: E501
            type (str): The speed class of the SIM.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
