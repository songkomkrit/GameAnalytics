def pull(msg):
    arr = msg.strip('b\'').split(',')

    '''
        ls = [cur, player, state, 
              x, y, coin, destroyed, shot]
    '''
          
    info = {
        'player': arr[1],
        'time': float(arr[0]),
        'state': arr[2],    # play, over, quit
        'x': int(arr[3]),
        'y': int(arr[4]),
        'coin': int(arr[5]),
        'destroyed': int(arr[6]),
        'shot': int(arr[7]),
        'shot_no_enemy': int(arr[7]) - int(arr[6])
    }
    
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