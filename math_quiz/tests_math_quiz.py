import unittest
from math_quiz import random_integer, random_sign, calculation


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        for _ in range(1000):  # Test a large number of random values
            rand_sign = random_sign()
            self.assertTrue(rand_sign in ['+', '-', '*'])

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (13, -2, '+', '13 + -2', 11),
                (-5, -3, '+', '-5 + -3', -8),
                (5, 2, '-', '5 - 2', 3),
                (10, -7, '-', '10 - -7', 17),
                (5, 2, '*', '5 * 2', 10),
                (5, -4, '*', '5 * -4', -20),
                (-5, -3, '*', '-5 * -3', 15),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculation(num1, num2, operator)
                self.assertEqual(problem, expected_problem) and self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
