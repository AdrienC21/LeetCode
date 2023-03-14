# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def recSearch(root: Optional[TreeNode], current_nb: int) -> None:
            nonlocal res
            if root is None:
                return None
            new_nb = 10 * current_nb + root.val
            if (root.left is None) and (root.right is None):
                res += new_nb
                return None
            if root.left is None:
                recSearch(root.right, new_nb)
                return None
            if root.right is None:
                recSearch(root.left, new_nb)
                return None
            recSearch(root.left, new_nb)
            recSearch(root.right, new_nb)
                
        recSearch(root, 0)
        return res
