class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        elif n == 1:
            return True
        elif n == 0:
            return False
        elif n < 1:
            return self.isPowerOfTwo(1 / n)
        else:
            d = n / 2
            if int(d) != d:
                return False
            return self.isPowerOfTwo(int(d))