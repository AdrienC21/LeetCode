"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    # not mine, not enough time ...
    def construct(self, grid: List[List[int]]) -> 'Node':
        def recSearch(n, r, c):
            all_same = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        all_same = False
                        break
            if all_same:
                return Node(grid[r][c], True)  # it's a leaf
            n = n // 2
            topLeft = recSearch(n, r, c)
            topRight = recSearch(n, r, c + n)
            bottomLeft = recSearch(n, r + n, c)
            bottomRight = recSearch(n, r + n, c + n)
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
        return recSearch(len(grid), 0, 0)
