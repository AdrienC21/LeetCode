"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:                
    def connect(self, root: 'Node') -> 'Node':
        initialRoot = root  # to be returned at the end
        
        # child and child head to update everything from left to right, depth by depth
        while root:  # will be evaluate at root.next at the end until we reach the end
            child = None
            childHead = None
            while root:
                if root.left:
                    if childHead is None:  # initialize childHead and child
                        childHead = root.left
                        child = root.left
                    else:
                        child.next = root.left
                        child = child.next  # move child to the right
                if root.right:
                    if childHead is None:  # initialize childHead and child
                        childHead = root.right
                        child = root.right
                    else:
                        child.next = root.right
                        child = child.next  # move child to the right
                # we attributed the value left and right of the root, now move root to the right
                root = root.next
            # we finished attributing next at this depth, move under
            root = childHead
        return initialRoot