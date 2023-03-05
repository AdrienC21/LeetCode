class Solution:
    # not mine, adapted
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # group same values
        graph = defaultdict(list)
        for i, num in enumerate(arr):
            graph[num].append(i)
        res = 0
        q = deque([0])  # queue
        seen = set()
        seen.add(0)

        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if i == (n - 1):  # reach the end
                    return res
                seen.add(i)
                u = arr[i]
                if (i + 1) < n:  # add right pos to reachable position from u
                    graph[u].append(i + 1)
                if (i - 1) >= 0:  # add left pos to reachable position from u
                    graph[u].append(i - 1)
                for j in graph[u]:  # for all position
                    if j not in seen:  # if not seen
                        q.append(j)  # add position to the queue
                del graph[u]
            res += 1
        return res
