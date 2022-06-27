class Solution:
    # even faster, using max directly ...
    def minPartitions(self, n: str) -> int:
        return max(n)
    # reduce and map
    """
from functools import reduce
    def minPartitions(self, n: str) -> int:
        return reduce(max, map(int, list(n)))
    """
    
    # Solution with a deque. Remove maximum amount of digits (deci-binary with as many 1s as possible) and remove trailing zeros potentialy created
    """
from collections import deque
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
    """
