class Solution:
    def is_permutation(self, s1: str, s2: str, m: int) -> bool:
        count_diff = 0
        for i in range(m):
            if s1[i] != s2[i]:
                if count_diff > 1:
                    return False
                if count_diff == 1:
                    # check if permutation works
                    if (s1[i] != c2) or (s2[i] != c1):
                        return False
                    count_diff += 1
                else:
                    count_diff += 1
                    c1 = s1[i]
                    c2 = s2[i]
        return True  # words are equal
        
    def numSimilarGroups(self, strs: List[str]) -> int:
        # no need for the step below, all words are anagram already
        """
        # group first words with the same characters freq
        precluster = defaultdict(list)
        counters = []
        i = 0
        for s in strs:
            c = Counter(s)
            for id_counter, counter in counters:
                if c == counter:
                    precluster[cluster_id].append(s)
                    break
            else:
                counters.append((i, c))
                precluster[i].append(s)
                i += 1
        # pre cluster, create a graph with edge if two words are letter permutation
        """
        # create a graph with edge if two words are letter permutation
        graph = defaultdict(list)
        n = len(strs)
        m = len(strs[0])
        for u in range(n-1):
            for v in range(u+1, n):
                if self.is_permutation(strs[u], strs[v], m):
                    graph[u].append(v)
                    graph[v].append(u)
        
        # count connexe components of the graph
        res = 0
        visited = [False for _ in range(n)]

        def dfs(u: int) -> None:
            nonlocal visited, graph
            if visited[u]:
                return
            # else, explore
            visited[u] = True
            for v in graph[u]:
                if not(visited[v]):
                    dfs(v)
            return

        for u in range(n):
            if not(visited[u]):
                res += 1
                dfs(u)
                
        return res
