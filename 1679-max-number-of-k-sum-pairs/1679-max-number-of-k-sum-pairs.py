from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        for c in nums:
            if c < k:
                d[k-c].append(c)
        nb_operations = 0
        for c in nums:
            if c < k:
                if (k-c) == c:
                    if len(d[c]) > 1:
                        d[c].pop()
                        d[c].pop()
                        nb_operations += 1
                elif d[k-c] and d[c]:
                    d[k-c].pop()
                    d[c].pop()
                    nb_operations += 1
        return nb_operations