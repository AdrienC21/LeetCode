class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        Group cycles together, then sort the cycles
        """
        n = len(s)
        parent = [i for i in range(n)]
        
        def get_parent(i):  # get the cycle of an index
            if parent[i] != i:
                parent[i] = get_parent(parent[i])
            return parent[i]
        
        def group_in_cycle(i, j):  # when there is a pair, group the indexes in a cycle
            par_i = get_parent(i)
            par_j = get_parent(j)
            parent[par_j] = par_i
        
        for i, j in pairs:
            group_in_cycle(i, j)
        
        cycles = [[] for _ in range(n)]
        for i in range(n):
            cycle_i = get_parent(i)
            cycles[cycle_i].append((i, s[i]))
        
        final_string = ["" for _ in range(n)]
        
        # process the cycles in order, for each cycle, the min letters go first
        for cycle in cycles:
            cycle_positions = [c[0] for c in cycle]
            cycle_letters = [c[1] for c in cycle]
            cycle_letters.sort()  # min letters first
            
            for i, pos in enumerate(cycle_positions):
                final_string[pos] = cycle_letters[i]
        
        return "".join(final_string)