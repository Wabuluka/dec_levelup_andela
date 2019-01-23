from app.tests.test_base import json, BaseTest

class TestCreateNewUser(BaseTest):
    pass
    # def test_create_user_url(self):
    #     new_user = {
    #         "firstname": "wabuluka",
    #         "lastname": "Davies",
    #         "othernames": "Geofrey",
    #         "email": "davieswabuluka@gmail.com",
    #         "phonenumber": "0701010101",
    #         "username": "webbie",
    #         "password": "webbie123"
    #     }
    #     request = self.app.post('/api/v2/auth/signup', content_type = 'application/json', data = json.dumps(new_user))
    #     response = json.loads(request.data.decode())
    #     self.assertIn('Created success', response['message'])
    #     self.assertEqual(request.status_code, 200)