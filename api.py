from flask.ext import restful
from flask.ext.restful import Resource, Api, fields, marshal_with
from fllipit import APP
from models import DB, Team
import pypyodbc

API = Api(APP)

# Setup the fields that will be used in the JSON output
teamFields = {
    "number": fields.Integer,
    "name": fields.String,
    "affiliation": fields.String,
    "round1": fields.Integer,
    "round2": fields.Integer,
    "round3": fields.Integer,
    "round4": fields.Integer,
    "round5": fields.Integer,
    "round6": fields.Integer,
    "round7": fields.Integer,
    "advanceTo4": fields.Boolean,
    "advanceTo5": fields.Boolean,
    "advanceTo6": fields.Boolean,
    "advanceTo7": fields.Boolean,
    "bestScore": fields.Integer
}


class TeamList(Resource):

    """Setup a REST resource for the Jenkins project/ build data."""

    @marshal_with(teamFields)
    def get(self):
        teams = []
        if APP.config['TEST_DB']:
            teams = Team.query.all()
            for team in teams:
                team.bestScore = team.getBestScore()
        else:
            conn = pypyodbc.connect(
                r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" + 
                r"Dbq="+APP.config['DB_FILE']+";")
           
            cur = conn.cursor()
            cur = conn.cursor()
            cur.execute(
                """
                SELECT TeamNumber, TeamName, Affiliation, 
                Trial1Score, Trial2Score, Trial3Score, 
                Trial4Score, Trial5Score, Trial6Score, Trial7Score, 
                Round4ProceedTo, Round5ProceedTo, Round6ProceedTo, Round7ProceedTo 
                FROM ScoringSummaryQuery
                """)
    
            for row in cur.fetchall():
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
                teams.append(team)
            cur.close()
            conn.close()           
        return teams

# map resource to URL
API.add_resource(TeamList, '/api/teams')
