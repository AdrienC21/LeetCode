class Solution:
    def recSqrt(self, left: int, right: int, x: int):
        if left == right:
            return left
        elif left == (right - 1):
            if (right * right) == x:
                return right
            return left
        else:
            m = (left + right) // 2
            s = m * m
            if s == x:
                return m
            elif s > x:
                return self.recSqrt(left, m, x)
            else:
                return self.recSqrt(m, right, x)
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        return self.recSqrt(1, x, x)