class Solution:
    def isPal(self, s: str) -> bool:
        if s == s[::-1]:
            return True
    def validPalindrome(self, s: str) -> bool:
        if self.isPal(s):
            return True
        for i, _ in enumerate(s):
            if s[i] != s[-(i+1)]:
                if i == 0:
                    return self.isPal(s[:i] + s[i+1:]) or self.isPal(s[:-(i+1)])
                else:
                    return self.isPal(s[:i] + s[i+1:]) or self.isPal(s[:-(i+1)] + s[-i:])
        return False