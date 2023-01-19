class Solution:
    # Trick:
    # if sum(nums[:i]) % k == x and sum(nums[:j]) % k == x,
    # then sum(nums[i:j]) % k == 0
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        running_sum_mod = 0
        count = [1] + (k - 1) * [0]  # count the running sums per modulo

        for n in nums:
            running_sum_mod = (running_sum_mod + n) % k
            res += count[running_sum_mod]
            count[running_sum_mod] += 1

        return res

    # TLE
    """
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i] % k
        
        def recSearch(i: int, j: int) -> int:
            nonlocal dp
            if dp[i][j] is not None:
                return dp[i][j]
            if i == 0:
                dp[i][j] = recSearch(i, j-1) + nums[j]
            else:
                dp[i][j] = recSearch(i-1, j) - nums[i-1]
            dp[i][j] %= k
            return dp[i][j]

        res = 0
        for i in range(n):
            for j in range(i, n):
                if recSearch(i, j) == 0:
                    res += 1
        return res
    """
