class Solution:
    def searchTarget(self, nums: List[int], target: int, m: int, i: int) -> int:
        i2 = i
        j2 = m
        while i2 < j2:
            m2 = (i2 + j2) // 2
            if nums[m2] == target:
                if (m2 == 0) or (nums[m2-1] != target):  # leftmost target
                    return m2
                j2 = m2 - 1
            else:  # nums[m2] < target
                i2 = m2 + 1
        if nums[i2] == target:
            return i2
        if nums[j2] == target:
            return j2
        return m
    def searchTarget2(self, nums: List[int], target: int, m: int, j: int, n: int) -> int:
        i2 = m
        j2 = j
        while i2 < j2:
            m2 = (i2 + j2) // 2
            if nums[m2] == target:
                if (m2 == (n-1)) or (nums[m2+1] != target):  # rightmost target
                    return m2
                i2 = m2 + 1
            else:  # nums[m2] > target
                j2 = m2 - 1
        if nums[i2] == target:
            return i2
        if nums[j2] == target:
            return j2
        return m
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # trivial cases
        if n == 0:
            return [-1, -1]
        if n == 1:
            if nums[0] == target:
                return [0, 0]
            return [-1, -1]
        # binary search two pointers
        i = 0
        j = n - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] == target:
                return [self.searchTarget(nums, target, m, i), self.searchTarget2(nums, target, m, j, n)]
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        if (nums[i] == target):
            temp = self.searchTarget(nums, target, i, i)
            return [temp, temp]
        if (nums[j] == target):
            temp = self.searchTarget(nums, target, j, j, n)
            return [temp, temp]
        return [-1, -1]