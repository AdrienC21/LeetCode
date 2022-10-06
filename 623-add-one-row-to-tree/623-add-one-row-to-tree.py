# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val, left=root)
        root = self.add(root, val, depth, "")
        return root
    def add(self, root: Optional[TreeNode], val: int, depth: int, direction: str) -> Optional[TreeNode]:
        if depth == 1:
            if not(root):
                return TreeNode(val=val)
            if direction == "left":
                return TreeNode(val=val, left=root)
            return TreeNode(val=val, right=root)
        if not(root):
            return None
        root.left = self.add(root.left, val, depth-1, direction="left")
        root.right = self.add(root.right, val, depth-1, direction="right")
        return root
 