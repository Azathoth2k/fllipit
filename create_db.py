from flask.ext.sqlalchemy import SQLAlchemy
from models import DB, Team
from fllipit import APP
import api
import random

DB.app = APP
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

# Top 12
for team in api.rankTeams(teams)[:12]:
    team.advanceTo4 = True
    team.round4=random.randrange(0, 400, 1)

# Top 4
for team in sorted(teams, key=lambda x: x.round4, reverse=True)[:4]:
    team.advanceTo5 = True
    team.round5=random.randrange(0, 400, 1)

#Top 2
for team in sorted(teams, key=lambda x: x.round5, reverse=True)[:2]:
    team.advanceTo6 = True
    team.round6=random.randrange(0, 400, 1)
    
# Add all teams to database
for team in teams:
    DB.session.add(team)
    
DB.session.commit()

