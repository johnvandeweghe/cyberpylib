# cyber-py-lib
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.2.0
- Package version: 0.2.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cyber_py_lib 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cyber_py_lib
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cyber_py_lib
from cyber_py_lib.rest import ApiException
from pprint import pprint


# Defining host is optional and default to http://No Production URL yet
configuration.host = "http://No Production URL yet"
# Create an instance of the API class
api_instance = cyber_py_lib.GameApi(cyber_py_lib.ApiClient(configuration))
unit_id = 'unit_id_example' # str | Which unit to retrieve

try:
    # Get a specific unit
    api_response = api_instance.get_unit(unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GameApi->get_unit: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://No Production URL yet*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GameApi* | [**get_unit**](docs/GameApi.md#get_unit) | **GET** /unit/{unitId} | Get a specific unit
*GameApi* | [**get_units**](docs/GameApi.md#get_units) | **GET** /units/{gameId} | Get units for a game.
*LobbyApi* | [**add_player**](docs/LobbyApi.md#add_player) | **POST** /player | Add a player to a game
*LobbyApi* | [**create_game**](docs/LobbyApi.md#create_game) | **POST** /game | Create a game
*LobbyApi* | [**get_game**](docs/LobbyApi.md#get_game) | **GET** /game/{gameId} | Get a specific game you know the ID for.
*LobbyApi* | [**get_maps**](docs/LobbyApi.md#get_maps) | **GET** /maps | Get all maps
*LobbyApi* | [**get_player**](docs/LobbyApi.md#get_player) | **GET** /player/{playerId} | get a player by id
*TurnApi* | [**create_unit_action**](docs/TurnApi.md#create_unit_action) | **POST** /unitAction | Take an action as a unit on a turn.
*TurnApi* | [**start_turn**](docs/TurnApi.md#start_turn) | **POST** /turns | Start a turn
*TurnApi* | [**update_turn**](docs/TurnApi.md#update_turn) | **PATCH** /turns/{turnId} | Update a turn (used to end a turn)


## Documentation For Models

 - [AttackActionArgs](docs/AttackActionArgs.md)
 - [Coordinates](docs/Coordinates.md)
 - [Game](docs/Game.md)
 - [GameMap](docs/GameMap.md)
 - [GameMapTiles](docs/GameMapTiles.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [Map](docs/Map.md)
 - [MoveActionArgs](docs/MoveActionArgs.md)
 - [Player](docs/Player.md)
 - [Turn](docs/Turn.md)
 - [Unit](docs/Unit.md)
 - [UnitAction](docs/UnitAction.md)
 - [UnitActionParams](docs/UnitActionParams.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




