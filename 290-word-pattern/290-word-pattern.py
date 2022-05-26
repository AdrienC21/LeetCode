class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        L = s.split(" ")
        if len(L) != len(pattern):
            return False
        hashmap = {}
        hashmap_inv = {}
        for i, c in enumerate(pattern):
            if c in hashmap:
                if L[i] != hashmap[c]:
                    return False
            else:
                if (L[i] in hashmap_inv) and (hashmap_inv[L[i]] != c):
                    return False
                hashmap[c] = L[i]
                hashmap_inv[L[i]] = c
        return True
