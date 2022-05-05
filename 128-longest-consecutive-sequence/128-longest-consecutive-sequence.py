class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            seen.add(n)
        longest_sequence = 0
        while seen:
            n = min(seen)
            seen.discard(n)
            current_sequence = 1
            while seen and ((n+1) in seen):
                n += 1
                current_sequence += 1
                seen.discard(n)
            longest_sequence = max(longest_sequence, current_sequence)
        return longest_sequence