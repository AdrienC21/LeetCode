class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        
        max_id = -1
        doubles = defaultdict(list)
        dic_id = {}
        for n in changed:
            if n in dic_id:
                i = dic_id[n]
                doubles[i].append(n)
            elif ((n / 2) == (n // 2)) and ((n // 2) in dic_id):
                i = dic_id[n//2]
                doubles[i].append(n)
                dic_id[n] = i
            elif (2 * n) in dic_id:
                i = dic_id[2*n]
                doubles[i].append(n)
                dic_id[n] = i
            else:
                max_id += 1
                doubles[max_id].append(n)
                dic_id[n] = max_id

        final_result = []
        for L in doubles.values():
            if len(L) % 2 != 0:
                return []
            freqs = defaultdict(int)
            for n in L:
                freqs[n] += 1
            sorted_nb = sorted(list(set(L)))
            
            # special case 0
            if not(sorted_nb[0]):
                sorted_nb = sorted_nb[1:]
                if freqs[0] % 2 != 0:
                    return []
                final_result.extend((freqs[0] // 2) * [0])

            for k in range(len(sorted_nb)-1):
                if freqs[sorted_nb[k]] > freqs[sorted_nb[k+1]]:
                    return []
                freqs[sorted_nb[k+1]] -= freqs[sorted_nb[k]]
                final_result.extend(freqs[sorted_nb[k]] * [sorted_nb[k]])
            if sorted_nb and (freqs[sorted_nb[-1]] != 0):
                return []
        return final_result
