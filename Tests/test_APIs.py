import unittest
from main import app
from flask import json

class TestGreetingsAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_greetings_v1(self):
        response = self.app.post('/greetings/v1', query_string={'format': 'JSON', 'db': 'mysql', 'date': '2022-08-08'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        print(data)
        # Add more assertions here based on the expected response

    def test_greetings_v2(self):
        response = self.app.post('/greetings/v2', query_string={'format': 'JSON', 'db': 'mongo', 'date': '2022-08-08'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        print(data)
        # Add more assertions here based on the expected response
    def test_greetings_v3(self):
        response = self.app.post('/greetings/v3', query_string={'format': 'JSON', 'db': 'memory', 'date': '2022-08-08', 'picture_path': '/path/to/picture'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        print(data)
        # Add more assertions here based on the expected response

    def test_greetings_v4(self):
        response = self.app.post('/greetings/v4', query_string={
            'format': 'XML', 
            'db': 'memory', 
            'date': '2022-08-08', 
            'discount_for_male': 10, 
            'items_for_male': ['item1', 'item2'], 
            'discount_for_female': 20, 
            'items_for_female': ['item3', 'item4']
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        print(data)
        # Add more assertions here based on the expected response

if __name__ == '__main__':
    unittest.main()