# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sym(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if (r1 is None) and (r2 is None):
            return True
        if (r1 is None) or (r2 is None):
            return False
        if r1.val != r2.val:
            return False
        return self.sym(r1.left, r2.right) and self.sym(r1.right, r2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.sym(root.left, root.right)
