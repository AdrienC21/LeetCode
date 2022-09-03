class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def generate(d, nb_digits):
            nonlocal k
            if not(nb_digits):
                return []
            if nb_digits == 1:
                return [str(d)]
            else:
                res = []
                if k == 0:
                    res.extend(generate(d, nb_digits - 1))
                else:
                    if (d - k) >= 0:
                        res.extend(generate(d-k, nb_digits - 1))
                    if (d + k) <= 9:
                        res.extend(generate(d+k, nb_digits - 1))
                return [str(d) + x for x in res]
        res = []
        for d in range(1, 10):
            res.extend(generate(d, n))
        return [int(x) for x in res]
