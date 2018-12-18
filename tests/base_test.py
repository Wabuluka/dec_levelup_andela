import unittest
from app import app
import json

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

if __name__ == '__main__':
    unittest.main()