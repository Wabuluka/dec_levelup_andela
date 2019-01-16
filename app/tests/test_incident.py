from app.tests.test_base import BaseTest
import json

class TestOneRedFlag(BaseTest):

    def test_get_one_redflag(self):
        response = self.client.get('/api/v1/redflagrecords/1')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],404)

    def test_all_redflags(self):
        response = self.client.get('/api/v1/redflagrecords')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],404)

    def test_create_incident(self):
        new_incident = {
            "type": "intervention",
            "location": "one",
            "comment": "one",
            "createdBy": "one",
        }
        response = self.client.post('/api/v1/redflagrecord', data = json.dumps(new_incident))
        self.assertEqual(response.status_code, 201)