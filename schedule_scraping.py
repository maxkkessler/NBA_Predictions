from bs4 import BeautifulSoup
import requests



#This scrapes the schedules from a particular year and puts it in a text file

def team_scraping(date, playoffs):

    breaker = 0         #if playoffs is on playoff games are included

    #create files
    file = open("NBA_Predictions/texts/schedule {}".format(date), 'w')
    file.write('')
    file.close()

    file = open("NBA_Predictions/texts/schedule {}".format(date), 'w')
    file.write('')
    file.close()

    months = ['october-2019','october', 'november', 'december', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october-2020']
    for month in months:
        
        if breaker:     #checks if breaker was turned on i.e. no playoff games
            break

        address = 'https://www.basketball-reference.com/leagues/NBA_{}_games-{}.html'.format(date, month)

        html_text = requests.get(address).text
        soup = BeautifulSoup(html_text, 'lxml')
        
        
        body = soup.find('tbody')
        if not body:                #Essentially checks if this is a real page, if it is not it won't have body (hopefully). Some seasons do not have all the months
            continue

        if int(date) == 2020 and month == 'april':  #An exception. If this address takes us to the april schedule that was not actually played
            continue 


        games = body.find_all('tr')     #gets all the games 
        for game in games:

            # Have to skip the playoff banner and decide if playoffs are included or not
            if game.find('th').text == 'Playoffs':
                if playoffs =='off':
                    breaker = 1
                    break
                else:
                    continue

            stuff = game.find_all('td') #gets the actual game

            offset = 0      #this assumes we do not need to skip the first box i.e. start time

            if stuff[0]['data-stat'] != "visitor_team_name":        #checks if it includes start time or not. Some seasons have the start time and some do not
                offset = 1      #Will allows us to skip start time

            visitor_team = stuff[offset]['csk'][:3]
            v_pts = stuff[offset+1].text
            home_team = stuff[offset+2]['csk'][:3]
            h_pts = stuff[offset+3].text
            if stuff[offset+5].text: 
                OT = 1
            else:
                OT = 0
            attendance = stuff[offset+6].text
            
            ls = [home_team, visitor_team, h_pts, v_pts, OT, attendance]
            
            f = open('NBA_Predictions/texts/schedule {}'.format(date), 'a', encoding='utf-8')
            f.write('{}, {}, {}\n'.format(ls[0], ls[1], ls[2:]))
            f.close()

if __name__ == '__main__':
    playoffs = str(input('Input "on" if you want to include playoffs and "off" if you don\'t: '))
    start = int(input('Input start date: '))
    stop = int(input('Input stop date: '))
    for date in range(start, stop, 1):
        team_scraping(date, playoffs)
