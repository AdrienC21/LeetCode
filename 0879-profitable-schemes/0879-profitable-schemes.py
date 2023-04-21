import numpy as np

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        nb_groups = len(group)
        dp = np.zeros((nb_groups+1, n+1, minProfit+1), dtype=int)
        mod = 10**9 + 7

        for j in range(n+1):  # base scenario
            dp[nb_groups, j, minProfit] = 1
        
        for i in range(nb_groups-1, -1, -1):
            for j in range(n+1):
                for p in range(minProfit+1):
                    dp[i, j, p] = dp[i+1, j, p]
                    if (j + group[i]) <= n:  # we can recruit this person
                        dp[i, j, p] += dp[i+1, j+group[i], min(minProfit, p+profit[i])]
                        # min used above to cap the dp
                        dp[i, j, p] %= mod
        return dp[0, 0, 0] % mod

    # rec solution with 3 variables TLE ...
    # dp with dict works but slower
    # so dp with array, still with bottom up approach!
    """
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = defaultdict(int)
        mod = 10**9 + 7
        nb_groups = len(group)
        
        for j in range(n+1):  # base scenario
            dp[(nb_groups, j, minProfit)] = 1
        
        for i in range(nb_groups-1, -1, -1):
            for j in range(n+1):
                for p in range(minProfit+1):
                    dp[(i, j, p)] = dp[(i+1, j, p)]
                    if (j + group[i]) <= n:  # we can recruit this person
                        dp[(i, j, p)] += dp[(i+1, j+group[i], min(minProfit, p+profit[i]))]
                        # min used above to cap the dp
                        dp[(i, j, p)] %= mod
        return dp[(0, 0, 0)] % mod
    """
