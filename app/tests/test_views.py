import unittest
import json
from app.model.intervention import DatabaseConnection

from run import app


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app = app.test_client()
        db = DatabaseConnection()
        db.create_tables()

    def tearDown(self):
        with self.app as app:
            db = DatabaseConnection()
            db.drop_tables()

    def create_record(self,casetype, createdby, title, location, comment, status):
        post_data = self.app.post(
            '/api/v2/red-flags',
            data=json.dumps(dict(
                casetype=casetype,
                comment=comment,
                createdby=createdby,
                title=title,
                location=location,
                status=status
            )),
            content_type='application/json'
        )
        return post_data

    def test_add_redflag(self):
        post = self.create_record('redflag','bill','opm-office','workers house','pension','pending')
        response = json.loads(post.data.decode())
        self.assertIn(response['message'], 'Created success')
        self.assertEqual(post.status_code, 201)


    def test_get_all_redflags(self):
        post = self.create_record('redflag','bill','opm-office','workers house','pension','pending')
        
        request_data = self.app.get('/api/v2/red-flags')
        response_data = json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code, 200)
        self.assertIn(response_data['message'], 'success')
        self.assertTrue(response_data['status'], 200)
        self.assertTrue(response_data['data'])

    def test_get_all_redflags_not_existing(self):
        request_data = self.app.get('/api/v2/red-flags')
        response_data = json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code, 200)
        self.assertIn(response_data['message'], 'there are no redflags')
       
    def test_get_specific_redflags(self):
        post = self.create_record('redflag','bill','opm-office','workers house','pension','pending')
        
        request_data = self.app.get('/api/v2/red-flags/1')
        response_data = json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code, 200)
        self.assertIn(response_data['message'], 'success')
        self.assertTrue(response_data['status'], 200)
        self.assertTrue(response_data['data'])

    
    def test_get_specific_redflags_not_existing(self):
        post = self.create_record('redflag','bill','opm-office','workers house','pension','pending')
        
        request_data = self.app.get('/api/v2/red-flags/100')
        response_data = json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code, 404)
        self.assertIn(response_data['message'], 'first post redflags')

    def test_delete_redflag(self):
        post = self.create_record('redflag','bill','opm-office','workers house','pension','pending')

        request_data = self.app.delete('/api/v2/red-flags/1')
        response_data = json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code, 200)
        self.assertIn(response_data['message'], 'Deleted')

    # def test_edit_comment_not_existing(self):
    #     post = self.create_record('redflag','bill','opm-office','workers house','pension','pending')

    #     request_data = self.app.patch('/api/v2/red-flags/100/comment')
    #     response_data = json.loads(request_data.data.decode())
        # self.assertEqual(request_data.status_code, 200)
        # self.assertIn(response_data['message'], 'Deleted')


    
    # def test_edit_comment(self):
    #     post = self.create_record('redflag','bill','opm-office','workers house','pension','pending')

    #     request_data = self.app.patch('/api/v2/red-flags/1/comment')
    #     response_data = json.loads(request_data.data.decode())
    #     self.assertEqual(request_data.status_code, 200)
    #     self.assertIn(response_data['message'], 'Deleted')
    def create_intervention(self,casetype, createdby, title, location, comment, status):
        post_data = self.app.post(
            '/api/v2/interventions',
            data=json.dumps(dict(
                casetype=casetype,
                comment=comment,
                createdby=createdby,
                title=title,
                location=location,
                status=status
            )),
            content_type='application/json'
        )
        return post_data


    def test_add_intervention(self):
        post = self.create_intervention('redflag','bill','opm-office','workers house','pension','pending')
        response = json.loads(post.data.decode())
        self.assertIn(response['message'], 'Created success')
        self.assertEqual(post.status_code, 200)        

    def test_get_all_interventions(self):
        post = self.create_intervention('redflag','bill','opm-office','workers house','pension','pending')
        
        request_data = self.app.get('/api/v2/interventions')
        response_data = json.loads(request_data.data.decode())
        # self.assertEqual(request_data.status_code, 200)
        self.assertIn(response_data['message'], 'success')
        self.assertTrue(response_data['status'], 200)
        self.assertTrue(response_data['data'])
        
    def test_get_specific_intervention(self):
        post = self.create_intervention('redflag','bill','opm-office','workers house','pension','pending')
        
        request_data = self.app.get('/api/v2/interventions/1')
        response_data = json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code, 200)
        self.assertIn(response_data['message'], 'success')
        self.assertTrue(response_data['status'], 200)
        self.assertTrue(response_data['data'])

    def test_get_all_interventions_not_existing(self):
        request_data = self.app.get('/api/v2/interventions')
        response_data = json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code, 404)
        self.assertIn(response_data['message'], 'there are no interventions')

    def create_user(self,firstname,lastname,othernames,email,phonenumber,registeredOn,username,isAdmin,location,password,status):
        post_data = self.app.post(
            '/api/v2/auth/signup',
            data=json.dumps(dict(
                firstname= firstname,
                lastname=lastname,
                othernames=othernames,
                email = email,
                phonenumber = phonenumber,
                registeredOn = registeredOn,
                username = username,
                isAdmin = isAdmin,
                location=location,
                password = password,
                status=status
            )),
            content_type='application/json'
        )
        return post_data

    def test_signup(self):
        post = self.create_user('redflag','bill','opm-office','workers house', 1213232424,'pending','dsdvdfdsfsd','sdfdfdfd','sddfdfdfd','ddsdsdd','sdssds')
        response = json.loads(post.data.decode())
        self.assertIn(response['message'], 'Created success')
        self.assertEqual(post.status_code, 200)