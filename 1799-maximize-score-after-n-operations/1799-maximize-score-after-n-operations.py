import numpy as np


class Solution:
    # not mine, dp and bit manipulation
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = (1 << n) * [-1]

        def dfs(mask, t):
            if mask == (1 << n) - 1:
                return 0
            if dp[mask] != -1:
                return dp[mask]
            ma = 0
            for i in range(n):
                if (1 << i) & mask:
                    continue
                for j in range(i + 1, n):
                    if (1 << j) & mask:
                        continue
                    next = dfs(mask | (1 << i) | (1 << j), t + 1) + np.gcd(nums[i], nums[j]) * t
                    ma = max(next, ma)
            dp[mask] = ma
            return dp[mask]

        return dfs(0, 1)

    # Wrong answer on one particular example, we miss some cases with the approach below
    """
    def maxScore(self, nums: List[int]) -> int:
        two_n = len(nums)
        n = two_n // 2
        gcd_matrix = np.zeros((two_n, two_n), dtype=np.int32)
        for i in range(two_n - 1):
            for j in range(i + 1, two_n):
                gcd = np.gcd(nums[i], nums[j])
                gcd_matrix[i, j] = gcd
                gcd_matrix[j, i] = gcd
        res = 0
        for i in range(n, 0, -1):
            # find max gcd between two elements
            coord = np.unravel_index(gcd_matrix.argmax(), gcd_matrix.shape)
            # update score
            res += i * gcd_matrix[coord]
            # delete the corresponding row and column for the pair
            gcd_matrix = np.delete(gcd_matrix, list(coord), 0)
            gcd_matrix = np.delete(gcd_matrix, list(coord), 1)
        return res
    """
