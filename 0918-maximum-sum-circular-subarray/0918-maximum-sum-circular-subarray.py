class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        tot_sum = sum(nums)
        current_min = 0  # min running sum
        current_max = 0
        tot_min = sys.maxsize  # min of all running sum
        tot_max = -sys.maxsize

        for n in nums:
            current_min = min(current_min + n, n)
            current_max = max(current_max + n, n)
            tot_min = min(tot_min, current_min)
            tot_max = max(tot_max, current_max)

        if tot_max <= 0:
            return tot_max
        return max(tot_max, tot_sum - tot_min)

    # O(n^2) but with DP, TLE ...
    """
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        def recSearch(i: int, j: int) -> int:
            nonlocal dp
            if dp[i][j] is not None:
                return dp[i][j]
            if j > i:
                sub_res = nums[j] + recSearch(i, j-1)
            else:
                sub_res = recSearch(i, n-1) + recSearch(0, j)
            dp[i][j] = sub_res
            return dp[i][j]
            
        res = -sys.maxsize
        for i in range(n):
            for j in range(n):
                res = max(res, recSearch(i, j))
        return res
    """

    # O(n^2), TLE ...
    """
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        circular = nums + nums[:-1]
        res = -sys.maxsize
        for k in range(1, n+1):
            sub_res = sum(circular[:k])
            res = max(res, sub_res)
            for j in range(k, 2*n - 1):
                sub_res -= circular[j-k]
                sub_res += circular[j]
                res = max(res, sub_res)
        return res
    """
