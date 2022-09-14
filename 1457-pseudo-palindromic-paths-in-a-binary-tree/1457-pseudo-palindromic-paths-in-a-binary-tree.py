# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isPalindromicPermu(self, freqs: List[int]) -> bool:
        nb_odds = 0
        for c in freqs:
            if c % 2 == 1:
                nb_odds += 1
                if nb_odds > 1:
                    break
        return (nb_odds <= 1)
        
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        freqs = 9 * [0]
        count = 0
        def recExplore(root):
            nonlocal count, freqs
            freqs[root.val-1] += 1
            if (root.left is None) and (root.right is None):  # it's a leaf
                if self.isPalindromicPermu(freqs):
                    count += 1
            if root.left:
                recExplore(root.left)
            if root.right:
                recExplore(root.right)
            freqs[root.val-1] -= 1
        recExplore(root)
        return count
