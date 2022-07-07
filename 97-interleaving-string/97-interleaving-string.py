class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if not(n):
            return s2 == s3
        if not(m):
            return s1 == s3
        if len(s3) != (m + n):
            return False
        dp = [[None for _ in range(m+1)] for _ in range(n+1)]
        dp[n][m] = 1
        def recSearch(i: int, j: int):
            # recursively search if there is a match, start from the end!
            nonlocal dp, n, m
            if not(dp[i][j] is None):
                return dp[i][j]
            if i == n:
                if s2[-(j+1)] == s3[-(i+j+1)]:
                    sub_res = recSearch(i, j+1)
                    dp[i][j] = sub_res
                    return sub_res
                dp[i][j] = 0
                return 0
            if j == m:
                if s1[-(i+1)] == s3[-(i+j+1)]:
                    sub_res = recSearch(i+1, j)
                    dp[i][j] = sub_res
                    return sub_res
                dp[i][j] = 0
                return 0
            if (s1[-(i+1)] == s3[-(i+j+1)]) and not(s2[-(j+1)] == s3[-(i+j+1)]):
                sub_res = recSearch(i+1, j)  # if it's 0, return 0, if it's 1, return 1
                dp[i][j] = sub_res
                return sub_res
            if (s2[-(j+1)] == s3[-(i+j+1)]) and not(s1[-(i+1)] == s3[-(i+j+1)]):
                sub_res = recSearch(i, j+1)  # if it's 0, return 0, if it's 1, return 1
                dp[i][j] = sub_res
                return sub_res
            if (s1[-(i+1)] == s3[-(i+j+1)]) and (s2[-(j+1)] == s3[-(i+j+1)]):
                sub_res = recSearch(i+1, j)
                if not(sub_res):
                    sub_res = recSearch(i, j+1)
                dp[i][j] = sub_res
                return sub_res
            dp[i][j] = 0  # no letter from s1 or s2 match at this position of s3
            return 0
        if recSearch(0, 0):
            return True
        return False
