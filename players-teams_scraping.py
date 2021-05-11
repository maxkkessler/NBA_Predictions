from bs4 import BeautifulSoup
import requests



#Scraped the player stats creating text files of them
#Also creates a text file of the teams with all the players

def scrape(address, date):
    html_text = requests.get(address).text
    soup = BeautifulSoup(html_text, 'lxml')
    names = set()
    teams = {}

    #create files
    file = open("NBA_Predictions/texts/players {}".format(date), 'w')
    file.write('test')
    file.close()

    file = open("NBA_Predictions/texts/teams {}".format(date), 'w')
    file.write('test')
    file.close()

    file = open("NBA_Predictions/texts/players {}".format(date),"r+")
    file.truncate(0)
    file.close()

    file = open("NBA_Predictions/texts/teams {}".format(date),"r+")
    file.truncate(0)
    file.close()



    #print(html_text)
    players = soup.find_all('tr', class_= 'full_table')
    for player in players:
        lefts = player.find_all('td', class_ = 'left')
        name = lefts[0]['csk']
        
        if name in names:       #check if player is a repeat
            continue
        else:
            names.add(name)

        if lefts[1].a != None:
            team_id = lefts[1].a.text
        else:
            continue
   
        
        pos = player.find('td', class_ = 'center').text

        # we have name, team_id, and pos
        # every other stat will be in rights
        rights = player.find_all('td', class_='right' or 'right non_qual' or 'right iz' or 'right non_qual iz')

        age = rights[0].text
        g = rights[1].text
        gs = rights[2].text
        mp_per_g = rights[3].text
        fg_per_g = rights[4].text
        fga_per_g = rights[5].text
        fg_pct = rights[6].text
        fg3_per_g = rights[7].text
        fg3a_per_g = rights[8].text
        fg3_pct = rights[9].text
        fg2_per_g = rights[10].text
        fg2a_per_g = rights[11].text
        fg2_pct = rights[12].text
        efg_pct = rights[13].text
        ft_per_g = rights[14].text
        fta_per_g = rights[15].text
        ft_pct = rights[16].text
        orb_per_g = rights[17].text
        drb_per_g = rights[18].text
        trb_per_g = rights[19].text
        ast_per_g = rights[20].text
        stl_per_g = rights[21].text
        blk_per_g = rights[22].text
        tov_per_g = rights[23].text
        pf_per_g = rights[24].text
        pts_per_g = rights[25].text

    

        stats = [name, pos, age, team_id, g, gs, mp_per_g, fg_per_g, fga_per_g, 
        fg_pct, fg3_per_g, fg3a_per_g, fg3_pct, fg2_per_g, fg2a_per_g, fg2_pct,
        efg_pct, ft_per_g, fta_per_g, ft_pct, orb_per_g, drb_per_g, trb_per_g, 
        ast_per_g, stl_per_g, blk_per_g, tov_per_g, pf_per_g, pts_per_g]

        if team_id not in teams:
            teams[team_id] = [name]
        else:
            teams[team_id].append(name)



        f = open('NBA_Predictions/texts/players {}'.format(date), 'a', encoding='utf-8')
        f.write('{}, {}\n'.format(stats[0], stats[1:]))
        f.close()

    for team in teams:
        f = open('NBA_Predictions/texts/teams {}'.format(date), 'a', encoding='utf-8')
        f.write('{}, {}\n'.format(team, teams[team]))
        f.close()


if __name__ == '__main__':
    print("This retrieves NBA data from start date to end date")
    start = int(input("Start date: "))
    end = int(input("End date: "))
    print("Retrieving...")
    for date in range(start, end, 1):   
        html = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'.format(date)
        scrape(html, date)
    print("Done")
