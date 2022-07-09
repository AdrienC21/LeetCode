class Solution:
    # not mine
    # use deq O(k) space complexity
    # O(n) time complexity
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        deq = deque([n-1])  # size at most k!
        for i in range(n-2, -1, -1):
            if (deq[0] - i) > k:
                deq.popleft()
            nums[i] += nums[deq[0]]
            while deq and (nums[deq[-1]] <= nums[i]):
                deq.pop()
            deq.append(i)
        return nums[0]
    # solution but time limit exceeded
    """
import sys
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [None for _ in range(n)]
        dp[-1] = nums[-1]
        def recSearch(i: int) -> int:
            nonlocal dp
            if not(dp[i] is None):
                return dp[i]
            max_score = -sys.maxsize
            for j in range(i + 1, min(i + k, n - 1) + 1):
                max_score = max(max_score, recSearch(j))
            max_score += nums[i]
            dp[i] = max_score
            return max_score
        return recSearch(0)
    """
