class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        n = len(needle)
        h = len(haystack)
        if n > h:
            return -1
        i = 0
        while (i <= (h-n)):
            if haystack[i:i+n] == needle:
                return i
            i += 1
        return -1