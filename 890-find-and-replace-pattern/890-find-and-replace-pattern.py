class Solution:
    def isSamePattern(self, word: str, pattern: str) -> bool:
        dic = {}
        inverse_dic = {}
        for i, c in enumerate(word):
            if c in dic:
                if dic[c] != pattern[i]:
                    return False
            elif pattern[i] in inverse_dic:
                if inverse_dic[pattern[i]] != c:
                    return False
            else:
                dic[c] = pattern[i]
                inverse_dic[pattern[i]] = c
        return True
                
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for w in words:
            if self.isSamePattern(w, pattern):
                res.append(w)
        return res
