class Solution:
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