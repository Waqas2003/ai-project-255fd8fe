import unittest
from app import *

class TestApp(unittest.TestCase):
    def test_app(self):
        self.assertEqual("Hello, World!", "Hello, World!")

if __name__ == "__main__":
    unittest.main()