# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recSearch(self, root: Optional[TreeNode], min_val: int, max_val: int):
        if not(root):
            return max_val - min_val
        max_val = max(max_val, root.val)
        min_val = min(min_val, root.val)
        return max(self.recSearch(root.left, min_val, max_val), self.recSearch(root.right, min_val, max_val))
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.recSearch(root, root.val, root.val)
