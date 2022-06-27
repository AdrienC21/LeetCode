from collections import deque
class Solution:
    def minPartitions(self, n: str) -> int:
        d = deque()
        for c in n:
            d.append(int(c))
        steps = 0
        while d:
            # decrase integers by 1
            for i, num in enumerate(d):
                if num != 0:
                    d[i] = num - 1
            # remove trailing zeros
            while d and not(d[0]):
                d.popleft()
            steps += 1
        return steps
