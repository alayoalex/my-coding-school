import unittest

def fun(x):
    return x + 10


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 13)

if __name__ == "__main__":
    unittest.main()