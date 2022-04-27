class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        d = deque()  # use deque
        ans = -sys.maxsize
        for x, y in points:
            while d and (x - d[0][1]) > k:
                d.popleft()
            if d:
                ans = max(ans, d[0][0] + x + y)
            while d and (d[-1][0] <= (y - x)):
                d.pop()
            d.append((y-x, x))
        return ans