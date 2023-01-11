class Solution:
    def solve(self,routes,hasApple,idx,parent):
        cost=0
        for child in routes[idx]:
            if(child!=parent):
                cost+=self.solve(routes,hasApple,child,idx)
        
        if(idx!=0 and hasApple[idx]):
            hasApple[parent]=True
            return cost+2
        return cost
        
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        routes=collections.defaultdict(list)
        res=0
        for k,v in edges:
            routes[k].append(v)
            routes[v].append(k)
            
        res=self.solve(routes,hasApple,0,0)
        return res
