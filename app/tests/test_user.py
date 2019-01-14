from app.tests.test_base import json, BaseTest

class TestCreateNewUser(BaseTest):

    def test_create_user_url(self):
        response = self.client.get('/api/v1/user')
        data =  json.loads(response.data)
        self.assertEqual(data["status"],404)