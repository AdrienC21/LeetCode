class Solution:
    # hint: dynamic programming and running sum per pile!
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[None for _ in range(k+1)] for _ in range(n)]
        
        # i pile, j remaining coins
        def recSearch(i: int, j: int) -> int:
            nonlocal dp
            
            if i == n:
                return 0
            if dp[i][j] is not None:
                return dp[i][j]

            sub_res = recSearch(i+1, j)
            running_sum_pile = 0
            for l in range(min(j, len(piles[i]))):
                running_sum_pile += piles[i][l]
                sub_res = max(sub_res, running_sum_pile + recSearch(i+1, j-l-1))
            dp[i][j] = sub_res
            return sub_res

        return recSearch(0, k)
