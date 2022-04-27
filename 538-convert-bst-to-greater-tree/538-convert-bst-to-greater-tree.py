# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recMod(self, root: Optional[TreeNode], s: int) -> int:
        if root is None:
            return s
        s = self.recMod(root.right, s)
        s = s + root.val
        root.val = s
        s = self.recMod(root.left, s)
        return s

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = self.recMod(root, 0)
        return root