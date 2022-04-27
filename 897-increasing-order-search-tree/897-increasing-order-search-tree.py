# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBSTdeque(self, root: TreeNode) -> TreeNode:
        if root is None:
            return deque()
        dleft = self.increasingBSTdeque(root.left)
        dright = self.increasingBSTdeque(root.right)
        d = deque()
        d.append(root.val)
        while dleft:
            d.appendleft(dleft.pop())
        while dright:
            d.append(dright.popleft())
        return d
            
    def increasingBST(self, root: TreeNode) -> TreeNode:
        d = self.increasingBSTdeque(root)
        t = None
        while d:
            t = TreeNode(val=d.pop(), right=t)
        return t