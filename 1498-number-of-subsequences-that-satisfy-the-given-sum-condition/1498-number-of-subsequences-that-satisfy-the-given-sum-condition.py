class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        res = 0

        # not continuous subsequence so we can sort
        nums.sort()

        # double pointers
        i = 0
        j = n - 1
        while i <= j:
            if (nums[i] + nums[j]) <= target:
                res += pow(2, j - i, mod)  # directly exponentiate with modulo!
                i += 1
            else:  # decrease biggest number
                j -= 1

        return res % mod
