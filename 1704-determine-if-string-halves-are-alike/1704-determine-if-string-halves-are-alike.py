class Solution:
    def __init__(self):
        self.vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        for i in range(len(s)//2):
            count += 1 if s[i] in self.vowels else 0
        for i in range(len(s)//2):
            count -= 1 if s[-(i+1)] in self.vowels else 0
            if count < 0:
                return False
        return not(count)
