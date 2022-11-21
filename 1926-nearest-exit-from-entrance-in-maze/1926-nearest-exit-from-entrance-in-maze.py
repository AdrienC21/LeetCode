class Solution:
    # spread from the entrance using a deque is better
    # O(mn)
    def add_tuple(self, u: tuple, v: tuple) -> tuple:
        return (u[0] + v[0], u[1] + v[1])
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        d = deque()
        d.append((entrance[0], entrance[1]))
        seen = set()
        seen.add((entrance[0], entrance[1]))
        res = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while d:
            res += 1
            for _ in range(len(d)):  # process the entire deque at time t
                (x, y) = d.popleft()
                # add unseen cells for t+1
                for k in directions:
                    x2, y2 = self.add_tuple((x, y), k)
                    if (x2 >= 0) and (x2 < m) and (y2 >= 0) and (y2 < n) and ((x2, y2) not in seen) and (maze[x2][y2] == '.'):
                        if (x2 == 0) or (x2 == (m-1)) or (y2 == 0) or (y2 == (n-1)):
                            return res
                        d.append((x2, y2))
                        seen.add((x2, y2))
        return -1

    # Djisktra: TLE ...
    # O(|E| + |V|log(|V|)) approx O(mn log(mn))
    """
    # unseen node with shortest distance to the entrance
    # for djisktra
    def min_distance(self, graph: dict, distances: dict, visited: set):

        # initialization
        m = sys.maxsize

        # search nearest node
        for v in graph.keys():
            if ((distances[v] < m) and (v not in visited)):
                m = distances[v]
                min_coord = v
        return min_coord

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        graph = defaultdict(list)
        m = len(maze)
        n = len(maze[0])
        # create a graph starting from entrance
        seen = set()
        to_visit = [tuple(entrance)]
        while to_visit:
            u = to_visit.pop()
            if u not in seen:
                seen.add(u)
                # if exit and != entrance, link the coordinate to the node "exit"
                if ((u[0] == 0) or (u[0] == (m-1)) or (u[1] == 0) or (u[1] == (n-1))) and (u != tuple(entrance)):
                    graph[u].append("exit")
                    graph["exit"].append(u)
                # connect with neighbors that are not walls
                for k in (-1, 1):
                    if ((u[0] + k) >= 0) and ((u[0] + k) < m) and (maze[u[0] + k][u[1]] == '.') and ((u[0] + k, u[1]) not in seen):
                        to_visit.append((u[0]+k,u[1]))
                        graph[u].append((u[0]+k,u[1]))
                        graph[(u[0]+k,u[1])].append(u)
                    if ((u[1] + k) >= 0) and ((u[1] + k) < n) and (maze[u[0]][u[1] + k] == '.') and ((u[0], u[1] + k) not in seen):
                        to_visit.append((u[0],u[1]+k))
                        graph[u].append((u[0],u[1]+k))
                        graph[(u[0],u[1]+k)].append(u)

        # djisktra shortest path from entrance to exit (if exists)
        distances = {u: sys.maxsize for u in graph.keys()}
        distances[tuple(entrance)] = 0
        visited = set()

        # djikstra
        for _ in range(len(graph)):
            # unseen node with shortest distance to the entrance
            u = self.min_distance(graph, distances, visited)
 
            # visit this node
            visited.add(u)
            # update for unseen neighbors their distance if it is lower
            for v in graph[u]:
                if ((v not in visited) and (distances[v] > distances[u] + 1)):
                    distances[v] = distances[u] + 1

        # if exit has been visited and distance != infinity
        # return distance to cell next to exit (so distances["exit"] - 1)
        return (distances["exit"] - 1) if (("exit" in distances) and (distances["exit"] != sys.maxsize)) else -1
    """
