class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        m = len(mat)
        n = len(mat[0])
        direction = "up"
        for k in range(min(m, n)):
            for j in range(k+1):
                if direction == "up":
                    coord = (k-j, j)
                else:
                    coord = (j, k-j)
                res.append(mat[coord[0]][coord[1]])
            # change direction
            direction = "up" if direction == "down" else "down"
        k = min(m, n) - 1
        for l in range(max(m, n) - min(m, n)):  # extra large diagonal for rectangle matrix
            for j in range(k+1):
                if direction == "up":
                    if m > n:
                        coord = (k-j+l+1, j)
                    else:
                        coord = (k-j, j+l+1)
                else:
                    if m > n:
                        coord = (j+l+1, k-j)
                    else:
                        coord = (j, k-j+l+1)
                res.append(mat[coord[0]][coord[1]])
            # change direction
            direction = "up" if direction == "down" else "down"
        # l = max(m, n) - min(m, n)
        for k in range(min(m, n)-2, -1, -1):
            for j in range(k+1):
                if direction == "up":
                    coord = (m-1-j, n-1-k+j)
                else:
                    coord = (m-1-k+j, n-1-j)
                res.append(mat[coord[0]][coord[1]])
            # change direction
            direction = "up" if direction == "down" else "down"
        return res