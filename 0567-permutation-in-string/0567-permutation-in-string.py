class Solution:
    # O(n) with double pointers!
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters1 = set(s1)
        letters2 = set(s2)
        if letters1.difference(letters2):
            return False  # at least a letter of s1 is not in s2
        # counter frequency of letters ins 1
        counter = defaultdict(int)
        for l in s1:
            counter[l] += 1
        # pointers
        i = 0
        j = 0
        # make a copy
        c = counter.copy()
        # iterate
        while (i < len(s2)) and (j < len(s2)):
            if s2[j] not in letters1:  # start to search permutation at j+1
                c = counter.copy()  # initialize the counter
                i = j + 1
                j = i
            elif not(c[s2[j]]) and (s2[i] == s2[j]):  # move i and j
                del c[s2[j]]
                i += 1
                j += 1
            elif not(c[s2[j]]):  # shift i until we see s2[j]
                del c[s2[j]]
                while (i < j) and (s2[i] != s2[j]):
                    c[s2[i]] += 1
                    i += 1
                if i != j:  # s2[i] == s2[j]
                    i += 1
                    j += 1
                else:
                    j += 1
            else:  # remove this letter from the permutation
                c[s2[j]] -= 1
                if not(c[s2[j]]):
                    del c[s2[j]]
                j += 1
                if not(c):  # we placed all the letters of s1, we found a permutation
                    return True
        if not(c):  # we placed all the letters of s1, we found a permutation
            return True
        return False
