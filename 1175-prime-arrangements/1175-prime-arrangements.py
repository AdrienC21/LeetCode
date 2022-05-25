class Solution:
    def pi(self, n: int) -> int:
        if n <= 1:
            return 0
        count = 0
        for num in range(2, n+1):
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                count += 1
        return count
    
    def facto(self, n: int) -> int:
        res = 1
        for k in range(2, n+1):
            res *= k
        return res
    
    def numPrimeArrangements(self, n: int) -> int:
        pi_n = self.pi(n)
        res = self.facto(pi_n) * self.facto(n-pi_n)
        return res % ((10**9 + 7))
