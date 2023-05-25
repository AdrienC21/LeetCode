class Solution:
    # Dynamic Programming
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if not(k) or (n >= k - 1 + maxPts):
            return 1.0

        res = 0.
        dp = [0. for _ in range(n+1)]
        dp[0] = 1.0  # prob to arrive at point i
        running_sum = dp[0]  # sum proba from i-maxPts to i-1

        for i in range(1, n+1):
            # P(i) = (P(i - 1)+P(i - 2)+...+P(i - maxPts)) / maxPts
            dp[i] = running_sum / maxPts
            if i < k:
                running_sum += dp[i]
            else:  # stop game
                res += dp[i]
            if (i - maxPts) >= 0:
                running_sum -= dp[i-maxPts]
        return res
