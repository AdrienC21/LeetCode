class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        a = a % 1337
        res = 1  # product of a**b0 * a**(10 * b1) * ....
        a_pow_10 = a  # a, a**10, a**100, etc mod n
        
        # (a*b)[n] = (a[n] * b[n])[n]

        for i in range(len(b)-1, -1, -1):
            res = (res * ((a_pow_10 ** b[i]) % 1337) % 1337)
            a_pow_10 = (a_pow_10 ** 10) % 1337
        return res