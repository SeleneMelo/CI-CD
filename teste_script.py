import unittest
from script import add_numbers, multiply_numbers

class TestProgram(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)

    def test_multiply_numbers(self):
        result = multiply_numbers(3, 5)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()
