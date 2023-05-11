class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[None for _ in range(n)] for _ in range(m)]
        
        def recSearch(i: int, j: int) -> int:
            nonlocal dp, m, n
            
            if (i >= m) or (j >= n):
                return 0
            if dp[i][j] is not None:
                return dp[i][j]
            sub_res = 0
            for k in range(j, n):
                if nums1[i] == nums2[k]:
                    sub_res = recSearch(i+1, k+1) + 1
                    break
            sub_res = max(sub_res, recSearch(i+1, j))
            dp[i][j] = sub_res
            return sub_res
        
        return recSearch(0, 0)
