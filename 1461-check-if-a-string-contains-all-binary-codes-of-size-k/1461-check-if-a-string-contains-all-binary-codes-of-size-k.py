class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        n = len(s)
        for i in range(k-1, n):
            seen.add(s[i-k+1:i+1])
        return len(seen) == (2**k)
