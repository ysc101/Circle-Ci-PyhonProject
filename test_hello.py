import unittest
from main import say_hello

class TestYogeshName(unittest.TestCase):
    def test_say_hello(self):
        """Test if say_hello returns 'Hello, YOGESH!'."""
        self.assertEqual(say_hello(), "Hello, YOGESH!")

if __name__ == "__main__":
    unittest.main()
