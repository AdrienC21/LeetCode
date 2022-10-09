# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        possibilities = set()
        def recSearch(root):
            nonlocal possibilities, k
            if not(root):
                return False
            if root.val in possibilities:
                return True
            possibilities.add(k-root.val)
            return recSearch(root.left) or recSearch(root.right)
        return recSearch(root)
