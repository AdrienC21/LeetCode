from functools import lru_cache


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp_seq = n * [1]

        dp_count = n * [1]  # dp store counts

        for i, num in enumerate(nums):
            for j in range(i):
                if nums[i] > nums[j]:  # increasing seq
                    if (dp_seq[j] + 1) == dp_seq[i]:
                        dp_count[i] += dp_count[j]
                    elif (dp_seq[j] + 1) > dp_seq[i]:  # update largest sequence
                        dp_count[i] = dp_count[j]
                        dp_seq[i] = dp_seq[j] + 1

        # Longest Increasing Subsequence
        lis = max(dp_seq)

        # Count of lis
        res = 0

        # Iterate over the lists
        for seq, count in zip(dp_seq, dp_count):
            if seq == lis:
                res += count
        return res
