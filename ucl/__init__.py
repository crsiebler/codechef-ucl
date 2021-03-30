import sys

TEST_CASE_SIZE = 12

class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.diff = 0

    def __repr__(self):
        return 'Team: {0}\tPoints: {1}\tDiff: {2}\n'.format(self.name, str(self.points), str(self.diff))

input = sys.stdin.readlines()

for count in range(0, int(input[0])):
    teams = {}
    
    lower = count * TEST_CASE_SIZE + 1
    upper = (count + 1) * TEST_CASE_SIZE + 1
    
    for i in range(lower, upper):
        game = input[i].strip()
        homeTeam = game.split('vs.')[0].strip().split(' ')[0]
        homeScore = int(game.split('vs.')[0].strip().split(' ')[1])
        awayTeam = game.split('vs.')[1].strip().split(' ')[1]
        awayScore = int(game.split('vs.')[1].strip().split(' ')[0])
        
        if homeTeam not in teams.keys():
            teams[homeTeam] = Team(homeTeam)
            
        if awayTeam not in teams.keys():
            teams[awayTeam] = Team(awayTeam)
        
        if homeScore > awayScore:
            teams[homeTeam].points = teams[homeTeam].points + 3
            teams[homeTeam].diff = teams[homeTeam].diff + (homeScore - awayScore)
            teams[awayTeam].diff = teams[awayTeam].diff + (awayScore - homeScore)
        elif awayScore > homeScore:
            teams[awayTeam].points = teams[awayTeam].points + 3
            teams[awayTeam].diff = teams[awayTeam].diff + (awayScore - homeScore)
            teams[homeTeam].diff = teams[homeTeam].diff + (homeScore - awayScore)
        else:
            teams[homeTeam].points = teams[homeTeam].points + 1
            teams[awayTeam].points = teams[awayTeam].points + 1
    
    standings = sorted(teams.items(), key=lambda kv: (kv[1].points, kv[1].diff))
    print("{0} {1}".format(standings.pop()[0], standings.pop()[0]))
    
    teams.clear()
