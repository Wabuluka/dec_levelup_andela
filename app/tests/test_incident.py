from app.tests.test_base import BaseTest
from .test_base import corruptioncasemodel
from app import app
import json

class TestOneRedFlag(BaseTest):
    

    def test_get_one_redflag(self):
        response = self.client.get('/api/v1/redflagrecords/1',)
        data =  json.loads(response.data)
        self.assertEqual(response.status_code, data)

    def test_all_redflags(self):
        
        response = self.client.get('/api/v1/redflagrecords')
        data =  json.loads(response.data)
        self.assertEqual(data,404)
        

    def test_create_incident(self):
        data = {
            "createdBy":"davieswabuluka",
            "caseType": "redflag",
            "location": "old kampasla",
            "status": "false",
            "comment": "too early to steal"
        }
        response = self.client.post('/api/v1/redflagrecords', content_type = 'application/json', data = json.dumps(data))
        self.assertEqual(response.status, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(data["status"], "draft")
        