class Solution:
    # O(1) space, O(n) time
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        size = (n * (n + 1)) // 2
        return int(size - sum(nums))
    # bad, nlog n
    """
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, n in enumerate(nums):
            if i != n:
                return i
        return n+1
    """