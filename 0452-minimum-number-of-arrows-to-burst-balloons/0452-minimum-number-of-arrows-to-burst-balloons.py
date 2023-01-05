class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])  # sort by end
        current_end = -sys.maxsize
        res = 0  # number of arrows to shoot
        for start, end in points:
            if start > current_end:  # this balloons and the next ones will not be bursted by the last arrow
                current_end = end
                res += 1
        return res
