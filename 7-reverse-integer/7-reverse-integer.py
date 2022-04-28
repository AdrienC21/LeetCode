class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        l = list(str(abs(x)))
        l = l[::-1]
        res = int("".join(l))
        res = sign * res
        if (res < -(2**31)) or (res > ((2**31) - 1)):
            res = 0
        return res