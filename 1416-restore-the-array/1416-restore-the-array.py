class Solution:
    # O(nlog(k)) with bottom up approach
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        mod = 10**9 + 7
        dp = (n + 1) * [0]
        dp[-1] = 1
        for i in range(n-1, -1, -1):
            if s[i] == '0':  # trailing zero beginning
                continue
            current_nb = 0
            for j in range(i, n):
                current_nb = 10 * current_nb + int(s[j])
                if current_nb > k:  # stop, number too large
                    break
                # else, update dp
                dp[i] = (dp[i] + dp[j+1]) % mod

        return dp[0] % mod
    
    # value too large cause cases are counted twice
    # also slower because of top down approach ...
    """
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        mod = 10**9 + 7
        dp = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
            if (s[i] != '0'):
                if int(s[i]) <= k:
                    dp[i][i] = 1
            else:
                for j in range(i+1, n):
                    dp[i][j] = 0

        def recSearch(i: int, j: int) -> int:
            nonlocal dp
            
            if dp[i][j] is not None:
                return dp[i][j]
            sub_res = 1 if int(s[i:j]) <= k else 0
            for l in range(i, j):
                sub_res += recSearch(i, l) * recSearch(l+1, j)
            dp[i][j] = sub_res
            return sub_res
            
        return recSearch(0, n-1) % mod
    """
