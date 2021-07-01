import microgear.client as client
import time

# NETPIE
appid = "SongkomkritIoT"
gearkey = "8btiHfpRazatGmb"
gearsecret = "RohBYJNo7zoAk4onKvpjltnPB"

client.create(gearkey, gearsecret, appid, {'debugmode': True})
client.setalias("Publisher")

def callback_connect():
    print ("Now I am connected with netpie")

def callback_message(topic, msg):
    # msg is in the form of "b'player,summary[player]['group']'" 
    arr = msg.strip('b\'').split(',')
    print(arr[0] + ': ' + arr[1])

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