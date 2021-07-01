# Game Analytics


## Description
This is a class project. It extends the exisiting codes on SpaceWars game originally written by Dan Petersson. Please visit <https://github.com/DanPetersson/SpaceWars> for futher details.

A player receives a coin when earning additional five scores. His/her type is known right after finishing each game. A game ends when it is over or when a player accidentally quit the program. In this project, four player types (Baffa, Bicalho, & Feijo, 2019) are available:

  1. hardcore achiever,
  2. hardcore killer,
  3. casual achiever, and
  4. casual killer.

This classification is based on average performance of an individual player collected in a server log. NETPIE (Network Platform for Internet of Everything) is used as a cloud platform. The *microgear* package is required. Please visit <https://netpie.io> for more information.


## Components

### Player

  * **space-wars-extended.py :** main source code
  * **addition.py :** addition to the main source code
  * **player.py :** publishing move and subscribing type

### Server

  * **server.py :** main source code (subscribing player move and publishing player type)
  * **message.py :** extracting received message from player and storing record in JSON format
  * **classify.py :** classifier

### Server Logs

  * **log-record.json :** collecting information on a player move in every second
  * **log-player-detailed.json :** collecting all player types
  * **log-player-updated.json :** collecting a recent player type
