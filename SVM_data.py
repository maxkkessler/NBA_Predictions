# We are gonna take combine the stats of the top 8 players by minutes and then subtract the stats of the away team from them
# Just try to combine everything into one kinda

from schedule_builder import schedule_bulder
from dictify import dictify
import numpy as np

def normalize(arr):
    d = 0
    for i in arr:
        d += i**2
    d = d**(1/2)
    for index in range(len(arr)):
        arr[index] = arr[index] / d

def add_arrays(arr1, arr2):
    arr3 = []
    for index in range(len(arr1)):
        n1 = 0
        n2 = 0
        if arr1[index] != '':
            n1= float(arr1[index])

        if arr2[index] != '':
            n2= float(arr2[index])
        
        arr3.append(n1+n2)
    return arr3

def subtract(arr1, arr2):
    arr3 = []
    for index in range(len(arr1)):
        arr3.append(arr1[index]-arr2[index])
    return arr3


#Function gets the stats of all the top players on all teams and combines them in a dictionary by team name. Top 7 players are included
def teams_stats(date):
    teams = dictify('teams {}'.format(date), 'teams')
    players = dictify('players {}'.format(date), 'players')
    d = {}        #dictionary holding all the team stats
    count = 0 

    #Recall minitues is 5 index
    for team in teams.items():
        name = team[0]
        players_on_team = team[1]
        #We have our team name and the players on that team

        mins = []
        for p in players_on_team:
            stats = players[p]
            mins.append(float(stats[5]))

        mins.sort(reverse=True)     # sorted list of minutes played
        cutoff = mins[6]     #abitrary cutoff. Not gonna count the people who dont play that much, only top 7


        for p in players_on_team:
            stats = players[p]
            playing_time = float(stats[5])

            #remove the non numerical data
            stats.pop(0)
            stats.pop(1)
            stats.pop(3)

            if playing_time >= cutoff:
                if name in d:
                    d[name] = add_arrays(d[name], stats)
                else:
                    d[name] = stats
    return d


#Does every matchup of the season subtracting the total team stats, home-away
def data_combo(date):   
    schedule = schedule_bulder('schedule {}'.format(date))      #get the schedule for the year
    stats = teams_stats(date)

    target = []     #contains wins/losses
    data = []       #contains the data


    # Recall data is in ['home', home_win, home_pts, away_pts, away]
    # We only wanna look at home games

    for item in schedule.items():
        name = item[0]      #gets the team name
        games = item[1]     #gets the game stats

        for game in games:
            if game[0] == 'home':        #only want home games
                if game[1] == 'win':
                    target.append(1)
                    home = name
                    away = game[4]
                    array = subtract(stats[home], stats[away])
                    normalize(array)
                    data.append(array)

                else:
                    target.append(0)
                    home = name
                    away = game[4]
                    array = subtract(stats[home], stats[away])
                    normalize(array)
                    data.append(array)
    
    return (data, target)



if __name__ == '__main__':
    
    data, target = data_combo(2019)
    print(data)
    