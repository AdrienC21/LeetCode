# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1
        j = n
        is_bad = 1 # min bad value found
        while i < j:
            m = (i + j) // 2
            if isBadVersion(m):
                j = m - 1
                is_bad = m
            else:
                i = m + 1
        if j < i:
            return is_bad
        if isBadVersion(i):
            return i
        return is_bad