import pandas as pd
import matplotlib.pyplot as plt

#teams = ['ANA','ARI','BOS','BUF','CAR','CGY','CHI','CBJ','COL','DAL','DET','EDM','FLA','L.A','MIN','MTL','NSH','N.J','NYI','NYR','OTT','PHI','PIT','S.J','STL','T.B','TOR','VAN','VGK','WPG','WSH']
teams = [
    ('Anaheim Ducks','ANA'),('Arizona Coyotes','ARI'),('Boston Bruins','BOS'),
    ('Buffalo Sabres','BUF'),('Carolina Hurricanes','CAR'),('Calgary Flames','CGY'),
    ('Chicago Blackhawks','CHI'),('Columbus Blue Jackets','CBJ'),('Colorado Avalanche','COL'),
    ('Dallas Stars','DAL'),('Detroit Red Wings','DET'),('Edmonton Oilers','EDM'),
    ('Florida Panthers','FLA'),('Los Angeles Kings','L.A'),('Minnesota Wild','MIN'),
    ('Montreal Canadiens','MTL'),('Nashville Predators','NSH'),('New Jersey Devils','N.J'),
    ('New York Islanders','NYI'),('New York Rangers','NYR'),('Ottawa Senators','OTT'),
    ('Philadelphia Flyers','PHI'),('Pittsburgh Penguins','PIT'),('San Jose Sharks','S.J'),
    ('St.Louis Blues','STL'),('Tampa Bay Lightning','T.B'),('Toronto Maple Leafs','TOR'),
    ('Vancouver Canucks','VAN'),('Vegas Golden Knights','VGK'),('Winnipeg Jets','WPG'),
    ('Washington Capitals','WSH')
]
'''
teams = [
    ('Anaheim Ducks','ANA'),('Arizona Coyotes','ARI'),('Boston Bruins','BOS')
]'''

data = pd.read_csv('skaters_small.csv')


def process_team(team):
    team_data = data.query('team=="' + team[1] + '" and situation=="all" and games_played>=10')
    team_data = team_data.sort_values(ascending=False, by='I_F_points')
    
    total_assists = []
    points_per_game = []
    for line in team_data.iterrows():
        a = line[1]['I_F_primaryAssists'] + line[1]['I_F_secondaryAssists']
        total_assists.append(a)
        try:
            ppg = int(line[1]['I_F_points']) / int(line[1]['games_played'])
        except:
            ppg = 0
        
        ppg = round(ppg, 2)
        points_per_game.append(ppg)

    team_data['I_F_assists'] = total_assists
    team_data['I_F_ppg'] = points_per_game
    
    
    out_data = team_data.sort_values(ascending=False, by='I_F_ppg')
    out_data = out_data[['name','games_played','I_F_goals','I_F_assists','I_F_points','I_F_ppg']]

    print(out_data)

    # matplotlib
    fig, ax = plt.subplots()

    people = out_data['name']
    points = out_data['I_F_ppg']

    for i, v in enumerate(points):
        ax.text(v + .005, i + .3, str(v), color='red', size='8')
    ax.barh(people, points)
    ax.set_yticklabels(people)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Points Per Game\n(at least 10 gp)')
    ax.set_title(team[0] + '\n2018-2019 Points Per Game')
    fig.set_size_inches((10, 6))

    plt.tight_layout()
    plt.savefig('figures/' + team[1] + '.png')

for team in teams:
    process_team(team)