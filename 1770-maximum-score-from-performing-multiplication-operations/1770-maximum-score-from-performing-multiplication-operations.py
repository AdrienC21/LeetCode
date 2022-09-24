import sys
class Solution:
    # Again dynamic programming, but more optimized
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[0 for _ in range(m+1)] for _ in range(m+1)]
        score = -sys.maxsize
        for k in range(1, m+1):
            for l in range(k+1):
                if l == 0:
                    res_left = -sys.maxsize
                else:
                    res_left = dp[l-1][k-l] + multipliers[k-1] * nums[l-1]
                if l == k:
                    res_right = -sys.maxsize
                else:
                    res_right = dp[l][k-l-1] + multipliers[k-1] * nums[n-k+l]
                dp[l][k-l] = max(res_left, res_right)

                if k == m:
                    score = max(score, dp[l][k-l])
        return score
        
    # Time limit exceeded
    """
    import sys
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[[None for _ in range(n)] for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j][j] = multipliers[i] * nums[j]
        def recCalc(k: int, i: int, j: int) -> int:
            nonlocal dp, n
            if i > j:
                return -sys.maxsize
            if k == m:
                return 0
            if not(dp[k][i][j] is None):
                return dp[k][i][j]
            res_left = recCalc(k+1, i+1, j)
            res_right = recCalc(k+1, i, j-1)
            res = max(multipliers[k] * nums[i] + res_left,
                      multipliers[k] * nums[j] + res_right)
            dp[k][i][j] = res
            return res
        return recCalc(0, 0, n-1)
    """
