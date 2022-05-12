from math import sqrt
class Solution:
    # implicit formula
    def fib(self, n: int) -> int:
        phi = (1 + sqrt(5)) / 2
        return round(pow(phi, n) / sqrt(5))
    """
    # dynamic programming and recursion
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [-1 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        def recFibo(k: int) -> int:
            if dp[k] != -1:
                return dp[k]
            res = recFibo(k-1) + recFibo(k-2)
            dp[k] = res
            return res
        return recFibo(n)
    """