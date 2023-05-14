class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        res = 0
        dp = [1] + high * [0]

        # complete list, nb string len i
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i-zero]) % mod
            if i >= one:
                dp[i] = (dp[i] + dp[i-one]) % mod
            # start increase result
            if i >= low:
                res = (res + dp[i]) % mod

        return res
