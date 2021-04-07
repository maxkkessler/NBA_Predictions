def schedule_bulder(file_name):
    #takes a one of the player or team files and returns a dict with name or team as the key
    d = {}
    count = 0
    with open('NBA_Predictions/texts/{}'.format(file_name), 'r', encoding='utf-8') as fp:
        while True:
            count += 1
            line = fp.readline()
    
            # parses everything up into a list
            if not line:
                break
            line = line.replace('[', '')
            line = line.replace(']', '')
            line = line.replace("'", '')
            line = line.replace('"', '')
            line = line.replace(',', '')
            line = line.replace('\n', '')
            l = line.split(' ')
            # finished parsing

            home = l[0]
            away = l[1]

            home_pts = l[2]
            away_pts = l[3]


            home_win, away_win = 'loss', 'win'
            if (home_pts == '') or (away_pts == ''):        #means we dont have the game stats i.e 2021
                break
                

            if int(home_pts) > int(away_pts):
                home_win, away_win = 'win', 'loss'

            # Enter game for home team
            home_stats = ['home', home_win, home_pts, away_pts, away]
            away_stats = ['away', away_win, away_pts, home_pts, home]

            # Enter the home teams stats
            if home in d:
                d[home].append(home_stats)
            else:
                d[home] = [home_stats]
            
            # Enter the away team tats
            if away in d:
                d[away].append(away_stats)
            else:
                d[away] = [away_stats]

    return d


if __name__ == '__main__':


    date = int(input('Please input date: '))
    team = str(input('Please input team: '))
    wins = 0
    losses = 0

    d = schedule_bulder('schedule {}'.format(date))


    games = d[team]
    for index, game in enumerate(games):
        print('Game {}: {} {} {} to {} at {} over {}'.format(index, team, game[1], game[2], game[3], game[0], game[4] ))
        if game[1] == 'win':
            wins += 1
        else:
            losses +=1
    
    print('\nRecord for season is {} {}'.format(wins, losses))
