# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.stack1 = []
        if root:  # if not None
            self.stack1.append(root)
        self.stack2 = []
        res = []  # result
        while self.stack1:
            # bfs
            for node in self.stack1:
                if node.left:
                    self.stack2.append(node.left)
                if node.right:
                    self.stack2.append(node.right)
            # extract rightmost element of stack1
            res.append(self.stack1[-1].val)
            # stack1 is stack2
            self.stack1 = self.stack2[:]
            self.stack2.clear()
        return res
