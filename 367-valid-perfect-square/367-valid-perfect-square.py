class Solution:
    def recSqrt(self, left: int, right: int, n: int) -> int:
        if left == right:
            return left
        elif left == (right - 1):
            if right * right == n:
                return right
            return left
        else:
            m = (left + right) // 2
            s = m * m
            if s == n:
                return m
            elif s > n:
                return self.recSqrt(left, m, n)
            else:
                return self.recSqrt(m, right, n)
    def customSqrt(self, n: int) -> int:
        if n <= 1:
            return n
        return self.recSqrt(1, n, n)
    def isPerfectSquare(self, num: int) -> bool:
        s = self.customSqrt(num)
        return ((s * s) == num)