import unittest
from main import add


class TestMain(unittest.TestCase):
    def test_add(self):
        num1 = 9
        num2 = 5
        res = add(num1, num2)
        self.assertEqual(res, 14)


if __name__=="__main__":
    unittest.main()