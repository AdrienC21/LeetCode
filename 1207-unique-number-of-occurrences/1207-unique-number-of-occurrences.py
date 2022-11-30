class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        for n in arr:
            freq[n] += 1
        s = set()
        for v in freq.values():
            if v in s:
                return False
            s.add(v)
        return True
