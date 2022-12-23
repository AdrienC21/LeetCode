class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[None, None] for _ in range(n)]
        
        def recSearch(i: int, buy: int) -> int:
            nonlocal prices, dp, n
            if i >= n:
                return 0
            if dp[i][buy] is not None:
                return dp[i][buy]
            if not(buy):  # buy == 0, sell
                res = max(prices[i] + recSearch(i+2, 1), recSearch(i+1, 0))
            else:
                res = max(-prices[i] + recSearch(i+1, 0), recSearch(i+1, 1))
            dp[i][buy] = res
            return res
        
        return recSearch(0, 1)
