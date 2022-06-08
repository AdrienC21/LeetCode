class Solution:
    # O(n) solution. Count number of 1 and 0 for each bit
    # for ones 1 at bit j across N elements, hamming distance at bit j
    # is nb * (N-nb)
    # then we sum!
    def totalHammingDistance(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(31, -1, -1):
            mask = 1 << i
            ones = 0
            for n in nums:
                if n & mask:
                    ones += 1
            zeros = N - ones
            res += zeros * ones
        return res

    # O(n^2) time limit exceeded
    """
    def hammingDistance(self, n1: int, n2: int) -> int:
        xor = n1 ^ n2  # bit equal to 1 if one is equal to 1 and the other equal to 0
        res = 0
        while xor:
            if (xor & 1) == 1:  # is last bit a 1?
                res += 1
            xor >>= 1  # shift 1
        return res

    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        tot_sum = 0
        for i in range(n-1):
            for j in range(i+1, n):
                hamming_distance = self.hammingDistance(nums[i], nums[j])
                tot_sum += hamming_distance
        return tot_sum
    """
