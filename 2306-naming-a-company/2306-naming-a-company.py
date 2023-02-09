class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        hashmap = defaultdict(set)
        for idea in ideas:
            hashmap[idea[0]].add(idea[1:])
        
        res = 0
        for l1 in hashmap:
            for l2 in hashmap:
                if l1 == l2:  # we want different letters
                    continue
                count = 0
                for w in hashmap[l1]:
                    if w in hashmap[l2]:
                        count += 1
                res += (len(hashmap[l1]) - count) * (len(hashmap[l2]) - count)
        return res

    # TLE
    """
    def distinctNames(self, ideas: List[str]) -> int:
        set_ideas = set(ideas)
        n = len(ideas)
        names = set()
        for i in range(n):
            ideaA = ideas[i][1:]
            for j in range(n):
                ideaB = ideas[j][1:]
                if ((ideas[j][0] + ideaA) not in set_ideas) and ((ideas[i][0] + ideaB) not in set_ideas):
                    names.add(ideas[i][0] + ideaB + " " + ideas[j][0] + ideaA)
        return len(names)
    """
