# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 1
        def recSearch(root, max_val):
            nonlocal count
            if root.left:
                if root.left.val >= max_val:
                    count += 1
                recSearch(root.left, max(max_val, root.left.val))
            if root.right:
                if root.right.val >= max_val:
                    count += 1
                recSearch(root.right, max(max_val, root.right.val))
        recSearch(root, root.val)
        return count
