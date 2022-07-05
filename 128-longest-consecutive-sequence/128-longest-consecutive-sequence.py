class Solution:
    # O(n) time. Because on average, if there are k sequence in nums, we search in the set
    # k * (n/k) times
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            seen.add(n)
        longest_sequence = 0
        for n in nums:
            if not((n - 1) in seen):  # it is the beginning of a sequence, calculate its length
                sequence = 1
                j = n + 1
                while j in seen:
                    j += 1
                    sequence += 1
                longest_sequence = max(longest_sequence, sequence)
        return longest_sequence
                
    # solution, but not optimal because min takes too much time
    """
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
    """
