from collections import defaultdict
class Solution:
    def predecessor(self, u: str, v: str, size: int) -> bool:
        # predecessor if only one difference
        difference = 0
        i = 0  # pointer in u
        j = 0  # pointer in v
        while (i < size) and (j < (size + 1)) and (difference < 2):  # u length: size, v: size+1
            if u[i] != v[j]:
                difference += 1
                j += 1
            else:
                i += 1
                j += 1
        if i == j:
            difference += 1  # last character of v
        return (difference == 1)

    def longestStrChain(self, words: List[str]) -> int:
        sizes = defaultdict(list)
        for w in words:  # group words by sizes
            sizes[len(w)].append(w)
        graph = defaultdict(list)
        for size in list(sizes.keys()):  # convert fix list object. else error "dictionary changed size during iteration"
            for u in sizes[size]:
                for v in sizes[size+1]:  # if u predecesor of v, add an edge
                    if self.predecessor(u, v, size):
                        graph[u].append(v)
        # then dfs to obtain the maximum depth
        depths = defaultdict(int)
        def visit(u: str) -> None:
            nonlocal graph, depths
            if u not in depths:
                depth = 0
                for v in graph[u]:
                    visit(v)
                    depth = max(depth, depths[v])
                depths[u] = depth + 1

        max_depth = 1  # initialize at 1 (a single word is a link)
        for u in list(graph.keys()):
            if u not in depths:
                visit(u)
            max_depth = max(max_depth, depths[u])
        return max_depth
