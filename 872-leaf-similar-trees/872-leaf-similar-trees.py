# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leaf(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def recSearch(root: Optional[TreeNode]) -> None:
            nonlocal res
            if not(root):
                return
            recSearch(root.left)
            if not(root.left) and not(root.right):
                res.append(root.val)
            recSearch(root.right)
        recSearch(root)
        return res

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = self.leaf(root1)
        l2 = self.leaf(root2)
        return l1 == l2
