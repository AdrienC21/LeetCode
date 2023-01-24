class Solution:
    def solve(self, routes: dict, hasApple: List[bool], i: int, parent: int) -> int:
        cost = 0
        for child in routes[i]:
            if child != parent:
                cost += self.solve(routes, hasApple, child, i)
        
        if (i != 0) and hasApple[i]:
            hasApple[parent] = True
            return cost + 2
        return cost

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        routes = defaultdict(list)
        res = 0
        for k, v in edges:
            routes[k].append(v)
            routes[v].append(k)
            
        res = self.solve(routes, hasApple, 0, 0)
        return res
