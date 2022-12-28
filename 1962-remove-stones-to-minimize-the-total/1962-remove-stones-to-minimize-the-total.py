class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapq.heapify(heap)
        for _ in range(k):
            stones = -heapq.heappop(heap)
            stones -= (stones // 2)
            heapq.heappush(heap, -stones)
        return -sum(heap)
