class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        pow_26 = 1
        for i in range(len(columnTitle)-1, -1, -1):
            c = columnTitle[i]
            res += (ord(c) - ord("A") + 1) * pow_26
            pow_26 *= 26
        return res