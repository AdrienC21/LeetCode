class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        Ls = []
        Lt = []
        for c in s:
            if c == "#":
                if Ls:
                    Ls.pop()
            else:
                Ls.append(c)
        for c in t:
            if c == "#":
                if Lt:
                    Lt.pop()
            else:
                Lt.append(c)
        return Ls == Lt