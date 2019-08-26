# cyber_py_lib.TurnApi

All URIs are relative to *http://No Production URL yet*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_unit_action**](TurnApi.md#create_unit_action) | **POST** /unitAction | Take an action as a unit on a turn.
[**start_turn**](TurnApi.md#start_turn) | **POST** /turns | Start a turn
[**update_turn**](TurnApi.md#update_turn) | **PATCH** /turns/{turnId} | Update a turn (used to end a turn)


# **create_unit_action**
> UnitAction create_unit_action(unit_action_params=unit_action_params)

Take an action as a unit on a turn.

### Example

```python
from __future__ import print_function
import time
import cyber_py_lib
from cyber_py_lib.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = cyber_py_lib.TurnApi()
unit_action_params = cyber_py_lib.UnitActionParams() # UnitActionParams |  (optional)

try:
    # Take an action as a unit on a turn.
    api_response = api_instance.create_unit_action(unit_action_params=unit_action_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TurnApi->create_unit_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_action_params** | [**UnitActionParams**](UnitActionParams.md)|  | [optional] 

### Return type

[**UnitAction**](UnitAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about units in the current game |  -  |
**400** | Invalid action type, or missing/invalid body field. |  -  |
**403** | It is not your turn, or the unit is out of action points |  -  |
**404** | The turn or unit could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_turn**
> Turn start_turn(inline_object2=inline_object2)

Start a turn

### Example

```python
from __future__ import print_function
import time
import cyber_py_lib
from cyber_py_lib.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = cyber_py_lib.TurnApi()
inline_object2 = cyber_py_lib.InlineObject2() # InlineObject2 |  (optional)

try:
    # Start a turn
    api_response = api_instance.start_turn(inline_object2=inline_object2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TurnApi->start_turn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | [optional] 

### Return type

[**Turn**](Turn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The turn that was created. |  -  |
**400** | Unable to end turn until all units have been placed. |  -  |
**403** | Not your turn. |  -  |
**404** | The game could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_turn**
> Turn update_turn(turn_id, inline_object3=inline_object3)

Update a turn (used to end a turn)

### Example

```python
from __future__ import print_function
import time
import cyber_py_lib
from cyber_py_lib.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = cyber_py_lib.TurnApi()
turn_id = 'turn_id_example' # str | Which turn to update.
inline_object3 = cyber_py_lib.InlineObject3() # InlineObject3 |  (optional)

try:
    # Update a turn (used to end a turn)
    api_response = api_instance.update_turn(turn_id, inline_object3=inline_object3)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TurnApi->update_turn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **turn_id** | [**str**](.md)| Which turn to update. | 
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | [optional] 

### Return type

[**Turn**](Turn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about units in the current game |  -  |
**400** | Missing turnId or set an invalid status |  -  |
**403** | It is not your turn. |  -  |
**404** | The turn could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

