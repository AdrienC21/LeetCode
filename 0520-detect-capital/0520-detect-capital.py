class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper():
            return all(c.isupper() for c in word) or all(c.islower() for c in word[1:])
        return all(c.islower() for c in word)
