from flask import url_for
import unittest
from main import app
from db_config import mysql

class TestBase(unittest.TestCase):

    def test_connectDB(self):
        # Defines the flask object's configuration for the unit tests
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
        app.config['MYSQL_DATABASE_DB'] = 'userdb'
        app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
        mysql.init_app(app)


class TestMain(unittest.TestCase):
    def test_users(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_new_users(self):
        tester = app.test_client(self)
        response = tester.get('/new_user')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_add_users(self):
        tester = app.test_client(self)
        data = {"inputName": "test" , "inputEmail": "test@test.com", "inputPassword": "password"}
        response = tester.post('/add',data=data)
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)    

    def test_add_users_nodata(self):
        tester = app.test_client(self)
        response = tester.post('/add')
        statuscode = response.status_code
        self.assertEqual(statuscode, 500) 

    def test_update_users(self):
        tester = app.test_client(self)
        data = {"id":"1","inputName": "test" , "inputEmail": "test@test.com", "inputPassword": "password"}
        response = tester.post('/update',data=data)
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)

    def test_update_users_nodata(self):
        tester = app.test_client(self)
        response = tester.post('/update')
        statuscode = response.status_code
        self.assertEqual(statuscode, 500)      

    def test_edit_users(self):
        tester = app.test_client(self)
        response = tester.get('/edit/1')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200) 

    def test_delete_users(self):
        tester = app.test_client(self)
        response = tester.get('/delete/1')
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)   
         
    def test_users_error(self):
        app.config['MYSQL_DATABASE_PASSWORD'] = 'password1'
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 500)

    def test_users_delete_error(self):
        app.config['MYSQL_DATABASE_PASSWORD'] = 'password1'
        tester = app.test_client(self)
        response = tester.get("/delete/1")
        statuscode = response.status_code
        self.assertEqual(statuscode, 500)  

    def test_users_edit_error(self):
        app.config['MYSQL_DATABASE_PASSWORD'] = 'password1'
        tester = app.test_client(self)
        response = tester.get("/edit/1")
        statuscode = response.status_code
        self.assertEqual(statuscode, 500)         

        

if __name__ == "__main__":
     unittest.main()
