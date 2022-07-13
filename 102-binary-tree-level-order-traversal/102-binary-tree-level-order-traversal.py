# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        to_visit = deque([(root, 0)])
        while to_visit:
            n, h = to_visit.popleft()
            if n:  # not None
                res.append((n.val, h))
                to_visit.append((n.left, h + 1))
                to_visit.append((n.right, h + 1))
        # then group nodes with same height
        new_res = []
        last_h = 0
        sub_list = []
        for (val, h) in res:
            if h == last_h:
                sub_list.append(val)
            else:
                new_res.append(sub_list)
                last_h = h
                sub_list = [val]
        if sub_list:
            new_res.append(sub_list)
        return new_res
