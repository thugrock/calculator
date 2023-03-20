import unittest
from app import app
import xmlrunner

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_square_root(self):
        response = self.client.post('/sqrt', data=dict(number=4))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Square Root', response.data)
        self.assertIn(b'Result: 2.0', response.data)

    def test_natural_logarithm(self):
        response = self.client.post('/ln', data=dict(number=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Natural Logarithm', response.data)
        self.assertIn(b'Result: 0.0', response.data)

    def test_power(self):
        response = self.client.post('/pow', data=dict(number=2, exponent=3))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Power', response.data)
        self.assertIn(b'Result: 8.0', response.data)

    def test_factorial(self):
        response = self.client.post('/fact', data=dict(number=5))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Factorial', response.data)
        self.assertIn(b'Result: 120', response.data)

if __name__ == '__main__':
        # Create a file handler for the test log file
    # Run the tests
    runner = xmlrunner.XMLTestRunner(output='./test-reports')
    unittest.main(testRunner=runner)
