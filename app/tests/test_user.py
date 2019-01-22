from app.tests.test_base import json, BaseTest

class TestCreateNewUser(BaseTest):

    def test_create_user_url(self):
    #     user = {
    #         "firstname": "davies",
    #         "lastname": "wabuluka",
    #         "othernames": "me",
    #         "email":"me@me.com", 
    #         "username":"dme",
    #     }
    #     response = self.client.post('/api/v2/auth/signup', content_type = 'application/json', data = json.dumps(user))
    #     self.assertEqual(response.status_code,200)

        signup = dict(username="greate_guy", firstname="wabuluka", lastname="wabuluka", email="mememe@gmail.com", password="joel1234", othernames="webbie")
        request = self.app.post('/api/v2/auth/signup', json=signup)
        response = json.loads(request.data.decode())
        self.assertIn('user signed up successfully', response['message'])
        self.assertEqual(request.status_code, 201)