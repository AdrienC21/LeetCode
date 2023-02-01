import numpy as np

class Solution:
    def gcd(self, a: int, b: int) -> int:
        if a < b:
            return self.gcd(b, a)
        if not(b):
            return a
        return self.gcd(b, a % b)

    def div(self, d: int) -> List[int]:
        if d == 1:
            return [1]
        res = [1]
        res2 = [d]
        for k in range(2, int(np.sqrt(d)) + 1):
            if d % k == 0:
                res.append(k)
                res2.append(d // k)
        while res:
            res2.append(res.pop())
        return res2

    def ispattern(self, s: str, p: str) -> bool:
        len_p = len(p)
        for k in range(0, len(s), len_p):
            if not(s[k:k+len_p] == p):
                return False
        return True
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not(str1) or not(str2):
            return ""
        n1 = len(str1)
        n2 = len(str2)
        d = self.gcd(n1, n2)
        div = self.div(d)
        for n in div:
            p = str2[:n]
            if self.ispattern(str1, p) and self.ispattern(str2, p):
                return p
        return ""
