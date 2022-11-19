class Solution:
    def is_left(self, p1: List[int], p2: List[int], m: List[int]):
        # (piM x pi pj).uz >= 0 if m to the right of segment pipj
        # x is vectorial product
        return ((p2[0]-p1[0])*(m[1]-p1[1])-(p2[1]-p1[1])*(m[0]-p1[0])) > 0

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        hull = []
        trees.sort(key=lambda x: (x[0], x[1]))  # left to right, down to up if equality

        # lower hull: left to right
        for tree in trees:
            while (len(hull) > 1) and self.is_left(hull[-1], hull[-2], tree):
                hull.pop()
            hull.append(tuple(tree))
        hull.pop()  # remove last duplicated element

        # upper hull: left to right
        for tree in trees[::-1]:
            while (len(hull) > 1) and self.is_left(hull[-1], hull[-2], tree):
                hull.pop()
            hull.append(tuple(tree))  # remove last duplicated element

        # remove duplcated element
        return list(set(hull))

# fail to implement
"""
from scipy.spatial import ConvexHull
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        hull = ConvexHull(points=trees)
        trees_on_perimeter = set()
        for p in hull.vertices:
            trees_on_perimeter.add(tuple(trees[p]))
        return [list(t) for t in trees_on_perimeter]
"""
# TLE, O(n^3) hull algo complexity
"""
class Solution:
    def is_left(self, p1: List[int], p2: List[int], m: List[int]):
        # (piM x pi pj).uz >= 0 if m to the right of segment pipj
        # x is vectorial product
        return ((p2[0]-p1[0])*(m[1]-p1[1])-(p2[1]-p1[1])*(m[0]-p1[0]))>0
    
    def convex_hull(self, points: List[List[int]]) -> List[Tuple[Tuple[int,int], Tuple[int,int]]]:
        N = len(points)
        if N == 1:
            return [(tuple(points[0]),tuple(points[0]))]
        hull = []
        for i in range(N):
            for j in range(N):
                if i != j:
                    border = True
                    for k in range(N):
                        if (k != i) and (k != j):
                            if self.is_left(points[i], points[j], points[k]):
                                border = False
                                break
                    if border:
                        hull.append((tuple(points[i]),tuple(points[j])))
        return hull

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        hull = self.convex_hull(trees)
        points_on_perimeter = set()
        for p1, p2 in hull:
            points_on_perimeter.add(p1)
            points_on_perimeter.add(p2)
        return [list(p) for p in points_on_perimeter]
"""
