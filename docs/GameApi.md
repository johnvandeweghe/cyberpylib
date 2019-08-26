# cyber_py_lib.GameApi

All URIs are relative to *http://No Production URL yet*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_unit**](GameApi.md#get_unit) | **GET** /unit/{unitId} | Get a specific unit
[**get_units**](GameApi.md#get_units) | **GET** /units/{gameId} | Get units for a game.


# **get_unit**
> Unit get_unit(unit_id)

Get a specific unit

### Example

```python
from __future__ import print_function
import time
import cyber_py_lib
from cyber_py_lib.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = cyber_py_lib.GameApi()
unit_id = 'unit_id_example' # str | Which unit to retrieve

try:
    # Get a specific unit
    api_response = api_instance.get_unit(unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->get_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | [**str**](.md)| Which unit to retrieve | 

### Return type

[**Unit**](Unit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about a specific unit |  -  |
**404** | The unit could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_units**
> list[Unit] get_units(game_id)

Get units for a game.

### Example

```python
from __future__ import print_function
import time
import cyber_py_lib
from cyber_py_lib.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = cyber_py_lib.GameApi()
game_id = 'game_id_example' # str | Which game's units to retrieve

try:
    # Get units for a game.
    api_response = api_instance.get_units(game_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->get_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | [**str**](.md)| Which game&#39;s units to retrieve | 

### Return type

[**list[Unit]**](Unit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about units in the current game |  -  |
**404** | The game could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

