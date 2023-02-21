class Solution:
    # for O(log(n)), exploit the fact that the list is not even anymore with the single integer
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            m = i + (j - i) // 2
            if (m % 2) == 1:  # even index only
                m -= 1
            if nums[m] == nums[m+1]:
                i = m + 2
            else:
                j = m
        return nums[i]

    # works, O(1) space, but O(n) time
    """
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < (len(nums) - 1):
            if nums[i] != nums[i+1]:
                return nums[i]
            i += 2
        if i == len(nums):
            return nums[-1]
        return nums[i]
    """
