"""Unit tests for the Flask COVID-19 app."""

import unittest
from app import app


class TestApp(unittest.TestCase):
    """Unit tests for the Flask app."""

    def setUp(self):
        """Create a test client."""
        self.client = app.test_client()

    def test_homepage(self):
        """Test if the homepage loads correctly."""
        response = self.client.get('/')
        self.assertIn(b'Hello, this is the homepage', response.data)

    def test_valid_stats(self):
        """Test if valid country stats load correctly."""
        response = self.client.get('/stats/US/2020-03-01/2021-03-10')
        self.assertIn(b'COVID-19 stats for US', response.data)

if __name__ == '__main__':
    unittest.main()
