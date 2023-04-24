class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        n = len(stones)
        while n > 1:
            large1 = stones.pop()
            large2 = stones.pop()
            if large1 != large2:
                stones.append(large1 - large2)
                n -= 1
                for i in range(n-1, 0, -1):
                    if stones[i] < stones[i-1]:
                        stones[i], stones[i-1] = stones[i-1], stones[i]
                    else:
                        break
            else:
                n -= 2
        if n:
            return stones[0]
        else:
            return 0
    # Other solution with heap
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-stone for stone in stones]
        heapq.heapify(s)
        while len(s) >= 2:
            p2 = -heapq.heappop(s)
            p1 = -heapq.heappop(s)
            if p2 != p1:
                heapq.heappush(s, -(p2 - p1))
        if s:
            return -s[0]
        return 0
    """
