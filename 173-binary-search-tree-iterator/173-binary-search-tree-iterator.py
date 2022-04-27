# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.L = []
        n = root
        while n:
            self.L.append(n)
            n = n.left

    def next(self) -> int:
        n = self.L[-1].right
        last = self.L.pop()
        while n:
            self.L.append(n)
            n = n.left   
        return last.val
        
    def hasNext(self) -> bool:
        return len(self.L) >= 1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()