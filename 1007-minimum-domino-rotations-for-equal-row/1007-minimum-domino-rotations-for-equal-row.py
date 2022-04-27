import numpy as np
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        val1 = tops[0]
        val2 = bottoms[0]
        if val1 != val2:
            sol = {"v1top": 0, "v1down": 1, "v2top": 1, "v2down": 0}
        else:
            sol = {"v1top": 0, "v1down": 0, "v2top": -np.inf, "v2down": -np.inf}
        for i in range(1, len(tops)):
            ti = tops[i]
            bi = bottoms[i]
            if ti == bi:
                if ti == val1:
                    sol["v2top"] = -np.inf
                    sol["v2down"] = -np.inf
                elif ti == val2:
                    sol["v1top"] = -np.inf
                    sol["v1down"] = -np.inf
                else:
                    sol["v1top"] = -1
                    break
            else:
                if (ti != val1) and (ti != val2) and (bi != val1) and (bi != val2):
                    sol["v1top"] = -1
                    break
                if (val1 != ti) and (val1 != bi):
                    sol["v1top"] = -np.inf
                    sol["v1down"] = -np.inf
                if (val2 != ti) and (val2 != bi):
                    sol["v2top"] = -np.inf
                    sol["v2down"] = -np.inf                
                if ti == val1:
                    sol["v1down"] += 1
                elif ti == val2:
                    sol["v2down"] += 1
                if bi == val1:
                    sol["v1top"] += 1
                elif bi == val2:
                    sol["v2top"] += 1
                
        res = np.inf
        for (k, val) in sol.items():
            if val == -1:
                return -1
            if val != -np.inf:
                res = min(res, val)
        if res == np.inf:
            return -1
        return res