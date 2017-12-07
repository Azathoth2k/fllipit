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
    round1Penalties = DB.Column(DB.Integer)
    round2Penalties = DB.Column(DB.Integer)
    round3Penalties = DB.Column(DB.Integer)
    round4Penalties = DB.Column(DB.Integer)
    round5Penalties = DB.Column(DB.Integer)
    round6Penalties = DB.Column(DB.Integer)
    round7Penalties = DB.Column(DB.Integer)

    # Constructor for the object
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
        advanceTo7=False,
        round1Penalties=0,
        round2Penalties=0,
        round3Penalties=0,
        round4Penalties=0,
        round5Penalties=0,
        round6Penalties=0,
        round7Penalties=0
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
        self.round1Penalties = self.fixInput(round1Penalties)
        self.round2Penalties = self.fixInput(round2Penalties)
        self.round3Penalties = self.fixInput(round3Penalties)
        self.round4Penalties = self.fixInput(round4Penalties)
        self.round5Penalties = self.fixInput(round5Penalties)
        self.round6Penalties = self.fixInput(round6Penalties)
        self.round7Penalties = self.fixInput(round7Penalties)
        self.sortScores()

    class Score:
        def __init__(self, round=1, score=0, penalties=0):
            self.round = round
            self.score = Team.default_to_zero(score)
            self.penalties = Team.default_to_zero(penalties)

    def sortScores(self):
        scores = [self.Score(1, self.round1, self.round1Penalties),
                  self.Score(2, self.round2, self.round2Penalties),
                  self.Score(3, self.round3, self.round3Penalties)]
        sorted_scores = sorted(
            scores,
            key=lambda x: (x.score, -x.penalties),
            reverse=True)

        self.bestScore = sorted_scores[0].score
        self.bestScorePenalties = sorted_scores[0].penalties

        self.secondBestScore = sorted_scores[1].score
        self.secondBestScorePenalties = sorted_scores[1].penalties

        self.worstScore = sorted_scores[2].score
        self.worstScorePenalties = sorted_scores[2].penalties
        
    def getRoundScore(self, roundNumber):
        scores = [self.round1, self.round2, self.round3, self.round4, self.round5, self.round6, self.round7]
        return scores[roundNumber-1]

    def getRoundPenalties(self, roundNumber):
        penalties = [
            self.round1Penalties,
            self.round2Penalties,
            self.round3Penalties,
            self.round4Penalties,
            self.round5Penalties,
            self.round6Penalties,
            self.round7Penalties]

        return self.default_to_zero(penalties[roundNumber-1])
    
    def isAdvancingToRound(self, roundNumber):
        advances = [self.advanceTo4, self.advanceTo5, self.advanceTo6, self.advanceTo7]
        return advances[roundNumber-4]
        
    def fixInput(self, data):
        """Convert unicode data to ASCII."""
        if isinstance(data, unicode):
            return data.encode('ascii', 'ignore')
        else:
            return data

    @staticmethod
    def default_to_zero(number):
        if number is None:
            return 0
        else:
            return number
        
    def toString(self):
        """Generate a string representing the project."""
        return "%s: name=%s" % (self.number, self.name)
    