class Solution:
    def sort_rev(self, d: List[List[int]], size: int) -> None:
        for i in range(size-1, 0, -1):
            if d[i][1] < d[i-1][1]:
                d[i], d[i-1] = d[i-1], d[i]
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = []
        len_d = 0
        for i, r in enumerate(mat):
            score = 0
            for v in r:
                if v:
                    score += 1
                else:
                    break
            if len_d < k:
                d.append([i, score])
                len_d += 1
                self.sort_rev(d, len_d)
            else:
                if score < d[-1][1]:
                    d.pop()
                    d.append([i, score])
                    self.sort_rev(d, len_d)
        return map(lambda x: x[0], d)