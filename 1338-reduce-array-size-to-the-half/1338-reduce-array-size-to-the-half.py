from collections import defaultdict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        for num in arr:
            freq[num] += 1
        freq_list = list(freq.values())
        freq_list.sort()
        target = len(arr) // 2
        removed = 0
        count = 0
        while removed < target:
            removed += freq_list.pop()
            count += 1
        return count
