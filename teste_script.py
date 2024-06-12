import unittest
from script import fibonacci

class TestProgram(unittest.TestCase):
    def test_fibonacci_zero(self):
        result = fibonacci(0)
        self.assertEqual(result, [])

    def test_fibonacci_one(self):
        result = fibonacci(1)
        self.assertEqual(result, [0])

    def test_fibonacci_two(self):
        result = fibonacci(2)
        self.assertEqual(result, [0, 1])

    def test_fibonacci_positive(self):
        result = fibonacci(6)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5])

    def test_fibonacci_negative(self):
        # Teste para garantir que a função lida bem com entradas negativas
        result = fibonacci(-3)
        self.assertEqual(result, [])

    def test_fibonacci_large_input(self):
        # Teste para garantir que a função lida bem com entradas grandes
        result = fibonacci(15)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])

    def test_fibonacci_prime_input(self):
    	# Teste para garantir que a função lida bem com um número primo
    	result = fibonacci(13)
    	self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])

if __name__ == '__main__':
    unittest.main()
