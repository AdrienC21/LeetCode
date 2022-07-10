class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)  # add the top floor
        n = len(cost)
        d = deque([n-1])  # for every i, store the reacheable position (here within two steps) with the lowest cumulative cost
        for i in range(n-2, -1, -1):
            if (d[0] - i) > 2:  # max two steps
                d.popleft()
            cost[i] += cost[d[0]]
            while d and cost[d[-1]] >= cost[i]:
                d.pop()
            d.append(i)
        return min(cost[0], cost[1])
