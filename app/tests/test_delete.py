from app.tests.test_base import BaseTest
import json

"""
    Testing delete function
"""
class TestDelete(BaseTest):

    def test_delete_route(self):
        response = self.client.get('/api/v1/redflagrecord/1')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],404)