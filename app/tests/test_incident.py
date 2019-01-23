from app.tests.test_base import BaseTest
from .test_base import corruptioncasemodel
from app import app
import json

class TestOneRedFlag(BaseTest):
    """
        tests whether a redflag can be created without authorixation
    """
    def test_create_redflag_incident(self):
        # token = self.get_user_token()
        data = {
            "createdBy": "w",
            "red_flag_title": "thieves in the allie",
            "caseType": "redflag",
            "location": 1232324,
            "status": "True",
            "comment": "too early to steal"
        }
        response = self.client.post('/api/v1/red-flags', content_type = 'application/json', data = json.dumps(data))
        self.assertEqual(response.status_code,401)