class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res = []
        eis = []  # end increasing subseqs, of length i+1 at pos i

        for obstacle in obstacles:
            if not(eis) or (obstacle >= eis[-1]):
                eis.append(obstacle)
                res.append(len(eis))
            else:
                # find pos
                pos = bisect_right(eis, obstacle)
                eis[pos] = obstacle
                res.append(pos + 1)
        return res
