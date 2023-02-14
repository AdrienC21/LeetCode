class Solution:
    def recAdd(self, a: list, b: list, r: bool) -> list:
        if not(a) and not(b):
            if r:
                return ["1"]
            return []
        if not(a):
            if not(r):
                return b
            for i in range(len(b)-1, -1, -1):
                if b[i] == "0":
                    return b[:i] + ["1"] + len(b[i+1:]) * ["0"]
            else:
                return ["1"] + len(b) * ["0"]
        if not(b):
            return self.recAdd(b, a, r)
        if (a[-1] == "1") and (b[-1] == "1"):
            c = "1" if r else "0"
            return self.recAdd(a[:-1], b[:-1], True) + [c]
        if (a[-1] == "1") or (b[-1] == "1"):
            if r:
                return self.recAdd(a[:-1], b[:-1], True) + ["0"]
            return self.recAdd(a[:-1], b[:-1], False) + ["1"]
        c = "1" if r else "0"
        return self.recAdd(a[:-1], b[:-1], False) + [c]
            
    def addBinary(self, a: str, b: str) -> str:
        return "".join(self.recAdd(list(a), list(b), False))
