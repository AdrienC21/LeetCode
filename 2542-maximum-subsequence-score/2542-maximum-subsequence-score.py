class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        cum_sum = 0
        nums = sorted([(n2, n1) for n1, n2 in zip(nums1, nums2)], reverse=True)  # descending order
        min_heap = []  # heap more efficient

        for n2, n1 in nums:
            heapq.heappush(min_heap, n1)
            cum_sum += n1
            if len(min_heap) > k:
                cum_sum -= heapq.heappop(min_heap)
            if len(min_heap) == k:
                res = max(res, cum_sum * n2)

        return res

    """
    # TLE ...
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        if k == 1:
            return max(nums1[i] * nums2[i] for i in range(n))
        nums = [[nums1[i], nums2[i]] for i in range(n)]
        nums.sort(key=lambda x: x[1])
        res = -sys.maxsize
        
        accum = list(accumulate([nums[i][0] for i in range(n)][::-1]))[::-1]
        
        dp = [[None for _ in range(k)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = nums[i][0]
        for i in range(1, k+1):
            dp[n-i][i-1] = accum[n-i]
        
        def recSearch(i: int, j: int) -> int:
            nonlocal dp, n
            
            if dp[i][j] is not None:
                return dp[i][j]
            
            subres = max(nums[i][0] + recSearch(i+1, j-1), recSearch(i+1, j))
            dp[i][j] = subres
            return subres
        
        for i in range(n-k, -1, -1):
            res = max(res, (nums[i][0] + recSearch(i+1, k-2)) * nums[i][1])
        return res
    """
