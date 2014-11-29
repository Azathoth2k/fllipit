"""This module is the main Flask web application for the FLL Pit Display."""

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful
from flask.ext.restful import Resource, Api, fields, marshal_with
from flask.ext.conditional import conditional
import urllib2
import json
import pypyodbc

APP = Flask(__name__)
APP.config.from_object('config')
API = Api(APP)
DB = SQLAlchemy(APP)


class Team(DB.Model):
    """Store data for a single Team"""
    number = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(200), unique=True)
    affiliation = DB.Column(DB.String(200), unique=True)
    round1 = DB.Column(DB.Integer)
    round2 = DB.Column(DB.Integer)
    round3 = DB.Column(DB.Integer)
    round4 = DB.Column(DB.Integer)
    round5 = DB.Column(DB.Integer)
    round6 = DB.Column(DB.Integer)
    round7 = DB.Column(DB.Integer)
    advanceTo4 = DB.Column(DB.Boolean)
    advanceTo5 = DB.Column(DB.Boolean)
    advanceTo6 = DB.Column(DB.Boolean)
    advanceTo7 = DB.Column(DB.Boolean)

    # Constructor for the object, expects a name and url
    def __init__(
        self,
        number=1234,
        name='MyTeam',
        affiliation="MyOrganizaton",
        round1=0,
        round2=0,
        round3=0,
        round4=0,
        round5=0,
        round6=0,
        round7=0,
        advanceTo4=False,
        advanceTo5=False,
        advanceTo6=False,
        advanceTo7=False
    ):
        """Construct a Team object using a name and URL."""
        self.number = self.fixInput(number)
        self.name = self.fixInput(name)
        self.affiliation = self.fixInput(affiliation)
        self.round1 = self.fixInput(round1)
        self.round2 = self.fixInput(round2)
        self.round3 = self.fixInput(round3)
        self.round4 = self.fixInput(round4)
        self.round5 = self.fixInput(round5)
        self.round6 = self.fixInput(round6)
        self.round7 = self.fixInput(round7)
        self.advanceTo4 = self.fixInput(advanceTo4)
        self.advanceTo5 = self.fixInput(advanceTo5)
        self.advanceTo6 = self.fixInput(advanceTo6)
        self.advanceTo7 = self.fixInput(advanceTo7)
        
    def getBestScore(self):
        return max(self.round1, self.round2, self.round3)
        
    def fixInput(self, data):
        """Convert unicode data to ASCII."""
        if isinstance(data, unicode):
            return data.encode('ascii', 'ignore')
        else:
            return data

    # Convert project to string
    def toString(self):
        """Generate a string representing the project."""
        return "%s: name=%s" % (self.number, self.name)

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


@APP.route('/')
def index():
    return render_template('index.html', title=APP.config['EVENT_NAME'])


@conditional(APP.route('/test'), APP.config['DEBUG'])
def test():
    return render_template('test.html')

if __name__ == '__main__':
    APP.run(host='0.0.0.0', debug=APP.config['DEBUG'])
