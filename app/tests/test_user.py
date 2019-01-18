from app.tests.test_base import json, BaseTest

class TestCreateNewUser(BaseTest):

    def test_create_user_url(self):
        user = {
            "userid" : 1,
            "firstname": "davies",
            "lastname": "wabuluka",
            "othernames": "me",
            "email":"me@me.com", 
            "username":"dme",
        }
        response = self.client.post('/api/v1/user', content_type = 'application/json', data = json.dumps(user))
        self.assertEqual(response.status_code,200)