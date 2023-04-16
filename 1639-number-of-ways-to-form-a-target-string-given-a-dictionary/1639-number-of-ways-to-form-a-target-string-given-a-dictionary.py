class Solution:
    # not mine, use optimized DP
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7
        m = len(target)
        n = len(words[0])
        # count occurence of letters per position
        count = [[0 for _ in range(26)] for _ in range(n)]
        for w in words:
            for k, c in enumerate(w):
                count[k][ord(c) - ord('a')] += 1
        # dp
        dp = [[None for _ in range(n)] for _ in range(m)]

        def recSearch(i: int, j: int) -> int:
            nonlocal dp, mod, count

            if i >= m:
                return 1
            if j >= n:
                return 0
            if dp[i][j] is not None:
                return dp[i][j]

            res = recSearch(i, j + 1) + recSearch(i + 1, j + 1) * count[j][ord(target[i]) - ord('a')]
            res %= mod
            dp[i][j] = res
            return res

        return recSearch(0, 0)
