# Real-Time Game Analytics


## Description
This is a class project. It extends the SpaceWars game source code originally written by Dan Petersson. Please visit <https://github.com/DanPetersson/SpaceWars> for further details.

A player name must be entered before the game starts. A player receives a coin when earning additional five scores and knows his/her player type right after finishing each game. A game ends when it is over or when a player accidentally quits the program. In this project, four player types (Baffa, Bicalho, & Feijo, 2019) are available:

  1. hardcore achiever,
  2. hardcore killer,
  3. casual achiever, and
  4. casual killer.

This classification is based on average performance of an individual player in comparison to the rest of game players collected in a server log as illustrated in the file *implementation.pdf*. NETPIE (Network Platform for Internet of Everything) is used as a cloud platform. The *microgear* package is required. Please visit <https://netpie.io> for more information.

Notepad++ (visit <https://notepad-plus-plus.org>) is a recommended code editor. It can also be used to create and view a JSON file.

If there are any mistakes, please contact me at songkomkrit.c@gmail.com.


## Components

### Player

  * **space-wars-extended.py :** main source code (Petersson's file *space_wars.py* with extension)
  * **addition.py :** addition to the main source code
  * **player.py :** publishing a player move and subscribing a player type
  * **/images/coin.png :** coin image

### Server

  * **server.py :** main source code (subscribing a player move and publishing a player type)
  * **message.py :** extracting the received message from a player and storing a record in JSON format
  * **classify.py :** classifier

### Server Logs (Not Included)

  * **log-record.json :** relevant information on moves per second made by each player
  * **log-player-detailed.json :** player types across all games played by each player
  * **log-player-updated.json :** player type of the most recent game for each player


## Reference

Bicalho, L. F., Baffa, A., & Feijó, B. (2019, October). A game analytics model to identify player profiles in singleplayer games. In *2019 18th Brazilian Symposium on Computer Games and Digital Entertainment (SBGames)* (pp. 11-20). IEEE. DOI: <https://dx.doi.org/10.1109/SBGames.2019.00013>
