class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                j = dic[n]
                if (i - j) <= k:
                    return True
            dic[n] = i
        return False