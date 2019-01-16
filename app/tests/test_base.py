import unittest
from app import app
from app.models.corrupt_model import CorruptionCase
from app.models.usr_model import UserModel
import json

corruptioncasemodel = CorruptionCase()
usermodel = UserModel()
"""
    Setting up the testing class to be used throughout the testing modules
"""
class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()


if __name__ == '__main__':
    unittest.main()