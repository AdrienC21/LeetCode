class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n == 1:
            return x
        else:
            if (n % 2) == 0:
                a = self.myPow(x, n // 2)
                return a * a
            else:
                a = self.myPow(x, n // 2)
                return a * a * x