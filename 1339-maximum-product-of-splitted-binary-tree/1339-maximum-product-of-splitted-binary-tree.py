# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # transform val in (val, sub of subtree)
        def modTree(root):
            if not(root):
                return 0
            if isinstance(root.val, tuple):
                return root.val[1]
            l = modTree(root.left)
            r = modTree(root.right)
            root.val = (root.val, l + r + root.val)
            return root.val[1]

        modTree(root)
        max_prod = -sys.maxsize
        tot_sum = root.val[1]

        def recSearch(root):
            nonlocal max_prod, tot_sum
            if not(root):
                return
            if root.left:
                # delete edge in left subtree
                recSearch(root.left)
                # delete left edge
                max_prod = max(max_prod, root.left.val[1] * (tot_sum - root.left.val[1]))
            if root.right:
                # delete edge in right subtree
                recSearch(root.right)
                # delete right edge
                max_prod = max(max_prod, root.right.val[1] * (tot_sum - root.right.val[1]))

        recSearch(root)
        return max_prod % (10**9 + 7)
