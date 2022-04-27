class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = s.lower()
        delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
        translation = s.maketrans(delchars, len(delchars) * " ")
        s2 = s2.translate(translation)
        s2 = s2.replace(" ", "")
        return (s2 == s2[::-1])