class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        if j < 0:
            return 0
        if nums[i] < target:
            return i + 1
        return i
