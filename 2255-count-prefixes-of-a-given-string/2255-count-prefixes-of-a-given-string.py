class Solution:
    def isPrefix(self, word: str, s: str) -> bool:
        n = len(word)
        if n > len(s):
            return False
        for i in range(n):
            if word[i] != s[i]:
                return False
        return True
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            if self.isPrefix(word, s):
                count += 1
        return count