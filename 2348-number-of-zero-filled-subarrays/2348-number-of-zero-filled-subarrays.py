class Solution:

    def __init__(self):
        self.cache = {1: 1}
    
    def calculate_nb_subarray(self, k: int) -> int:
        if k in self.cache:
            return self.cache[k]
        res = self.calculate_nb_subarray(k-1) + k
        self.cache[k] = res
        return res

    # O(max size subarray) + O(len nums) = O(n)
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        # pointers in nums
        i = 0
        j = 0
        n = len(nums)
        while i < n:
            if nums[i]:
                i += 1
                continue
            j = i + 1
            while (j < n) and not(nums[j]):
                j += 1
            res += self.calculate_nb_subarray(j - i)
            i = j
        return res
