class Solution:
    def partitionString(self, s: str) -> int:
        res = 1
        i = 0
        n = len(s)
        current_set = set()
        while i < n:
            if s[i] not in current_set:
                current_set.add(s[i])
            else:
                current_set = set([s[i]])
                res += 1
            i += 1
        return res
