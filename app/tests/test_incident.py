from app.tests.test_base import BaseTest
from .test_base import corruptioncasemodel
from app import app
import json

class TestOneRedFlag(BaseTest):

    def test_create_incident(self):
        data = {
            "createdBy":"davieswabuluka",
            "caseType": "redflag",
            "location": "old kampasla",
            "status": "false",
            "comment": "too early to steal"
        }
        response = self.client.post('/api/v1/redflagrecords', content_type = 'application/json', data = json.dumps(data))
        # data =  json.loads(response.data)
        self.assertEqual(response.status_code,200)

    def test_get_one_redflag(self):
        data = {
            "createdBy":"davieswabuluka",
            "caseType": "redflag",
            "location": "old kampasla",
            "status": "false",
            "comment": "too early to steal"
        }
        self.client.post('/api/v1/redflagrecords', content_type = 'application/json', data = json.dumps(data))
        response_del = self.client.get('/api/v1/redflagrecords/1')
        data =  json.loads(response_del.data)
        self.assertEqual(response_del.status_code, 200)

    def test_delete_one_redflag(self):
        data = {
            "createdBy":"davieswabuluka",
            "caseType": "redflag",
            "location": "old kampasla",
            "status": "false",
            "comment": "too early to steal"
        }
        response = self.client.post('/api/v1/redflagrecords', content_type = 'application/json', data = json.dumps(data))
        response = self.client.delete('/api/v1/redflagrecords/1')
        data =  json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_all_redflags(self):
        
        response = self.client.get('/api/v1/redflagrecords')
        # data =  json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        

    