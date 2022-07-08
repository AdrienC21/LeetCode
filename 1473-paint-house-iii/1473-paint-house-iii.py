import sys
class Solution:
    # iteratively modify all the solutions while we paint the houses
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = {(0, 0): 0}  # (target, last color): cost
        for i, color_i in enumerate(houses):
            new_dp = {}
            colors = range(color_i, color_i+1) if color_i else range(1, n+1)  # check if already painted
            for color in colors:  # try to paint all colours
                for j, k in dp:  # for each solutions for houses 0:i-1
                    nj = j + (k != color)  # increase if we create a new neighborhood
                    if nj > target:
                        continue
                    new_dp[(nj, color)] = min(new_dp.get((nj, color),
                                                         sys.maxsize),
                                              dp[j, k] + (cost[i][color-1] if color != color_i else 0))
            dp = new_dp
        possible_costs = [dp[j, k] for j, k in dp if j == target]  # cost where target has been reached
        if not(possible_costs):  # else return -1
            possible_costs = [-1]
        return min(possible_costs)

    # solution: it works, but TLE on an extreme case
    """
import sys
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        min_cost = sys.maxsize
        def recSearch(i: int, target: int, current_cost: int):
            nonlocal min_cost
            if target < 0:  # too much neighborhoods
                return
            if i == m:  # we painted all the houses
                if target == 0:  # initial cost is 0
                    min_cost = min(min_cost, current_cost)
                    return
                # not enough neighborhood, do nothing
                return
            # still some houses to paint
            if target == 0:  # no more possible neighborhood, color is forced
                prev_color = houses[i-1]
                if houses[i] and (houses[i] != prev_color):  # if house already painted and decrease target
                    return
                if houses[i]:  # house part of last neighborhood and painted
                    recSearch(i+1, target, current_cost)
                    return
                # paint the house
                houses[i] = prev_color
                recSearch(i+1, target, current_cost + cost[i][prev_color-1])
                houses[i] = 0
                return
            else:
                if i == 0:
                    prev_color = 0
                else:
                    prev_color = houses[i-1]
                if houses[i] and (houses[i] != prev_color):  # if house already painted and decrease target
                    recSearch(i+1, target-1, current_cost)
                    return
                if houses[i]:  # house part of last neighborhood and painted
                    recSearch(i+1, target, current_cost)
                    return
                # paint the house
                for color in range(1, n+1):
                    houses[i] = color
                    dicrease_target = 1 if (prev_color != color) else 0
                    recSearch(i+1, target-dicrease_target, current_cost + cost[i][color-1])
                houses[i] = 0
                return
        recSearch(0, target, 0)
        if min_cost == sys.maxsize:
            return -1
        return min_cost
    """
