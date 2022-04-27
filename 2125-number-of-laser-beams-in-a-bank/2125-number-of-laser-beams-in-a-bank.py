class Solution:
    def sumString(self, s: str) -> int:
        res = 0
        for v in s:
            if v == "1":
                res += 1
        return res
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prevNbDevices = None
        for i, row in enumerate(bank):
            s = self.sumString(row)
            if s != 0:
                if prevNbDevices is None:
                    prevNbDevices = s
                else:
                    res += s * prevNbDevices
                    prevNbDevices = s
        return res