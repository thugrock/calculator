import unittest
from app import app
import logging
from logging.config import dictConfig
FORMAT ='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
#app.logger.basicConfig(filename='test.log', level=logging.ERROR, format=FORMAT)

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_square_root(self):
        response = self.client.post('/sqrt', data=dict(number=4))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Square Root', response.data)
        self.assertIn(b'Result: 2.0', response.data)
        app.logger.critical("number is 4, operation is square root, result is 2.0")

    def test_natural_logarithm(self):
        response = self.client.post('/ln', data=dict(number=1))
        org = response
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Natural Logarithm', response.data)
        self.assertIn(b'Result: 0.0', response.data)
        app.logger.critical("number is 1, operation is natural logarithm, result is 0.0")

    def test_power(self):
        response = self.client.post('/pow', data=dict(number=2, exponent=3))
        org = response
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Power', response.data)
        self.assertIn(b'Result: 8.0', response.data)
        app.logger.critical("number is 2, exponent is 3, operation is power, result is 8.0")

    def test_factorial(self):
        response = self.client.post('/fact', data=dict(number=5))
        org = response
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Factorial', response.data)
        self.assertIn(b'Result: 120', response.data)
        app.logger.critical("number is 5, operation is factorial, result is 120")
'''
    def test_not_square_root(self):
        response = self.client.post('/sqrt', data=dict(number=4))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Result: 3.0', response.data)
        app.logger.critical("number is 4, operation is square root, result is 2.0")

    def test_not_natural_logarithm(self):
        response = self.client.post('/ln', data=dict(number=1))
        self.assertNotEqual(response.status_code, 404)
        self.assertNotIn(b'Result: 1.0', response.data)
        app.logger.critical("number is 1, operation is natural logarithm, result is 0.0")

    def test_not_power(self):
        response = self.client.post('/pow', data=dict(number=2, exponent=3))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Result: 7.0', response.data)
        app.logger.critical("number is 2, exponent is 3, operation is power, result is 8.0")

    def test_not_factorial(self):
        response = self.client.post('/fact', data=dict(number=5))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Result: 130', response.data)
        app.logger.critical("number is 5, operation is factorial, result is 120")
'''

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": '%(asctime)s "%(name)s" %(levelname)s "%(funcName)s" "%(lineno)d" "%(message)s"'
,
            }
        },
        "handlers": {
            "file": {
                "class": "logging.FileHandler",
                "filename": "logs/test.log",
                "formatter": "default",
            },
        },
        "root": {"level": "CRITICAL", "handlers": ["file"]},
    }
)
if __name__ == '__main__':
        # Create a file handler for the test log file
    log = logging.getLogger('werkzeug')
    # Run the tests
    log.setLevel(logging.CRITICAL)
    unittest.main()
