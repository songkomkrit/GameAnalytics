import microgear.client as client
import logging
import time

import json
from json.decoder import JSONDecodeError

appid = "SongkomkritIoT"
gearkey = "8btiHfpRazatGmb"
gearsecret = "RohBYJNo7zoAk4onKvpjltnPB"

client.create(gearkey, gearsecret, appid, {'debugmode': True})
client.setalias("Subscriber")

exec(open('message.py').read())
exec(open('classify.py').read())

def callback_connect():
    print ("Now I am connected with netpie")

with open('log-player-updated.json', 'r') as infile:
    try:
        summary = json.load(infile)
    except JSONDecodeError:
        summary = dict()

num_players = len(summary)
X = [[-1000*v]*6 for v in range(1,5)]
reserved = '#@$'
P = [reserved]*4

if num_players > 0:
    i = 0
    
    for player in summary.keys():
        X.append(summary[player]['attr'])
        P.append(player)
        
        if i < 4:
            X.pop(0)
            P.pop(0)
        
        i += 1
        

def callback_message(topic, msg):
    print(topic, ": ", msg)
    global summary, num_players, X, P
    info = pull(msg)
    push_record(info)
    player = info['player']
    
    
    if player not in summary:
        # attr = avg of ['x', 'y', 'coin', 'destroyed', 'shot', 'shot_no_enemy']
        summary.update({player: {'group': 'null',
                                 'time': 0,
                                 'count': 0,
                                 'attr': [0]*6}})
        
        if num_players < 4:
            X.pop(0)
            P.pop(0)
    
    
    if info['state'] != 'play':
        summary[player]['time'] = info['time']
        summary[player]['count'] += 1
        count = summary[player]['count']
        
        cur_attr = []
        
        for i, v in enumerate(['x', 'y', 'coin', 'destroyed', 'shot', 'shot_no_enemy']):
            cur_attr.append(info[v])
            summary[player]['attr'][i] = ((count-1)*summary[player]['attr'][i] + info[v])/count

        
        if player in P:
            X.pop(P.index(player))
            P.remove(player)
        else:
            num_players += 1
        
        X.append(summary[player]['attr'])
        P.append(player)
        list_group = classify(X)
           
        for i in range(len(P)):
            if P[i] != '#@$':
                summary[P[i]]['group'] = list_group[i]
        
        client.publish("/group", player + ',' + summary[player]['group'])
        
        with open('log-player-updated.json', 'w', encoding='utf-8') as outfile:
            json.dump(summary, outfile, ensure_ascii=False, indent=4)
         
         
        current = {'player': player,
                   'group': summary[player]['group'],
                   'time': info['time'],
                   'count': count,
                   'attr': cur_attr}    

        with open('log-player-detailed.json', 'r') as infile:
            try:
                old_data = json.load(infile)
            except JSONDecodeError:
                old_data = []
                
        data = old_data + [current]

        with open('log-player-detailed.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)

       
def callback_error(msg):
    print("error", msg)

client.on_connect = callback_connect
client.on_message = callback_message
client.on_error = callback_error
client.subscribe("/game")
client.connect(True)