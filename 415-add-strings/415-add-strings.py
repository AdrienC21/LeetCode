class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            return self.addStrings(num2, num1)
        power = 1
        res = 0
        for i in range(len(num1)):
            res = res + (int(num1[-(i+1)]) + int(num2[-(i+1)])) * power
            power *= 10
        for i in range(len(num1), len(num2)):
            res = res + int(num2[-(i+1)]) * power
            power *= 10
        return str(res)