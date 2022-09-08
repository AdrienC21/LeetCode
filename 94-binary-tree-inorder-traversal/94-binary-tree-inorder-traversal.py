# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not(root):
            return []
        if (root.left is None) and (root.right is None):
            return [root.val]
        if root.left is None:
            res = [root.val]
            res.extend(self.inorderTraversal(root.right))
            return res
        if root.right is None:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            return res
        res = self.inorderTraversal(root.left)
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res
