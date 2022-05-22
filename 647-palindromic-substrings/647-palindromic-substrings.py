class Solution:
    # O(n^2) solution. try radius!
    def radiusSearch(self, s: str, lens: int, i: int, j: int) -> int:
        res = 0
        while (i >= 0) and (j < lens):
            if s[i] != s[j]:
                break
            res += 1
            # expand the radius!
            i -= 1
            j += 1
        return res
    def countSubstrings(self, s: str) -> int:
        lens = len(s)
        res = 0
        for i in range(lens):
            res += self.radiusSearch(s, lens, i, i)
            if i < (lens - 1):  # search also palindrom with an even size
                res += self.radiusSearch(s, lens, i, i+1)
        return res
    
    # O(n^3) solution. Test all substrings
    """
    def isPalindromic(self, sub: str, n: int):
        for k in range(n//2):
            if sub[k] != sub[n-k-1]:
                return False
        return True
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                sub = s[i:(j+1)]
                if self.isPalindromic(sub, j-i+1):
                    res += 1
        return res
    """