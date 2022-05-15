# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def recMaxDepth(root, depth):
            m = depth  # maximum
            if root:
                if root.left:
                    m = max(m, recMaxDepth(root.left, depth+1))
                if root.right:
                    m = max(m, recMaxDepth(root.right, depth+1))  
            return m
        max_depth = recMaxDepth(root, 0)
                    
        res = 0
        def recSearch(root, depth):
            nonlocal res, max_depth
            if root:
                if not(root.left) and not(root.right) and (depth == max_depth):
                    res += root.val
                recSearch(root.left, depth+1)
                recSearch(root.right, depth+1)
        recSearch(root, 0)
        return res