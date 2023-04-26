class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num < 10:
            return num
        L = list(str(num))
        return self.addDigits(reduce(lambda x, y: int(x) + int(y), L))
