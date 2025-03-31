import unittest
import json
from src.app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome", response.get_json()["message"])

    def test_add(self):
        response = self.client.post("/add", 
            data=json.dumps({"a": 2, "b": 3}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"], 5)

if __name__ == "__main__":
    unittest.main()