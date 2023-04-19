# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zz(self, root: Optional[TreeNode]):
        if root is None:
            return -1, -1, -1
        r_zz_left, _, r_max_zz = self.zz(root.right)
        zz_right = 1 + r_zz_left
        _, l_zz_right, l_max_zz = self.zz(root.left)
        zz_left = 1 + l_zz_right
        return zz_left, zz_right, max(r_max_zz, l_max_zz, zz_left, zz_right)
        
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        _, _, res = self.zz(root)
        return res
