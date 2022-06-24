import heapq
class Solution:
    # clever idea: let N be the biggest element of the array
    # [n1, ..., nk, N] to be formed, then the operations was:
    # N = prev_N + n1 + .... + nk
    # while prev_N > sum(n1, ..., nk), repeat!
    # insert back into a max heap to access the biggest element fast!
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)
        target = [-x for x in target]
        if n == 1:
            return -target[0] == 1
        heapq.heapify(target)
        while True:
            m = -heapq.heappop(target)
            if m == 1:  # biggest element 1, so all values equal to 1, return True
                return True
            rest = -sum(target)
            if (m <= rest) or ((rest != 1) and ((m % rest) == 0)):
                return False
            heapq.heappush(target, -(m % rest))
