import unittest
import os
from app import app

class Test_app(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()                              # Define test instance

    # Ensure home page loads
    def test_index(self):              
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)

    # Ensure contact page loads
    def test_contact_page(self):
        rv = self.app.get('/contact')
        self.assertEqual(rv.status_code, 200)

    # Ensure project page loads
    def test_projects_page(self):
        rv = self.app.get('/projects')
        self.assertEqual(rv.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()