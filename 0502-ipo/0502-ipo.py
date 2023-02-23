class Solution:
    # Use heap for maximum efficiency
    # Not mine, I wanted to do DP initially ...
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profits_candidate = []
        projects = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(projects)  # sort by lowest capital first!
        
        for _ in range(k):
            while projects and (projects[0][0] <= w):  # we can afford this project
                c, p = heapq.heappop(projects)
                heapq.heappush(profits_candidate, -p)  # it's a min heap so -p to store the biggest value
            if not(profits_candidate):  # no candidate to pull, end of the pre-IPO
                break
            # else, increase capital by taking the biggest profit project available
            w += -heapq.heappop(profits_candidate)
        return w
