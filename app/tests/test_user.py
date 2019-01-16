from app.tests.test_base import json, BaseTest

class TestCreateNewUser(BaseTest):

    def test_create_user_url(self):
        user = {
            "userid" : 1,
            "firstname": "davies",
            "lastname": "wabuluka",
            "othernames": "me",
            "email":"me@me.com", 
            # "phoneNumber":123433, 
            "username":"dme",
            # "registeredOn":"123223",
            # "isAdmin":True
        }
        response = self.client.post('/api/v1/user', content_type = 'application/json', data = json.dumps(user))
        # data =  json.loads.decode()(response.data)
        self.assertEqual(response.status_code,200)