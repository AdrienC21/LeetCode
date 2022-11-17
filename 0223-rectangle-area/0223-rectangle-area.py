class Solution:
    def area(self, x1: int, x2: int, y1: int, y2: int) -> int:
        return (y2 - y1) * (x2 - x1)
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        tot = self.area(ax1, ax2, ay1, ay2) + self.area(bx1, bx2, by1, by2)
        if (ax2 <= bx1) or (ay1 >= by2) or (ax1 >= bx2) or (ay2 <= by1):  # no overlap
            return tot
        x = min(ax2, bx2) - max(ax1, bx1)
        y = min(ay2, by2) - max(ay1, by1)
        return tot - x * y  # remove intersection
