from itertools import combinations
from numpy import sum as sss
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res_set = set()
        nums2 = sorted(nums)
        n = len(nums2)
        for i in range(n-3):
            if (i > 0) and (nums2[i] == nums2[i-1]):
                continue
            for j in range(i+1, n-2):
                if (j > (i+1)) and (nums2[j] == nums2[j-1]):
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    sum_val = nums2[i] + nums2[j] + nums2[left] + nums2[right]
                    if sum_val > target:
                        right -= 1
                    elif sum_val == target:
                        res_set.add((nums2[i], nums2[j], nums2[left], nums2[right]))
                        left += 1
                    else:
                        left += 1
        return list(res_set)