class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        for i, p in enumerate(prices):
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices
