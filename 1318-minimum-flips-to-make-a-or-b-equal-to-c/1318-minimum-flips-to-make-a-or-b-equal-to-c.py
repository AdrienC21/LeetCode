class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a_bit = list(map(lambda x: int(x), list(format(a, 'b'))))
        b_bit = list(map(lambda x: int(x), list(format(b, 'b'))))
        c_bit = list(map(lambda x: int(x), list(format(c, 'b'))))
        n = max(len(a_bit), max(len(b_bit), len(c_bit)))
        # complete the bit sequences
        a_bit = (n - len(a_bit)) * [0] + a_bit
        b_bit = (n - len(b_bit)) * [0] + b_bit
        c_bit = (n - len(c_bit)) * [0] + c_bit
        res = 0
        for i in range(n):
            if c_bit[i]:
                if a_bit[i] or b_bit[i]:
                    continue
                res += 1
            else:
                res += a_bit[i] + b_bit[i]
        return res
