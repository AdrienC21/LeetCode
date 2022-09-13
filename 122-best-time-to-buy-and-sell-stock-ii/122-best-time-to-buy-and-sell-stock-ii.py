class Solution:
    def recMaxProf(self, prices: List[int], i: int, buy: int, L: List[List[int]]) -> int:
        if i >= len(prices):
            return 0

        if (L[i][buy] != -1):
            return L[i][buy]

        if buy:
            L[i][buy] = max(-prices[i] + self.recMaxProf(prices, i+1, 1-buy, L),
                            self.recMaxProf(prices, i+1, buy, L))
            return L[i][buy]
        else:
            L[i][buy] = max(prices[i] + self.recMaxProf(prices, i+1, 1-buy, L),
                            self.recMaxProf(prices, i+1, buy, L))
            return L[i][buy]
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        L = [[-1 for _ in range(2)] for _ in range(n)]
        return self.recMaxProf(prices, i=0, buy=1, L=L)
