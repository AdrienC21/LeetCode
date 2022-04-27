class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_set = set()
        nums2 = sorted(nums)
        n = len(nums2)
        for i in range(n-2):
            if (i > 0) and (nums2[i] == nums2[i-1]):
                continue
            left = i + 1
            right = n - 1
            while left < right:
                sum_val = nums2[i] + nums2[left] + nums2[right]
                if sum_val > 0:
                    right -= 1
                elif sum_val == 0:
                    res_set.add((nums2[i], nums2[left], nums2[right]))
                    left += 1
                else:
                    left += 1
        return list(res_set)