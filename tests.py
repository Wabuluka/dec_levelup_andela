import unittest
from run import RedFlagRecord, app
import json

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_create_red_flag(self):
        response = self.client.post('/api/v1/redflags/<int:id>')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()