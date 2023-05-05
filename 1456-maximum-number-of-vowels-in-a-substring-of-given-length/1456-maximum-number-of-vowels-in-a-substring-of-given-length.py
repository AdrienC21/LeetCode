class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        i = 0
        j = k-1
        res = sum(s[l] in vowels for l in range(k))
        current = res
        while j < (n - 1):
            j += 1
            i += 1
            if s[i-1] in vowels:
                current -= 1
            if s[j] in vowels:
                current += 1
            res = max(res, current)
        return res
            