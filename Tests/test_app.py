import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertIn(b'Hello, this is the homepage', response.data)

    def test_valid_stats(self):
        response = self.client.get('/stats/US/2020-03-01/2021-03-10')
        self.assertIn(b'COVID-19 stats for US', response.data)
if __name__ == '__main__':
    unittest.main()
