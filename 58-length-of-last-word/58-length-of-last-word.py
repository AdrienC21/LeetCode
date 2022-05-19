class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        j = n - 1
        while (j >= 0) and (s[j] == " "):
            j -= 1
        i = j
        while (i >= 0) and (s[i] != " "):
            i -= 1
        if i < 0:
            return j + 1
        return j - i