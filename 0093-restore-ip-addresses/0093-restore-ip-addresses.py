class Solution:
    def is_valid_integer(self, s: str) -> bool:
        if (len(s) > 1) and (s[0] == "0"):
            return False  # no trailing zeros
        if not(s.isnumeric()):
            return False
        if int(s) >= 256:
            return False
        return True
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []
        n = len(s)
        res = []

        # recursive function
        def recSearch(s: str, i: int, address: List[str]) -> None:
            nonlocal res
            if len(address) == 3:
                if self.is_valid_integer(s[i:]):
                    res.append(address + [f".{s[i:]}"])
                return None

            for j in range(i, n):
                if self.is_valid_integer(s[i:j+1]):
                    recSearch(s, j + 1, address + [f".{s[i:j+1]}"])

        recSearch(s, 0, [])
        return ["".join(address)[1:] for address in res]
