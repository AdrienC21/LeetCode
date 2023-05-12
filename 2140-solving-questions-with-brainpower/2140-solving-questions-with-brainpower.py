class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [None for i in range(n)]
        dp[n-1] = questions[n-1][0]
        max_dp = [None for _ in range(n)]
        max_dp[n-1] = dp[n-1]
        
        def get_max_dp(i: int) -> int:
            nonlocal max_dp, dp

            if max_dp[i] is not None:
                return max_dp[i]
            max_dp[i] = max(get_max_dp(i+1), dp[i])
            return max_dp[i]

        for j in range(n-2, -1, -1):
            sub_res = questions[j][0]
            if (j + 1 + questions[j][1]) < n:
                sub_res += dp[j + 1 + questions[j][1]]
            sub_res = max(sub_res, get_max_dp(j+1))
            dp[j] = sub_res
        
        return dp[0]
