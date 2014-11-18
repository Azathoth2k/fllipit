"""This module is the main Flask web application for the FLL Pit Display."""

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful
from flask.ext.restful import Resource, Api, fields, marshal_with
from flask.ext.conditional import conditional
import urllib2
import json

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
        self.number = number
        self.name = name
        self.affiliation = affiliation
        self.round1 = round1
        self.round2 = round2
        self.round3 = round3
        self.round4 = round4
        self.round5 = round5
        self.round6 = round6
        self.round7 = round7
        self.advanceTo4 = advanceTo4
        self.advanceTo5 = advanceTo5
        self.advanceTo6 = advanceTo6
        self.advanceTo7 = advanceTo7

    # Convert project to string
    def toString(self):
        """Generate a string representing the project."""
        return "%s: name=%s" % (self.number, self.name)

teamFields = {
    "number": fields.Integer,
    "name": fields.String,
    "affiliation": fields.String,
    "round0": fields.Integer,
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
}


class TeamList(Resource):

    """Setup a REST resource for the Jenkins project/ build data."""

    @marshal_with(teamFields)
    def get(self):
        teams = Team.query.all()
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
