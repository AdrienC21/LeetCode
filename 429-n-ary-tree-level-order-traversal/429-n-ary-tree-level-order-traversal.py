"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        res = []
        def recSearch(L) -> None:
            nonlocal res
            new_L = []
            append_res = []
            for c in L:
                if c:
                    if c.children is not None:
                        new_L.extend(c.children)
                    append_res.append(c.val)
            res.append(append_res)
            if new_L:
                recSearch(new_L)
        recSearch([root])
        return res
