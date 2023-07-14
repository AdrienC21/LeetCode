class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = n * [None]
        dp[-1] = 1
        
        indexes = defaultdict(list)
        for i, num in enumerate(arr):
            indexes[num].append(i)

        def recSearch(i: int) -> int:
            nonlocal dp
            
            if dp[i] is not None:
                return dp[i]
            
            j = bisect_right(indexes[arr[i] + difference], i)
            if j == len(indexes[arr[i] + difference]):  # index does not exist
                dp[i] = 1
            else:
                dp[i] = 1 + recSearch(indexes[arr[i] + difference][j])
            
            return dp[i]

        return max(recSearch(i) for i in range(n-1, -1, -1))
