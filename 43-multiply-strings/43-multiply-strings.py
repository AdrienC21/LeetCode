class Solution:
    def toInteger(self, n: str) -> int:
        res = int(n[0])
        for i in range(1, len(n)):
            res *= 10
            res += int(n[i])
        return res
    def multiply(self, num1: str, num2: str) -> str:
        n1 = self.toInteger(num1)
        n2 = self.toInteger(num2)
        return str(n1 * n2)