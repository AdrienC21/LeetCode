class Solution:
    # complexity, time O(log(k)*n^2), space O(k)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        heapq.heapify(h)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if len(h) < k:
                    heapq.heappush(h, -matrix[i][j])
                elif -matrix[i][j] > h[0]:
                    heapq.heappushpop(h, -matrix[i][j])
        return -heapq.heappop(h)
        
    # time limit exceeded
    # complexity, time O(n^2) (worst case O(k*n^2)), space O(k)
    """
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        d = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if len(d) < k:
                    d.append(matrix[i][j])
                    p = len(d) - 1
                    while (p > 0) and (d[p] < d[p-1]):
                        d[p], d[p-1] = d[p-1], d[p]
                        p -= 1
                elif matrix[i][j] < d[-1]:
                    d.pop()
                    d.append(matrix[i][j])
                    p = k - 1
                    while (p > 0) and (d[p] < d[p-1]):
                        d[p], d[p-1] = d[p-1], d[p]
                        p -= 1
        return d[-1]
    """
