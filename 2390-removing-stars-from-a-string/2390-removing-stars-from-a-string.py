class Solution:
    def removeStars(self, s: str) -> str:
        L = []
        for c in s:
            if c == '*':
                L.pop()
            else:
                L.append(c)
        return "".join(L)
