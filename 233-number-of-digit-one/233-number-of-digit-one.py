from math import log10
class Solution:
    def g(self, k: int) -> int:
        return k * (10**(k-1))
    def countDigitOne(self, n: int) -> int:
        res = 0  # final result
        while n != 0:
            k = int(log10(n))
            base = self.g(k)
            res += base
            nb = int(n // 10**k)
            if nb >= 2:
                res += ((nb - 1) * base + 10**k)
                n = n - nb*(10**k)
            else:
                n = n - 10**k
                res += (n + 1)
        return int(res)