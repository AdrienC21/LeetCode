class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        m = (left + right) // 2
        while left < right:
            val = nums[m]
            if val == target:
                return m
            elif val < target:
                left = m + 1
            else:
                right = m - 1
            m = (left + right) // 2
        if left == right:
            if nums[left] == target:
                return left
        return -1