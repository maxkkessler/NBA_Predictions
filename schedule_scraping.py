from bs4 import BeautifulSoup
import requests


def team_scraping(date, playoffs):

    breaker = 0         #if playoffs is on playoff games are included

    #create files
    file = open("NBA_Predictions/texts/schedule {}".format(date), 'w')
    file.write('')
    file.close()

    file = open("NBA_Predictions/texts/schedule {}".format(date), 'w')
    file.write('')
    file.close()

    months = ['october', 'november', 'december', 'january', 'february', 'march', 'april', 'may', 'june']
    for month in months:
        
        if breaker:     #checks if breaker was turned on i.e. no playoff games
            break

        address = 'https://www.basketball-reference.com/leagues/NBA_{}_games-{}.html'.format(date, month)

        html_text = requests.get(address).text
        soup = BeautifulSoup(html_text, 'lxml')
        
        
        body = soup.find('tbody')
        if not body:
            continue

        games = body.find_all('tr')     #gets all the games 
        for game in games:

            start_time = None      # sets the start time to None so that if the game is before 2001 they still have a start time

            offset = 0      # this will allow me to ignore start time if necessary

            # if the game is before 2001 there is no start time
            if int(date) < 2001:
                offset = -1

            # Have to skip the playoff banner
            if game.find('th').text == 'Playoffs':
                if playoffs =='off':
                    breaker = 1
                    break
                else:
                    continue
                

            stuff = game.find_all('td')

            if offset == 0:         #checks if date is before 2001
                start_time = stuff[offset].text

            visitor_team = stuff[offset+1]['csk'][:3]
            v_pts = stuff[offset+2].text
            home_team = stuff[offset+3]['csk'][:3]
            h_pts = stuff[offset+4].text
            if stuff[offset+6].text: 
                OT = 1
            else:
                OT = 0
            attendance = stuff[offset+7].text
            
            ls = [home_team, visitor_team, h_pts, v_pts, OT, attendance, start_time]
            
            f = open('NBA_Predictions/texts/schedule {}'.format(date), 'a', encoding='utf-8')
            f.write('{}, {}, {}\n'.format(ls[0], ls[1], ls[2:]))
            f.close()

if __name__ == '__main__':
    playoffs = str(input('Input "on" if you want to include playoffs and "off" if you don\'t: '))
    start = int(input('Input start date: '))
    stop = int(input('Input stop date: '))
    for date in range(start, stop, 1):
        team_scraping(date, playoffs)
