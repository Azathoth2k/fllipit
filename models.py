from flask.ext.sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

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