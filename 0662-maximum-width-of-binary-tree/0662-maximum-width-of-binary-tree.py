# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = -sys.maxsize
        current_l = [(root, 0)]
        next_l = []
        while current_l:
            res = max(res, current_l[-1][1] - current_l[0][1] + 1)
            for (node, depth) in current_l:
                if node.left is not None:
                    next_l.append((node.left, 2*depth+1))
                if node.right is not None:
                    next_l.append((node.right, 2*depth+2))
            current_l = next_l[:]
            next_l = []
        return res
