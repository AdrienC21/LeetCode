class Solution:
    # NOT MINE
    # O(V+E) time, O(V+E) space
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        answer = n * [0]
        count = n * [1]
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def postorder(u, parent=None):
            for v in graph[u]:
                if v == parent:
                    continue
                postorder(v, u)
                count[u] += count[v]
                answer[u] += answer[v] + count[v]

        def preorder(u, parent=None):
            for v in graph[u]:
                if v == parent:
                    continue
                answer[v] = answer[u] + n - 2 * count[v]
                preorder(v, u)

        postorder(0)
        preorder(0)
        return answer
