class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        s = set(nums[0])
        for num in nums[1:]:
            s = s.intersection(set(num))
        return sorted(list(s))
