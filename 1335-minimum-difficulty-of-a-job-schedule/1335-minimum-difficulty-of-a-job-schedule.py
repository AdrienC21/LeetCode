class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:  # more tasks than days
            return -1
        
        # pre compute the combinations of maximums
        max_2D = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            max_2D[i][i] = jobDifficulty[i]
            for j in range(i+1, n):
                max_2D[i][j] = max(max_2D[i][j-1], jobDifficulty[j])

        running_sum = list(accumulate(jobDifficulty))
        dp = [[None for _ in range(d)] for _ in range(n)]
        # init dp
        for i in range(1, d+1):  # i element,i task remaining,at least a task per day
            prev_sum = running_sum[-(i+1)] if (i+1) <= n else 0
            dp[-i][i-1] = running_sum[-1] - prev_sum
        for i in range(1, d):  # i tasks
            for k in range(i+1, d+1):  # k days > i => impossible, no free day
                dp[-i][k-1] = sys.maxsize
        for i in range(n):  # 1 day remaining => do all the remaining task
            dp[i][0] = max_2D[i][n-1]

        # rec function
        def recSearch(i: int, k: int) -> int:
            nonlocal dp, n, d
            if i >= n:
                if k == -1:
                    return 0
                return sys.maxsize  # no free day

            if not(dp[i][k] is None):
                return dp[i][k]
            val = sys.maxsize
            for j in range(i, n):
                val = min(val, max_2D[i][j] + recSearch(j+1, k-1))
            dp[i][k] = val
            return val
        
        res = recSearch(0, d-1)
        if res == sys.maxsize:
            return -1
        return res
