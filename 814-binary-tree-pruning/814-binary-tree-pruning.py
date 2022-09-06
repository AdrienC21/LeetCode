# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recSearch(root: Optional[TreeNode]):
            if (root.left is None) and (root.right is None):
                return (root.val == 1)
            res_left = False
            res_right = False
            if root.left:
                res_left = recSearch(root.left)
                if not(res_left):
                    root.left = None
            if root.right:
                res_right = recSearch(root.right)
                if not(res_right):
                    root.right = None
            return res_left or res_right or (root.val == 1)
        res = recSearch(root)
        if res:
            return root
        return None
