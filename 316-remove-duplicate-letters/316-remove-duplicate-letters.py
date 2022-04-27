class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        L = []  # stack
        seen = 26 * [False]
        last_ind = [-1 for _ in range(26)]
        ref = ord("a")
        for i, v in enumerate(s):
            last_ind[ord(v) - ref] = i
        for i, v in enumerate(s):
            if seen[ord(v)-ref]:
                continue
            while L and (L[-1] > v) and (i < last_ind[ord(L[-1])-ref]):
                seen[ord(L.pop())-ref] = False
            L.append(v)
            seen[ord(v)-ref] = True
                
        return "".join(L)