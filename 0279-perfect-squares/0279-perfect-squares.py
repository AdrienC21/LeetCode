from math import sqrt
class Solution:
    def __init__(self):
        self.num_squares = {i**2: 1 for i in range(1, 101)}
    def numSquares(self, n: int) -> int:
        if n in self.num_squares:
            return self.num_squares[n]
        s = int(sqrt(n))
        minimum = sys.maxsize
        for k in range(s, s//2, -1):
            minimum = min(minimum, self.numSquares(n - k ** 2) + 1)
        self.num_squares[n] = minimum
        return minimum
