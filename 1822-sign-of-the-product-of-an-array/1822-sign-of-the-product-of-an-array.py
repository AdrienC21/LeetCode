class Solution:
    def arraySign(self, nums: List[int]) -> int:
        nb_neg = 0
        for n in nums:
            if not(n):
                return 0
            if n < 0:
                if nb_neg:
                    nb_neg = 0
                else:
                    nb_neg = 1
        if nb_neg:
            return -1
        return 1

    """
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for n in nums:
            if not(n):
                return 0
            if n < 0:
                res *= -1
        return res
    """
