"""
Role:       	Player (complement to space-wars-extended.py)
Author:     	Songkomkrit Chaiyakan
Github link:	https://github.com/songkomkrit/GameAnalytics

"""

import microgear.client as client
import time
import datetime

# NETPIE
appid = "SongkomkritIoT"
gearkey = "8btiHfpRazatGmb"
gearsecret = "RohBYJNo7zoAk4onKvpjltnPB"

client.create(gearkey, gearsecret, appid, {'debugmode': True})
# client.setalias("Player")
client.setalias(PLAYER_NAME)

def callback_connect():
    print("Now I am connected with netpie")

def callback_message(topic, msg):
    # msg is in the form of "b'player,summary[player]['group'],info['time']'" 
    ls = msg.strip('b\'').split(',')
    time = datetime.datetime.fromtimestamp(float(ls[2]))
    time = f'{time:%Y-%m-%d %H:%M:%S}'
    print('Name = ' + ls[0] + ' | Type = ' + ls[1] + ' | Last Played = ' + time)

def callback_error(msg):
    print("error", msg)

client.on_connect = callback_connect 
client.on_message = callback_message 
client.on_error = callback_error 
client.subscribe("/group")
client.connect(False)

prev = time.time()

def push(cur, player, state, 
         x, y, coin, destroyed, shot):
    
    ls = [cur, player, state, 
          x, y, coin, destroyed, shot]  
    msg = ','.join([str(e) for e in ls])
    
    client.publish("/game", msg)