# Question: https://neetcode.io/problems/gradient-descent

"""
    Very straightforward question, basic ML 101
"""

class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # The derivative of this function is 2 * x
        guess = init
        for _ in range(iterations):
            derivative = 2 * guess

            guess = guess - learning_rate * derivative

        return round(guess, 5)
