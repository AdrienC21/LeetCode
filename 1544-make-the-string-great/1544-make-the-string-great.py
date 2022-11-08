class Solution:
    def makeGood(self, s: str) -> str:
        d = []
        for i in range(len(s)):
            if d and ((d[-1].islower() and s[i].isupper() and d[-1] == s[i].lower()) or (d[-1].isupper() and s[i].islower() and d[-1].lower() == s[i])):
                d.pop()
            else:
                d.append(s[i])
        return "".join(d)
