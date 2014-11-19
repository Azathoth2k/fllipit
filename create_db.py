from fllipit import DB, Team
import random

DB.create_all()

for i in range(80):
    team = Team(
        number=i,
        name="My Team %i" % (i),
        affiliation="Some %i School" % (i),
        round1=random.randrange(0, 400, 1),
        round2=random.randrange(0, 400, 1),
        round3=random.randrange(0, 400, 1))
    DB.session.add(team)
    
DB.session.commit()
