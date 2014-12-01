from models import DB, Team
import api
import random

DB.create_all()

teams = []
for i in range(80):
    team = Team(
        number=i,
        name="My Team %i" % (i),
        affiliation="Some %i School" % (i),
        round1=random.randrange(0, 400, 1),
        round2=random.randrange(0, 400, 1),
        round3=random.randrange(0, 400, 1))
    teams.append(team)

sortedTeams = api.rankTeams(teams)

# TODO add playoff round scores to top 12/4/2    
    
for team in teams:
    DB.session.add(team)
    
DB.session.commit()

