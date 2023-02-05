class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        letters1 = set(p)
        letters2 = set(s)
        if letters1.difference(letters2):
            return []  # at least a letter of s1 is not in s2
        # counter frequency of letters in p
        counter = defaultdict(int)
        for l in p:
            counter[l] += 1
        # pointers
        i = 0
        j = 0
        # make a copy
        c = counter.copy()
        # result store all indices
        res = []
        # iterate
        while (i < len(s)) and (j < len(s)):
            if s[j] not in letters1:  # start to search anagram at j+1
                c = counter.copy()  # initialize the counter
                i = j + 1
                j = i
            elif not(c[s[j]]) and (s[i] == s[j]):  # move i and j
                del c[s[j]]
                i += 1
                j += 1
                if not(c):  # we placed all the letters of p, we found an anagram
                    res.append(i)
            elif not(c[s[j]]):  # shift i until we see s[j]
                del c[s[j]]
                while (i < j) and (s[i] != s[j]):
                    c[s[i]] += 1
                    i += 1
                if i != j:  # s[i] == s[j]
                    i += 1
                    j += 1
                else:
                    j += 1
                if not(c):  # we placed all the letters of p, we found an anagram
                    res.append(i)
            else:  # remove this letter from the permutation
                c[s[j]] -= 1
                if not(c[s[j]]):
                    del c[s[j]]
                j += 1
                if not(c):  # we placed all the letters of p, we found an anagram
                    res.append(i)
        if not(c):  # we placed all the letters of p, we found an anagram
            if i not in res:
                res.append(i)
        return res
