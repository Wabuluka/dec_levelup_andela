import unittest
from app import app
from app.models.corrupt_model import CorruptionCase
from app.models.usr_model import UserModel
from app.models.db_conn import DatabaseConnection
import json
"""
export FLASK_ENV=TESTING
echo $FLASK_ENV
"""


corruptioncasemodel = CorruptionCase()
usermodel = UserModel()
"""
    Setting up the testing class to be used throughout the testing modules
"""
class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        db = DatabaseConnection()
        # db.create_tables()

        
    # def tearDown(self):
    #     with self.app as app:
    #         cursor = DatabaseConnection()
    #         cursor.drop_tables()
    


if __name__ == '__main__':
    unittest.main()