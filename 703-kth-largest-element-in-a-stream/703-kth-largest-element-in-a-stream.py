class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        self.lenHeap = 0
        for nb in nums:
            self.add(nb)
        
    def add(self, val: int) -> int:
        if self.lenHeap < self.k:
            heapq.heappush(self.heap, val)
            self.lenHeap += 1
 
        elif self.heap[0] < val:  # smallest element in heap on the left!
            heapq.heappushpop(self.heap, val)  # heappushpop method!
 
        if self.lenHeap == self.k:
            return self.heap[0]
        else:
            return -1
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)