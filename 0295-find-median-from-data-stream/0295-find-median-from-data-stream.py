# better idea, two heaps! One left heap with the n/2 smallest elements, one right heap with the n/2 biggest elements
# python heap: biggest element first
class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        heapq.heapify(self.left_heap)
        heapq.heapify(self.right_heap)
    
    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_heap, -num)
        
        # check
        if self.left_heap and self.right_heap and (-self.left_heap[0] > self.right_heap[0]):
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        # if size difference strictly greater than 1, equilibrate
        if len(self.left_heap) > (len(self.right_heap) + 1):
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        if len(self.right_heap) > (len(self.left_heap) + 1):
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))
        
    def findMedian(self) -> float:
        if len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]
        if len(self.right_heap) > len(self.left_heap):
            return self.right_heap[0]
        # else equal size
        return (-self.left_heap[0] + self.right_heap[0]) / 2

# first try, with dicho and update position of the median
"""
class MedianFinder:

    def __init__(self):
        self.left_pos = None
        self.right_pos = None
        self.values = []
    
    def dicho(self, L: list, num: int) -> int:
        i = 0
        j = len(L) - 1
        while i < j:
            m = (i + j) // 2
            if L[m] <= num:
                i = m + 1
            else:
                j = m
        if i < len(L):
            if L[i] <= num:
                return i + 1
        return i
    
    def addNum(self, num: int) -> None:
        if not(self.values):
            self.values.append(num)
            self.left_pos = 0
            self.right_pos = 0
            return
        d = self.dicho(self.values, num)
        if self.left_pos == self.right_pos:
            if d >= self.right_pos:
                self.right_pos += 1
                self.values.insert(d, num)
                self.median = (self.left_pos + self.right_pos) / 2
            else:
                if self.left_pos:
                    self.left_pos -= 1
                else:
                    self.right_pos += 1
                self.values.insert(d, num)
                self.median = (self.left_pos + self.right_pos) / 2
        else:
            self.values.insert(d, num)
            self.left_pos += 1

    def findMedian(self) -> float:
        if self.left_pos == self.right_pos:
            return self.values[self.left_pos]
        return (self.values[self.left_pos] + self.values[self.right_pos]) / 2
"""

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()