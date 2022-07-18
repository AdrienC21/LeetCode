from collections import defaultdict
class Solution:
    # not mine
    # use a hashmap and modifiy inplace the matrix with cumulative sum
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        count = 0
        m = len(matrix)
        n = len(matrix[0])
        d = defaultdict(int)
        for row in matrix:
            for j in range(1, n):
                row[j] += row[j-1]
        for j in range(n):
            for k in range(j, n):
                d.clear()
                d[0] = 1
                cum_sum = 0
                for i in range(m):
                    cum_sum += matrix[i][k] - (matrix[i][j-1] if j else 0)
                    count += d[cum_sum - target]
                    d[cum_sum] += 1
        return count
