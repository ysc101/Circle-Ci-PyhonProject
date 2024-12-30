import unittest
from hello import say_hello

class TestHelloWorld(unittest.TestCase):
    def test_say_hello(self):
        """Test if say_hello returns 'Hello, World!'."""
        self.assertEqual(say_hello(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
