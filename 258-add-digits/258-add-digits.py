class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif (num % 10) == num:
            return num
        else:
            L = list(str(num))
            return  self.addDigits(reduce(lambda x,y: int(x) + int(y), L))