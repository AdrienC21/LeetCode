class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = defaultdict(int)
        for t in tasks:
            freq[t] += 1
        res = 0
        for t in freq:
            f = freq[t]
            if f == 1:
                return -1
            if f % 3 == 0:
                res += (f // 3)
            # if f % 3 == 2, packet of 3 and 1 of 2
            # else, packet of 3 and 2 packets of 2
            else:
                res += (f // 3) + 1
        return res
