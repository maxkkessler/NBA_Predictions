def dictify(file_name):
    #takes a one of the player or team files and returns a dict with name or team as the key
    d = {}
    count = 0
    with open('NBA_Predictions/texts/{}'.format(file_name), 'r', encoding='utf-8') as fp:
        while True:
            count += 1
            line = fp.readline()
    
            if not line:
                break
            line = line.replace('[', '')
            line = line.replace(']', '')
            line = line.replace("'", '')
            line = line.replace('"', '')
            line = line.replace(',', '')
            line = line.replace('\n', '')
            l = line.split(' ')
            d[l[0]] = l[1:]
    
    return d

            
    




if __name__ == '__main__':
    team = str(input("Team: \n"))
    date = int(input("Date: \n"))
    d1 = dictify('players {}'.format(date))
    d2 = dictify('teams {}'.format(date))
    players = d2[team]
    for player in players:
        print('{} stats are:\n {}\n'.format(player, d1[player]))
