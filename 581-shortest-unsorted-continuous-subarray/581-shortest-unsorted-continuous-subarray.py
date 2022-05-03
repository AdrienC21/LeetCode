class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == nums2[i]:
                i += 1
            else:
                break
        if i == n:
            return 0
        j = n - 1
        while j > 0:
            if nums[j] == nums2[j]:
                j -= 1
            else:
                break
        if i == j:
            return 0
        else:
            return j-i+1