class Solution:
    # Binary search
    def binarySearch(self, stack: List[int], k: int, l: int, elt: int) -> int:
        i = k
        j = l
        while i <= j:  # <=
            m = (i + j) // 2
            if stack[m] == elt:
                return m
            elif stack[m] > elt:
                j = m - 1
            else:
                i = m + 1
        return i  # i is the correct value to modify the stack at the right place
        
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        # old way with cmp
        from functools import cmp_to_key
        def doll_compare(x: List[int], y: List[int]) -> int:
            if x[0] == y[0]:
                return y[1] - x[1]
            else:
                return x[0] - y[0]
        key = cmp_to_key(doll_compare)
        envelopes.sort(key=key)
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))  # sort by width, then height decreasing if equality
        n = len(envelopes)
        res = 1
        stack = []
        stack.append(envelopes[0][1])
        for i in range(1, n):
            if (envelopes[i][1] > stack[-1]):
                stack.append(envelopes[i][1])
                res += 1
            else:
                j = self.binarySearch(stack, 0, len(stack)-1, envelopes[i][1])
                stack[j] = envelopes[i][1]
        return res
    # Solution dynamic programming: we search not for the higher dolls like the solution below, but for the dolls lower in hight than doll i. O(n^2)
    """
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: x[0])  # sort by width
        n = len(envelopes)
        res = 1
        dp = n * [0]
        dp[0] = 1
        for i in range(1, n):
            sub_res = 0
            for j in range(i):
                if (envelopes[j][0] < envelopes[i][0]) and (envelopes[j][1] < envelopes[i][1]):
                    sub_res = max(dp[j], sub_res)
            dp[i] = sub_res + 1
            res = max(dp[i], res)
        return res
    """
    # Dynamic programming, time limit exceeded
    """
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # sort by width
        envelopes.sort(key=lambda x: x[0])
        n = len(envelopes)
        # Dynamic programming
        dp = [-1 for _ in range(n)]
        dp[-1] = 1
        def recSearch(i):  # number of doll including the doll i
            nonlocal dp
            if dp[i] != -1:
                return dp[i]
            max_nb_doll = 0
            for j in range(i+1, n):  # search higher doll (among those having a larger width (start at i+1))
                if (envelopes[j][0] != envelopes[i][0]) and (envelopes[j][1] > envelopes[i][1]):  # width need to be different + higher dolls
                    max_nb_doll = max(max_nb_doll, recSearch(j))
            max_nb_doll += 1  # include doll i
            dp[i] = max_nb_doll
            return max_nb_doll
        for i in range(n):
            recSearch(i)
        return max(dp)
    """