class Solution:
    
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        s = set()
        candidates.sort()

        def recSearch(candidates: List[int], target: int) -> List[List[int]]:
        
            if not(candidates):
                return []
            if candidates[0] > target:
                return []
            if candidates[0] == target:
                return [[target]]
            if candidates[-1] > target:
                return recSearch(candidates[:-1], target)
            if candidates[-1] == target:
                return [[target]] + recSearch(candidates[:-1], target)
            subres = recSearch(candidates[1:], target-candidates[0]) + recSearch(candidates, target-candidates[0])
            for i in range(len(subres)):
                subres[i].append(candidates[0])
            return subres + recSearch(candidates[1:], target)
        
        L = recSearch(candidates, target)
        for elt in L:
            s.add(tuple(elt))
        res = []
        for t in s:
            res.append(list(t))
        return res