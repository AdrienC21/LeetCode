class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[None, None] for _ in range(n)]
        
        def recSearch(i: int, buy: int) -> int:
            nonlocal n, dp, fee
            
            if i >= n:
                return 0
            if dp[i][buy] is not None:
                return dp[i][buy]
            if buy:
                res = max(recSearch(i+1, buy), recSearch(i+1, 1-buy) - prices[i])
                dp[i][buy] = res
                return res
            res = max(recSearch(i+1, buy), recSearch(i+1, 1-buy) + prices[i] - fee)
            dp[i][buy] = res
            return res

        return recSearch(0, 1)
