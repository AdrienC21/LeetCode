import numpy as np
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        bs = np.array([int(x) for x in s])  # binary string as a list of int
        ones_to_flip = [0] + list(accumulate(bs))
        zeros_to_flip = list(accumulate((1 - bs)[::-1]))[::-1]
        zeros_to_flip = zeros_to_flip + [0]

        res = sys.maxsize
        for i in range(n+1):
            res = min(res, ones_to_flip[i]+zeros_to_flip[i])
        return res
