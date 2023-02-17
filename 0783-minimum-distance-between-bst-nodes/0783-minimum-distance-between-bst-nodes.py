# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []

        def recSearch(root: Optional[TreeNode]) -> None:
            nonlocal values

            if not(root):
                return
            values.append(root.val)
            recSearch(root.left)
            recSearch(root.right)

        recSearch(root)
        values.sort()
        res = sys.maxsize
        for i in range(len(values)-1):
            if (values[i+1] - values[i]) < res:
                res = values[i+1] - values[i]
        return res

