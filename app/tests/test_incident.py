from app.tests.test_base import BaseTest
from .test_base import corruptioncasemodel
from app import app
import json

class TestOneRedFlag(BaseTest):
    # def test_create_redflag_incident(self):
    #     data = {
    #         "createdBy": "w",
    #         "red_flag_title": "thieves in the allie",
    #         "caseType": "redflag",
    #         "location": 1232324,
    #         "status": "True",
    #         "comment": "too early to steal"
    #     }
    #     response = self.client.post('/api/v2/red-flags', content_type = 'application/json', data = json.dumps(data))
    #     self.assertEqual(response.status_code,200)

    # def test_create_wrong_incident(self):
    #     data = {
    #         "createdBy": "w",
    #         "red_flag_title": "thieves in the allie",
    #         "caseType": "redflag",
    #         "location": 1232324,
    #         "status": "True",
    #         "comment": "too early to steal"
    #     }
    #     response = self.client.post('/api/v1/redflagrecord', content_type = 'application/json', data = json.dumps(data))
    #     self.assertEqual(response.status_code,404)


    # def test_get_one_redflag(self):
    #     data = {
    #         "createdBy":"davieswabuluka",
    #         "caseType": "redflag",
    #         "location": "old kampasla",
    #         "status": "false",
    #         "comment": "too early to steal"
    #     }
    #     create = self.client.post('/api/v2/red-flags', content_type = 'application/json', data = json.dumps(data))
    #     self.assertEqual(create.status_code,200)
    #     response = self.client.get('/api/v2/red-flags/2')
    #     data =  json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)


    # def test_all_redflags(self):
    #     data = {
    #         "createdBy":"davieswabuluka",
    #         "caseType": "redflag",
    #         "location": "old kampasla",
    #         "status": "false",
    #         "comment": "too early to steal"
    #     }
    #     create = self.client.post('/api/v2/red-flags', content_type = 'application/json', data = json.dumps(data))
    #     self.assertEqual(create.status_code,200)
    #     response = self.client.get('/api/v2/red-flags')
    #     data =  json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)
        


    # def test_delete_one_redflag(self):
    #     data = {
    #         "createdBy":"davieswabuluka",
    #         "caseType": "redflag",
    #         "location": "old kampasla",
    #         "status": "false",
    #         "comment": "too early to steal"
    #     }
    #     create = self.client.post('/api/v2/red-flags', content_type = 'application/json', data = json.dumps(data))
    #     self.assertEqual(create.status_code,200)
    #     response = self.client.delete('/api/v2/red-flags/1')
    #     data =  json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)
        

    # def test_edit_comment(self):
    #     data = {
    #         "createdBy":"davieswabuluka",
    #         "caseType": "redflag",
    #         "location": "old kampasla",
    #         "status": "false",
    #         "comment": "too early to steal"
    #     }
    #     create = self.client.post('/api/v2/red-flags', content_type = 'application/json', data = json.dumps(data))
    #     self.assertEqual(create.status_code,200)
    #     response = self.client.get('/api/v2/red-flags')
    #     data =  json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)
    #     response = self.client.put('/api/v2/red-flags/1/edit-comment')
    #     self.assertEqual(response.status_code, 200)


    # def test_edit_location(self):
    #     data = {
    #         "createdBy":"davieswabuluka",
    #         "caseType": "redflag",
    #         "location": "old kampasla",
    #         "status": "false",
    #         "comment": "too early to steal"
    #     }
    #     create = self.client.post('/api/v2/red-flags', content_type = 'application/json', data = json.dumps(data))
    #     self.assertEqual(create.status_code,200)
    #     response = self.client.get('/api/v2/red-flags')
    #     data =  json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)
    #     response = self.client.put('/api/v2/red-flags/1/location')
    #     self.assertEqual(response.status_code, 200)
    
        

    pass