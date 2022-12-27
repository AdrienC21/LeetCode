class Solution:
    # TRICK: we don't need to store all indexes, we can start from the end and store the position i such that from i (or above) we can reach the end
    # O(n) time, O(1) space
    def canJump(self, nums: List[int]) -> bool:
        to_reach = len(nums) - 1  # init at last index
        for i in range(len(nums)-1, -1, -1):
            if (i + nums[i]) >= to_reach:
                to_reach = i
        return (to_reach == 0)

    # TLE again
    """
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            for k in range(min(nums[i], n-i-1), 0, -1):
                dp[i] = dp[i] or dp[i+k]
                if dp[i]:
                    break
        return dp[0]
    """

    # TLE
    """
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [None for _ in range(n)]
        dp[n-1] = True

        def recSearch(i: int) -> bool:
            nonlocal dp
            if dp[i] is not None:
                return dp[i]
            sent = False
            for k in range(1, nums[i]+1):
                sent = sent or recSearch(i+k)
                if sent:
                    break
            dp[i] = sent
            return sent

        return recSearch(0)
    """
