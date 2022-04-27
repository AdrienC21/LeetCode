class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        elif n < 1:
            return self.isPowerOfFour(1 / n)
        else:
            d = n / 4
            if int(d) != d:
                return False
            return self.isPowerOfFour(int(d))