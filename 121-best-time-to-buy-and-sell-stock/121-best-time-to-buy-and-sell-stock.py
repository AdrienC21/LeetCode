from functools import reduce
class Solution:
    def recMaxProf(self, prices, i, k, buy, L):
        if (i >= len(prices) or k <= 0):
            return 0

        if (L[i][buy] != -1):
            return L[i][buy]

        if buy:
            L[i][buy] = max(-prices[i] + self.recMaxProf(prices, i+1, k, 1-buy, L),
                            self.recMaxProf(prices, i+1, k, buy, L))
            return L[i][buy]
        else:
            L[i][buy] = max(prices[i] + self.recMaxProf(prices, i+1, k-1, 1-buy, L),
                            self.recMaxProf(prices, i+1, k, buy, L))
            return L[i][buy]
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        L = [[-1 for _ in range(2)] for _ in range(n)]
        return self.recMaxProf(prices, i=0, k=1, buy=1, L=L)
