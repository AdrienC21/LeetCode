class Solution:
    # more efficient, bitwise manipulation
    def __init__(self):
        self.mod = (10**9 + 7)
    def concatenatedBinary(self, n: int) -> int:
        res = 0
        nb_pair = 0
        for k in range(1, n+1):
            if k&(k-1) == 0:
                nb_pair += 1
            res = ((res << nb_pair) % self.mod + k) % self.mod
        return res
    # TLE
    """
    def __init__(self):
        self.mod_nb = (10**9 + 7)
    def binary_to_int(self, s: str) -> int:
        power = 1
        res = 0
        for i in range(len(s)):
            res += int(s[-(i+1)]) * power
            res %= self.mod_nb
            power *= 2
        return res
    def int_to_binary(self, n: int) -> str:
        res = []
        while n:
            res.append(str(n%2))
            n = n // 2
        return "".join(res[::-1])
    def concatenatedBinary(self, n: int) -> int:
        tot = []
        for k in range(1, n+1):
            tot.append(self.int_to_binary(k))
        return self.binary_to_int("".join(tot))
    """
