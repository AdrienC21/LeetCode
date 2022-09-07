# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def recSearch(root: Optional[TreeNode]) -> str:
            if (root.left is None) and (root.right is None):
                return f"{root.val}"
            if root.right is None:
                return f"{root.val}({recSearch(root.left)})"
            if root.left is None:
                return f"{root.val}()({recSearch(root.right)})"
            return f"{root.val}({recSearch(root.left)})({recSearch(root.right)})"
        return recSearch(root)
