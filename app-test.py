"""Backend unit testing for the FLL Pit Display."""

from fllipit import APP
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

if __name__ == '__main__':
    unittest.main()