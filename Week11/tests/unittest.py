import unittest

def add(x, y):
    return x + y
def mul(x, y):
    return x * y

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_mul(self):
        self.assertEqual(mul(1, 2), 2)
        self.assertEqual(mul(2, 2), 4)



if __name__ == '__main__':
    unittest.main()
