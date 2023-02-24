class Solution:
    # Partially mine ...
    # O(N * log(N) * log(M)), N = len(nums), M = max(nums)
    def minimumDeviation(self, nums: List[int]) -> int:
        q = []  # min heap
        for n in nums:
            q.append(-2 * n if (n % 2) == 1 else -n)
        res = sys.maxsize
        maxval = max(q)
        heapq.heapify(q)
        while True:
            val = heapq.heappop(q)
            res = min(res, maxval - val)
            if (val % 2) == 1:
                break
            val >>= 1
            maxval = max(maxval, val)
            heapq.heappush(q, val)
        return res
