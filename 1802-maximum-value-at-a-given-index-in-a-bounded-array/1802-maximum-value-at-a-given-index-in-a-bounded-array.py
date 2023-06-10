class Solution:
    def cum_sum(self, k: int) -> int:
        return (k * (k + 1)) // 2

    def valIndex(self, val: int, n: int, index: int, maxSum: int) -> bool:
        res = 0
        # left sum
        res += self.cum_sum(val)
        if val > (index + 1):
            res -= self.cum_sum(val - index - 1)
        else:
            res += index - val + 1
        # right sum
        res += self.cum_sum(val - 1)
        if val > (n - index):
            res -= self.cum_sum(val - n + index)
        else:
            res += n - index - val
        return res <= maxSum

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        i = 0
        j = maxSum
        while i < j:
            m = i + (j - i) // 2
            if self.valIndex(m, n, index, maxSum):
                i = m + 1
            else:
                j = m - 1
        k = min(i, j)
        if k < 1:
            return 1
        while self.valIndex(k, n, index, maxSum):
            k += 1
        return k - 1
