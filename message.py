"""
Role:       	Server (complement to server.py)
Author:     	Songkomkrit Chaiyakan
Github link:	https://github.com/songkomkrit/GameAnalytics

"""

def pull(msg):
    ls = msg.strip('b\'').split(',')

    '''
        ls = [cur, player, state, 
              x, y, coin, destroyed, shot]
    '''
          
    info = OrderedDict({
        'player': ls[1],
        'time': float(ls[0]),
        'state': ls[2],    # play, over, quit
        'x': int(ls[3]),
        'y': int(ls[4]),
        'coin': int(ls[5]),
        'destroyed': int(ls[6]),
        'shot': int(ls[7]),
        'shot_no_enemy': int(ls[7]) - int(ls[6])
    })
    
    return info


def push_record(info):
    filename = 'log-record.json'

    with open(filename, 'r') as infile:
        try:
            old_data = json.load(infile)
        except JSONDecodeError:
            old_data = []
    
    data = old_data + [info]
    
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)