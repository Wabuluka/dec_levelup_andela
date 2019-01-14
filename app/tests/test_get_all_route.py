from app.tests.test_base import BaseTest
import json

"""
    Testing whether the get all url works
"""
class TestGetAllRoutes(BaseTest):

    def test_get_all_routes(self):
        response = self.client.get('/api/v1/redflagrecords')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],404)