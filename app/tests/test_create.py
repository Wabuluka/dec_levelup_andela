from app.tests.test_base import BaseTest
import json

"""
    Testing whether the get all url works
"""
class TestPostCase(BaseTest):

    def test_post_route(self):
        response = self.client.get('/api/v1/redflagrecords')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],404)