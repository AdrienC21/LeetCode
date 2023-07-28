class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[[None, None] for _ in range(n)] for _ in range(n)]  # [score, index to take]
        for i in range(n):
            dp[i][i] = [nums[i], i]
            if i < (n - 1):
                if nums[i] >= nums[i+1]:
                    dp[i][i+1] = [nums[i], i]
                else:
                    dp[i][i+1] = [nums[i+1], i+1]

        def recSearch(i: int, j: int) -> Tuple[int, int]:
            if dp[i][j][0] is not None:
                return dp[i][j]
            # we take i
            other_player1 = recSearch(i+1, j)
            if other_player1[1] == (i+1):
                subres1 = recSearch(i+2, j)
            else:  # j
                subres1 = recSearch(i+1, j-1)
            subsum1 = subres1[0] + nums[i]

            # we take j
            other_player2 = recSearch(i, j-1)
            if other_player2[1] == i:
                subres2 = recSearch(i+1, j-1)
            else:  # j-1
                subres2 = recSearch(i, j-2)
            subsum2 = subres2[0] + nums[j]
            
            if subsum1 >= subsum2:  # best move is to take i
                dp[i][j] = [subsum1, i]
            else:  # best move is to take j
                dp[i][j] = [subsum2, j]
            return dp[i][j]
        
        score_player_1, _ = recSearch(0, n-1)
        score_player_2 = sum(nums) - score_player_1
        return (score_player_1 >= score_player_2)
                