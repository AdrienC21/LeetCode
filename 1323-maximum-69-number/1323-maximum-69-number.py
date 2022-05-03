class Solution:
    def maximum69Number(self, num: int) -> int:
        i = 0
        s = str(num)
        n = len(s)
        while (i < n) and (s[i] == "9"):
            i += 1
        if (i == n):
            return num  # only 9s
        return int(s[:i]+"9"+s[i+1:])  # replace the leftmost 6 by a 9