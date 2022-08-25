class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n < 1:
            return self.isPowerOfThree(1 / n)
        a = n / 3
        if int(a) != a:
            return False
        return self.isPowerOfThree(int(a))
