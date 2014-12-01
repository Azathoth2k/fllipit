from flask.ext import restful
from flask.ext.restful import Resource, Api, fields, marshal_with
from fllipit import APP
from models import DB, Team
import pypyodbc

API = Api(APP)


# Get teams from the database
def getTeams():
    teams = []
    if APP.config['TEST_DB']:
        # In test mode, use the sqlite database
        teams = Team.query.all()
        for team in teams:
            team.sortScores()
    else:
        # In production mode, get the data from the Access database
        # Create the database connection
        conn = pypyodbc.connect(
            r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
            r"Dbq="+APP.config['DB_FILE']+";")
        cur = conn.cursor()

        # Get the data from the database
        cur.execute(
            """
            SELECT TeamNumber, TeamName, Affiliation,
            Trial1Score, Trial2Score, Trial3Score,
            Trial4Score, Trial5Score, Trial6Score, Trial7Score,
            Round4ProceedTo, Round5ProceedTo,
            Round6ProceedTo, Round7ProceedTo
            FROM ScoringSummaryQuery
            """)

        # Build the list of Team objects
        for row in cur.fetchall():
            # Build the team object
            team = Team(
                number=row[0],
                name=row[1],
                affiliation=row[2],
                round1=row[3],
                round2=row[4],
                round3=row[5],
                round4=row[6],
                round5=row[7],
                round6=row[8],
                round7=row[9],
                advanceTo4=row[10],
                advanceTo5=row[11],
                advanceTo6=row[12],
                advanceTo7=row[13])

            # Add the current team to the list of all teams
            teams.append(team)

        # Close the database connection
        cur.close()
        conn.close()
    
    return teams

def rankTeams(teams):
    return sorted(
        teams,
        key=lambda x: (x.bestScore, x.secondBestScore, x.worstScore),
        reverse=True)


# Setup the fields that will be used in the JSON output
teamFields = {
    "number": fields.Integer,
    "name": fields.String,
    "affiliation": fields.String,
    "round1": fields.Integer,
    "round2": fields.Integer,
    "round3": fields.Integer,
    "bestScore": fields.Integer,
    "rank": fields.Integer
}


playoffFields = {
    "number": fields.Integer,
    "name": fields.String,
    "score": fields.Integer
}


class Rankings(Resource):

    """Setup a REST resource for the Team data."""

    @marshal_with(teamFields)
    def get(self):
        teams = getTeams()
             
        i = 1
        for team in rankTeams(teams):
            team.rank = i
            i += 1
        
        return sortedTeams


class Playoffs(Resource):
    
    """Setup a REST resource for the playoff data"""
    
    @marshal_with(playoffFields)
    def get(self, roundNumber):
        # Get only the teams that are marked to advance to the selected round
        teams = [t for t in getTeams() if t.isAdvancingToRound(roundNumber)]
        
        if roundNumber <= 4:
            # If this is the first playoff round, return team list sorted by qualifying rank
            return rankTeams(teams)
        else:
            # Return team list sorted by scores from previous round
            return sorted(
                teams,
                key=lambda x: x.getRoundScore(roundNumber-1),
                reverse=True)

# map resource to URL
API.add_resource(Rankings, '/api/teams')
API.add_resource(Playoffs, '/api/playoffs/<int:roundNumber>')