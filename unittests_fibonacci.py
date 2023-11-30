import unittest


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        """Setting up  test. Set the instance of class Fibonacci"""
        self.fibonacci = Fibonacci()

    def tearDown(self):
        """Tearing down function not required for this test case"""
        pass

    def test_base_cases(self):
        self.assertEqual(self.fibonacci(0), 0)
        self.assertEqual(self.fibonacci(1), 1)

    def test_general_cases(self):
        self.assertEqual(self.fibonacci(2), 1)
        self.assertEqual(self.fibonacci(3), 2)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            self.fibonacci(-1)

    def test_sequence_correctness(self):
        for i in range(2, 10):
            self.assertEqual(
                self.fibonacci(i) + self.fibonacci(i + 1), self.fibonacci(i + 2)
            )

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci("0")
        with self.assertRaises(ValueError):
            self.fibonacci("1")
        with self.assertRaises(ValueError):
            self.fibonacci("abc")
        with self.assertRaises(ValueError):
            self.fibonacci("")
        with self.assertRaises(ValueError):
            self.fibonacci(None)

    def test_large_values(self):
        # Maximum recursion depth for our function equals to 490
        result = self.fibonacci(490)
        self.assertEqual(
            self.fibonacci(490),
            result,
        )

    def test_recursion_limit_exceeded(self):
        # RecursionError: maximum recursion depth for our function equals to 490
        with self.assertRaises(RecursionError):
            self.fibonacci(1000)


if __name__ == "__main__":
    unittest.main()
