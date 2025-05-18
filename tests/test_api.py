import unittest

import sys
sys.path.append('backend')
from main import app, read_message, get_time

class APITestCase(unittest.TestCase):
    def test_read_message(self):
        data = read_message()
        self.assertIn('message', data)

    def test_get_time(self):
        data = get_time()
        self.assertIn('time', data)


if __name__ == '__main__':
    unittest.main()
