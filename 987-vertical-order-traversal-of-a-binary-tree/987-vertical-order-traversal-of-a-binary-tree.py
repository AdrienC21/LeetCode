# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from functools import cmp_to_key
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        def traversal(root, row, col):
            nonlocal d
            d[col].append((row, root.val))
            if root.left:
                traversal(root.left, row + 1, col - 1)
            if root.right:
                traversal(root.right, row + 1, col + 1)
        traversal(root, 0, 0)
        sorted_columns = sorted(list(d.keys()))
        res = []
        def cmp_func(x, y):
            if x[0] == y[0]:  # same row, compare value
                return -1 if (x[1] < y[1]) else 1
            return -1 if (x[0] < y[0]) else 1
        key = cmp_to_key(cmp_func)
        for col in sorted_columns:
            res.append([x[1] for x in sorted(d[col], key=key)])
        return res
