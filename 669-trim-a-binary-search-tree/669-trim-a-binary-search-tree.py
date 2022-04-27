# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        elif root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val == low:
            return TreeNode(val=root.val, left=None, right=self.trimBST(root.right, low, high))
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        elif root.val == high:
            return TreeNode(val=root.val, left=self.trimBST(root.left, low, high), right=None)
        else:
            return TreeNode(val=root.val, left=self.trimBST(root.left, low, high), right=self.trimBST(root.right, low, high))