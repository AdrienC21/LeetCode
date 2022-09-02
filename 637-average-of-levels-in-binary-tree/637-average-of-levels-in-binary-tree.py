# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        to_visit = [root]
        res = []  # result
        while to_visit:
            total_sum = 0
            count = 0
            next_visit = []
            while to_visit:
                node = to_visit.pop()
                count += 1
                total_sum += node.val
                if node.left:
                    next_visit.append(node.left)
                if node.right:
                    next_visit.append(node.right)
            to_visit = next_visit
            res.append(total_sum / count)
        return res
