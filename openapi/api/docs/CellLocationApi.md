# soracom_api.CellLocationApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_get_cell_locations**](CellLocationApi.md#batch_get_cell_locations) | **POST** /cell_locations | List location information for multiple cell towers.
[**get_cell_location**](CellLocationApi.md#get_cell_location) | **GET** /cell_locations | Get location information for a cell tower.


# **batch_get_cell_locations**
> [CellLocation] batch_get_cell_locations(cell_identifier)

List location information for multiple cell towers.

Retrieves a list of location information (latitude / longitude) for multiple cell towers which are identified by Cell IDs etc.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import cell_location_api
from soracom_api.model.cell_identifier import CellIdentifier
from soracom_api.model.cell_location import CellLocation
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = soracom_api.Configuration(
    host = "https://api.soracom.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: api_token
configuration.api_key['api_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with soracom_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cell_location_api.CellLocationApi(api_client)
    cell_identifier = [
        CellIdentifier(
            cid="cid_example",
            eci="eci_example",
            ecid="ecid_example",
            identifier="identifier_example",
            lac="lac_example",
            mcc="mcc_example",
            mnc="mnc_example",
            tac="tac_example",
        ),
    ] # [CellIdentifier] | List of cell identifiers.

    # example passing only required values which don't have defaults set
    try:
        # List location information for multiple cell towers.
        api_response = api_instance.batch_get_cell_locations(cell_identifier)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling CellLocationApi->batch_get_cell_locations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cell_identifier** | [**[CellIdentifier]**](CellIdentifier.md)| List of cell identifiers. |

### Return type

[**[CellLocation]**](CellLocation.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of location information for the specified cell towers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cell_location**
> CellLocation get_cell_location(mcc, mnc)

Get location information for a cell tower.

Retrieves location information (latitude / longitude) for a cell tower which is identified by Cell ID etc. Please specify MCC, MNC, LAC and CID when the access radio technology is 3G. It is possible to retrieve location information without CID, but the location information will be low accuracy.  For LTE (4G), please specify MCC, MNC, TAC and ECID. As it is based on an open database to convert cell information into location information, the location information does not exist or might be incorrect.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import cell_location_api
from soracom_api.model.cell_location import CellLocation
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = soracom_api.Configuration(
    host = "https://api.soracom.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: api_token
configuration.api_key['api_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with soracom_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cell_location_api.CellLocationApi(api_client)
    mcc = "mcc_example" # str | MCC - Mobile Country Code
    mnc = "mnc_example" # str | MNC - Mobile Network Code
    lac = "lac_example" # str | LAC - Location Area Code (for 3G) (optional)
    cid = "cid_example" # str | CID - Cell ID (for 3G) (optional)
    tac = "tac_example" # str | TAC - Tracking Area Code (for 4G) (optional)
    ecid = "ecid_example" # str | ECID - Enhanced Cell ID (for 4G) - specify either `ecid` or `eci` (optional)
    eci = "eci_example" # str | ECID - Enhanced Cell ID (for 4G) - specify either `ecid` or `eci` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get location information for a cell tower.
        api_response = api_instance.get_cell_location(mcc, mnc)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling CellLocationApi->get_cell_location: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get location information for a cell tower.
        api_response = api_instance.get_cell_location(mcc, mnc, lac=lac, cid=cid, tac=tac, ecid=ecid, eci=eci)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling CellLocationApi->get_cell_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mcc** | **str**| MCC - Mobile Country Code |
 **mnc** | **str**| MNC - Mobile Network Code |
 **lac** | **str**| LAC - Location Area Code (for 3G) | [optional]
 **cid** | **str**| CID - Cell ID (for 3G) | [optional]
 **tac** | **str**| TAC - Tracking Area Code (for 4G) | [optional]
 **ecid** | **str**| ECID - Enhanced Cell ID (for 4G) - specify either &#x60;ecid&#x60; or &#x60;eci&#x60; | [optional]
 **eci** | **str**| ECID - Enhanced Cell ID (for 4G) - specify either &#x60;ecid&#x60; or &#x60;eci&#x60; | [optional]

### Return type

[**CellLocation**](CellLocation.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Location information for the cell tower |  -  |
**404** | Location information is not found for the cell tower |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

