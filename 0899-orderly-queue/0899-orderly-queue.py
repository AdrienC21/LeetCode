class Solution:
    # the theory: k > 1, always sort, otherwise, try all combination (n)
    # complexity: O(n)
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(list(s)))
        n = len(s)
        res = s
        for _ in range(n-1):
            s = s[1:] + s[0]
            res = min(res, s)
        return res
    # better with a queue, but still TLE ...
    """
    from collections import OrderedDict
    def orderlyQueue(self, s: str, k: int) -> str:
        n = len(s)
        if k > (n // 2):  # we can sort the string
            return "".join(sorted(list(s)))
        seen = set([s])
        heap = []
        heapq.heapify(heap)
        q = deque()
        q.append(s)
        while q:
            string = q.pop()
            for i in range(k):
                new_word = string[:i] + string[i+1:] + string[i]
                if new_word not in seen:
                    seen.add(new_word)
                    heapq.heappush(heap, new_word)
                    q.append(new_word)
        return heapq.heappop(heap)
    """
    # TLE ...
    """
    def orderlyQueue(self, s: str, k: int) -> str:
        h = [s]
        heapq.heapify(h)
        seen = set([s])
        n = len(s)
        for _ in range(n):
            L = list(h)
            for w in L:
                for j in range(k):
                    new_word = w[:j] + w[j+1:] + w[j]
                    if new_word not in seen:
                        seen.add(new_word)
                        heapq.heappush(h, new_word)
        return heapq.heappop(h)
    """
