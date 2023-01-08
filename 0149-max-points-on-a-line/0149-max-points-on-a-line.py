import sys

class Solution:
    def slope(self, p1: List[int], p2: List[int]) -> float:
        # calculate slope between two points
        if p1[0] == p2[0]:
            return sys.maxsize
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    def maxPoints(self, points: List[List[int]]) -> int:
        points.sort()  # sort by x, then y

        # list of lines [nb_points_on_line, [points_on_the_line], slope_of_the_line]
        def recSearch(points: List[List[int]]) -> list:
            if not(points):
                return []
            n = len(points)
            if n == 1:
                # return line with 1 point (slope None at the moment)
                return [[1, points, None]]
            elif n == 2:
                return [[2, points, self.slope(points[0], points[1])]]
            res = recSearch(points[1:])
            p1 = points[0]
            points_to_ignore = set()  # ignore all the p such that p1 is already aligned with p
            for i, (nb, list_p, slope) in enumerate(res):
                if self.slope(p1, list_p[0]) == slope:  # p1 on this line, update its count
                    res[i][0] += 1
                    res[i][1].append(p1)
                    for p in list_p:
                        points_to_ignore.add(tuple(p))
            # add lines with 2 points for the points p that are not aligned with p1 and an existing line
            for p in points[1:]:
                if tuple(p) not in points_to_ignore:
                    res.append([2, [p1, p], self.slope(p1, p)])
            
            return res
        
        L = recSearch(points)
        return max([l[0] for l in L])
