class Solution:
    def dicho(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] == target:
                return m + 1
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        if i == j:
            if (nums[i] == target) or (nums[i] < target):
                return i + 1
            return i
        return max(i, j)
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums2 = list(accumulate(sorted(nums)))
        return [self.dicho(nums2, q) for q in queries]
