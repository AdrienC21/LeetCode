import numpy as np
class Solution:
    def calcSlope(self, p1: List[int], p2: List[int]) -> float:
        if p2[0] == p1[0]:
            slope = np.inf
        elif p2[1] == p1[1]:
            slope = 0
        else:
            slope = (p2[1] -  p1[1]) / (p2[0] - p1[0])
        return slope
    def recSearch(self, points: List[List[int]]):
        if points == []:
            return []
        n = len(points)
        if n == 1:
            return [[1, [points[0]], None]]
        elif n == 2:
            p1 = points[0]
            p2 = points[1]
            slope = self.calcSlope(p1, p2)
            return [[2, points, slope]]
        else:
            p = points[0]
            subres = self.recSearch(points[1:])
            points_to_exclude = []
            for i, group in enumerate(subres):
                if self.calcSlope(p, group[1][0]) == group[2]:  # points in the same group
                    subres[i][0] = group[0] + 1
                    subres[i][1].append(p)
                    for p_ex in group[1]:  # we are aligned to those points, a group is already formed
                        points_to_exclude.append(p_ex)
            for p2 in points[1:]:
                if not(p2 in points_to_exclude):
                    subres.append([2, [p, p2], self.calcSlope(p, p2)])
            return subres
            
    def maxPoints(self, points: List[List[int]]) -> int:
        points_sorted = sorted(points, key=lambda x: x[0])
        res = self.recSearch(points_sorted)
        return reduce(lambda x,y: max(x, y), map(lambda x: x[0], res))