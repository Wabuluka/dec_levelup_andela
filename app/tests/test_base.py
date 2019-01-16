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

    def demo_data(self):
        create_incident = {
            "id": 1,
            "createdBy":"davieswabuluka",
            "red_flag_title": "thieves in the allie",
            "caseType": "redflag",
            "location": "old kampasla",
            "status": "false",
            "comment": "too early to steal"
        }
        return create_incident



if __name__ == '__main__':
    unittest.main()