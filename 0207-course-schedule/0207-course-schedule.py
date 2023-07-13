class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        
        cycles = numCourses * [None]
        
        def hasCycle(i: int) -> bool:
            nonlocal graph, cycles
            
            if cycles[i] is not None:
                return cycles[i]
        
            cycles[i] = True
            for j in graph[i]:
                if hasCycle(j):
                    return True
            cycles[i] = False
            return False
    
        for i in range(numCourses):
            if hasCycle(i):
                return False
        return True
