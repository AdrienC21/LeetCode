# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:      
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        d = deque()
        lend = 0
        
        def sortd() -> None:
            nonlocal d
            nonlocal lend
            i = lend - 1
            while (i > 0) and (d[i] < d[i-1]):
                d[i], d[i-1] = d[i-1], d[i]
                i -= 1
            
        def recSearch(root: Optional[TreeNode]) -> None:
            nonlocal d
            nonlocal lend
            nonlocal k
            if root is None:
                return
            if lend < k:
                d.append(root.val)
                lend += 1
                sortd()
            elif d[lend-1] > root.val:
                d.pop()
                d.append(root.val)
                sortd()
            recSearch(root.left)
            recSearch(root.right)
            
        recSearch(root)
        return d[k-1]