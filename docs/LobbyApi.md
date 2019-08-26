# cyber_py_lib.LobbyApi

All URIs are relative to *http://No Production URL yet*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_player**](LobbyApi.md#add_player) | **POST** /player | Add a player to a game
[**create_game**](LobbyApi.md#create_game) | **POST** /game | Create a game
[**get_game**](LobbyApi.md#get_game) | **GET** /game/{gameId} | Get a specific game you know the ID for.
[**get_maps**](LobbyApi.md#get_maps) | **GET** /maps | Get all maps
[**get_player**](LobbyApi.md#get_player) | **GET** /player/{playerId} | get a player by id


# **add_player**
> Player add_player(inline_object1=inline_object1)

Add a player to a game

### Example

```python
from __future__ import print_function
import time
import cyber_py_lib
from cyber_py_lib.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = cyber_py_lib.LobbyApi()
inline_object1 = cyber_py_lib.InlineObject1() # InlineObject1 |  (optional)

try:
    # Add a player to a game
    api_response = api_instance.add_player(inline_object1=inline_object1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LobbyApi->add_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | [optional] 

### Return type

[**Player**](Player.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Player information |  -  |
**403** | The game is full. |  -  |
**404** | The game could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_game**
> Game create_game(inline_object=inline_object)

Create a game

### Example

```python
from __future__ import print_function
import time
import cyber_py_lib
from cyber_py_lib.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = cyber_py_lib.LobbyApi()
inline_object = cyber_py_lib.InlineObject() # InlineObject |  (optional)

try:
    # Create a game
    api_response = api_instance.create_game(inline_object=inline_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LobbyApi->create_game: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

[**Game**](Game.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The meta information about a game, including map tile data. |  -  |
**400** | The map id was not provided. |  -  |
**404** | The map could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_game**
> Game get_game(game_id)

Get a specific game you know the ID for.

### Example

```python
from __future__ import print_function
import time
import cyber_py_lib
from cyber_py_lib.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = cyber_py_lib.LobbyApi()
game_id = 'game_id_example' # str | Which game's ID to retrieve

try:
    # Get a specific game you know the ID for.
    api_response = api_instance.get_game(game_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LobbyApi->get_game: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | [**str**](.md)| Which game&#39;s ID to retrieve | 

### Return type

[**Game**](Game.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The meta information about a game, including map tile data. |  -  |
**404** | The game could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maps**
> list[Map] get_maps()

Get all maps

### Example

```python
from __future__ import print_function
import time
import cyber_py_lib
from cyber_py_lib.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = cyber_py_lib.LobbyApi()

try:
    # Get all maps
    api_response = api_instance.get_maps()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LobbyApi->get_maps: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Map]**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of playable maps |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player**
> Player get_player(player_id)

get a player by id

### Example

```python
from __future__ import print_function
import time
import cyber_py_lib
from cyber_py_lib.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = cyber_py_lib.LobbyApi()
player_id = 'player_id_example' # str | Which player's ID to retrieve

try:
    # get a player by id
    api_response = api_instance.get_player(player_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LobbyApi->get_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | [**str**](.md)| Which player&#39;s ID to retrieve | 

### Return type

[**Player**](Player.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Player information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

