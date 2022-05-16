from functools import reduce
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        L = []
        max_len = reduce(min, map(lambda s: len(s), strs))
        for i in range(max_len):
            c = strs[0][i]
            allSame = True
            for w in strs[1:]:
                if w[i] != c:
                    allSame = False
                    break
            if allSame:
                L.append(c)
            else:
                break
        return "".join(L)