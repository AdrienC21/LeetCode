from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        s = 1
        for nb in range(2, int(sqrt(num)+1)):
            if num % nb == 0:
                if (num // nb) == nb:
                    s += nb
                else:
                    s += (nb + (num // nb))
        return (s == num)