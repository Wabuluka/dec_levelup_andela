from app.tests.test_base import BaseTest
import json

class TestOneRedFlag(BaseTest):

    def test_get_one_redflag(self):
        response = self.client.get('/api/v1/redflagrecord/1')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],404)

    def test_all_redflags(self):
        response = self.client.get('/api/v1/redflagrecords')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],404)