import heapq
class Solution:
    # priority queue solution
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = []
        u = 1  # first ugly number
        seen = set()
        seen.add(u)
        heapq.heappush(heap, u)
        found = 0  # ugly number found (start at 0)
        while found < n:
            u = heapq.heappop(heap)
            found += 1
            # add new ugly numbers
            for p in primes:
                if (p * u) not in seen:  # not already added in the heap
                    heapq.heappush(heap, p * u)
                    seen.add(p * u)
        return u
        
    # Naive solution, search all numbers in order. Time limit exceeded
    """
    def isUgly(self, n: int, primes: List[int]) -> bool:
        for p in primes:
            while (n % p) == 0:
                n = n // p
        return (n == 1)
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1
        n -= 1
        # n is number of Ugly number to find
        i = 2  # number to test
        while n > 0:
            if self.isUgly(i, primes):  # we found an ugly number
                n -= 1
            i += 1  # test next number
        i -= 1
        return i
    """