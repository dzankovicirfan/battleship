# Battleship game

Batlleship game done with Python, Django and Django REST framework.
Game for 2 players. It is standard battleship game with 5 ships:
  * Carrier (5 spaces)
  * Battleship (4 spaces)
  * Cruiser (3 spaces)
  * Submarine (3 spaces)
  * Destroyer (2 spaces)

Size of the board is 10 x 10.

Ships are created for both players when game is created.

Account app is for creating users(signup, login, authorization).

Game app is for actualy playing game with API endpoints.

****
****

## Requirements for project
* python3
* virtualenv

## Installation

Clone project, and go in to root of the project.

    $ virutalenv v
    $ source v/bin/activate
    $ cd battleship
    $ pip install -r requirements.txt
    $ python manage.py migrate

    # _runserver localy_
    $ python manage.py runserver


You can access admin page through this url:
http://127.0.0.1:8000/admin/

****
****

## API endpoints
http://127.0.0.1:8000/api/

### Account

Create user on signup, then login with username and password, get JWT token, and use that token for authorization in the app.

More about JWT token: https://getblimp.github.io/django-rest-framework-jwt/

__Sign up__

/attack/signup/

method: __POST__

    {
      "username": "test",
      "password": "testpassword123!$"
    }

__Login__

/attack/login/

method: __POST__

    {
      "username": "test",
      "password": "testpassword123!$"
    }

as a response you get JWT token.

    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImlyZmFuIiwiZXhwIjoxNTQ1OTA2MTYyLCJlbWFpbCI6IiJ9.SLR5fRWWzju-rGvn7pgLnjB09RNFVog6CzPe0T-K3eM"
    }

Use that token in request Headers for authorization.

    'Content-Type': "application/json",
    'Authorization': "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImlyZmFuIiwiZXhwIjoxNTQ1OTA2MTYyLCJlbWFpbCI6IiJ9.SLR5fRWWzju-rGvn7pgLnjB09RNFVog6CzPe0T-K3eM"

****

## Game

### Creating game
Game model has GET, POST, PUT, DELETE methods.

endpoint:

      /game/game/
method: __GET__ or __POST__



Get all games(or filter some games), or create new game.

    {
    	"name": "First game",
    	"player1": 1,    # ids of players in a game
    	"player2": 2
    }

Update or delte game:

    /game/game/game_id/


### Positioning ships

After creating game both players should set up their ships.

endpoint:

    /game/shipposition/game_id/

method: __POST__

    [
    	{
    		"ship": 1,
    		"horizontal": true,
    		"x": 1,
    		"y": 1
    	},
    	{
    		"ship": 3,
    		"horizontal": false,
    		"x": 10,
    		"y": 10
    	},
    	{
    		"ship": 5,
    		"horizontal": true,
    		"x": 1,
    		"y": 3
    	},
    	{
    		"ship": 7,
    		"horizontal": true,
    		"x": 1,
    		"y": 4
    	},
    	{
    		"ship": 9,
    		"horizontal": false,
    		"x": 5,
    		"y": 10
    	}
    ]

* __ship__ is ship id
* __horizontal__ is true or false, chose if you want to set your ship horizontal or verical
* __x__ is integer in range 1-10
* __y__ is integer in range 1-10


Both players should set up their ships.

### Playing game

You play game by attacking your opponent. Game is finished when one player hits all the ships of the opponent.

endpoint:

    /game/attack/

method: __POST__

    {
      "game": 1,
      "x": 1,
      "y": 2
    }

* __game__ is id of the game
* __x__ is integer in ragne 1-10
* __y__ is integer in ragne 1-10

response is the attack object:

    {
      "game": 1,
      "x": 1,
      "y": 2,
      "hit": true
    }

where you can see if your attack was succesfull.
