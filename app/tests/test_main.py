import unittest

from app import main

class TestBase(unittest.TestCase):
    def setUp(self):
        self.app = main

    def tearDown(self):
        del self.app

    def test_config(self):
        self.app.MIN = 0
        self.app.MAX = 100
        assert self.app.get_min_and_max() == (0, 100)

    def test_api(self):
        self.app.mystery_num = 25
        assert self.app.api(50) == 'Lower!'
        self.app.mystery_num = 75
        assert self.app.api(50) == 'Higher!'
        self.app.mystery_num = 50
        assert self.app.api(50) == 'Yeah! You guessed right!'


if __name__ == '__main__':
    unittest.main()
