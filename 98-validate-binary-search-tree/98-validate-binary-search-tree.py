# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def isValid(self, root: Optional[TreeNode], lower: Optional[int]=sys.maxsize, higher: Optional[int]=-sys.maxsize):
        if root:
            if (root.val >= lower) or (root.val <= higher):
                return False
            if root.left and not(self.isValid(root.left, min(lower, root.val), higher)):
                return False
            if root.right and not(self.isValid(root.right, lower, max(higher, root.val))):
                return False
        return True
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            return self.isValid(root)
        return True
