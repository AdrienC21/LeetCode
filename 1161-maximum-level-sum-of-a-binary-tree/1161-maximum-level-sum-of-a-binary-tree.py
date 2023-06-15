from functools import cmp_to_key


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = []
        to_visit = [root]
        current_level = 0
        current_sum = 0
        while to_visit:
            current_level += 1  # new level
            current_sum = 0  # sum for this level
            new_to_visit = []  # collect node for the next level
            for node in to_visit:
                current_sum += node.val
                if node.left is not None:
                    new_to_visit.append(node.left)
                if node.right is not None:
                    new_to_visit.append(node.right)
            sums.append([current_sum, current_level])  # add the sum
            to_visit = new_to_visit[:]  # update to_visit
        # sort by biggest sum and then smallest level
        def custom_cmp(a: List[int], b: List[int]) -> int:
            if a[0] == b[0]:
                if a[1] < b[1]:
                    return 1
                return -1
            if a[0] > b[0]:
                return 1
            return -1
        custom_key = cmp_to_key(custom_cmp)
        sums.sort(key=custom_key, reverse=True)
        return sums[0][1]
