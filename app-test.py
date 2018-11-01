"""Backend unit testing for the FLL Pit Display."""

from fllipit import APP, Team
from coverage import coverage

import unittest
import os


class BasicTestCase(unittest.TestCase):

    """Basic test case."""

    def test_index(self):
        """Verfy that the index page is present."""
        tester = APP.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_api(self):
        """Verify that the API endpoint is present."""
        tester = APP.test_client(self)
        response = tester.get('/api/teams', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    def test_bestScore(self):
        
        # Three scores entered
        team1 = Team(round1=350, round2=440, round3=500, round4=410, round5=120)
        team2 = Team(round1=350, round2=440, round3=120, round4=410, round5=120)
        team3 = Team(round1=350, round2=298, round3=305, round4=325, round5=120)
        
        self.assertEqual(500, team1.bestScore)
        self.assertEqual(440, team1.secondBestScore)
        self.assertEqual(350, team1.worstScore)

        self.assertEqual(440, team2.bestScore)
        self.assertEqual(350, team2.secondBestScore)
        self.assertEqual(120, team2.worstScore)

        self.assertEqual(350, team3.bestScore)
        self.assertEqual(305, team3.secondBestScore)
        self.assertEqual(298, team3.worstScore)
        
    def test_bestScore_incomplete(self):
        """Verify that the code can determine the best score for a team when not all 3 scores are entered"""
        
        # No scores entered yet
        team0 = Team()
        
        # One score entered
        team1 = Team(round1=350)
        
        # Two scores entered
        team2 = Team(round1=350, round2=440)
        team3 = Team(round1=350, round2=120)
        
        self.assertEqual(0, team0.bestScore)
        self.assertEqual(0, team0.secondBestScore)
        self.assertEqual(0, team0.worstScore)
        
        self.assertEqual(350, team1.bestScore)
        self.assertEqual(0, team1.secondBestScore)
        self.assertEqual(0, team1.worstScore)
        
        self.assertEqual(440, team2.bestScore)
        self.assertEqual(350, team2.secondBestScore)
        self.assertEqual(0, team2.worstScore)
        
        self.assertEqual(350, team3.bestScore)
        self.assertEqual(120, team3.secondBestScore)
        self.assertEqual(0, team3.worstScore)

if __name__ == '__main__':
    unittest.main()