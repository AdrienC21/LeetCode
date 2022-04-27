class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = []
        track = 0
        for i in range(1, n):
            res.append(-i)
            track -= i
        res.append(-track)
        return res