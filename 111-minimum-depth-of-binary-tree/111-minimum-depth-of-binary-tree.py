# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            if root.left and root.right:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
            if root.left:
                return 1 + self.minDepth(root.left)
            if root.right:
                return 1 + self.minDepth(root.right)
            return 1
        return 0
