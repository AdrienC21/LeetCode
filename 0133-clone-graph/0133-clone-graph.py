"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mapping = {}

        def recClone(node: 'Node') -> 'Node':
            nonlocal mapping

            if node in mapping:
                return mapping[node]
            new_node = Node(val=node.val)
            mapping[node] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(recClone(n))
            return new_node

        return recClone(node) if node else None
