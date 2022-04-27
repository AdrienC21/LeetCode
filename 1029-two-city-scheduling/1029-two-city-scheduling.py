class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs2 = []
        for i, c in enumerate(costs):
            costs2.append([c[0], c[1] , c[1] - c[0]])
        costs2.sort(key=lambda x: x[2])
        tot_cost = 0
        n = len(costs2)
        for i, c in enumerate(costs2):
            if i < (n // 2):
                tot_cost += c[1]
            else:
                tot_cost += c[0]
        return tot_cost