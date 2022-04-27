class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Minimum Spanning Tree ! Let's use Prim's algorithm (Kruskal works too)
        """
        
        # Create the graph
        V = len(points)  # number verticies
        graph = [[0 for _ in range(V)] for _ in range(V)]
        for i in range(V-1):
            for j in range(i+1, V):
                # manhattan distance
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[j][i] = dist
                graph[i][j] = dist

        key = V * [10**7]  # lengths to all node of min spanning tree
        parent = V * [None]  # store the minimum spanning Tree
        inSpanningTree = V * [False]  # is in spanning tree
 
        # first node selected will be 0
        parent[0] = -1  # 0 no parent
        key[0] = 0  # dist to spanning tree equal to 0 (to pick 0 first)
        
        for _ in range(V):  # select all vertices (V)
            
            # select edge with min distance to the spanning tree
            u = 0
            min_dist = 10**7
            for v in range(V):
                if (key[v] < min_dist) and not(inSpanningTree[v]):
                    u = v
                    min_dist = key[v]
            
            inSpanningTree[u] = True  # add the min vertex
            
            for v in range(V):
                
                # edge if distance > 0, connect if not already in spanning tree
                # by checking key[v] > graph[u][v], we update the distance of 
                if (graph[u][v] > 0) and not(inSpanningTree[v]) and (key[v] > graph[u][v]):
                    key[v] = graph[u][v]
                    parent[v] = u
        
        # sum the V-1 edges
        res = 0
        for v in range(1, V):
            res += graph[v][parent[v]]
        return res