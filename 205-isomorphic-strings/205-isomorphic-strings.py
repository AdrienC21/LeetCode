class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        hashset_rev = set()  # set of seen letters in t
        for c1, c2 in zip(s, t):
            if c1 in hashmap:
                if hashmap[c1] != c2:  # c1 has already been paired
                    return False
            else:
                if c2 in hashset_rev:
                    return False
                hashset_rev.add(c2)
                hashmap[c1] = c2
        return True