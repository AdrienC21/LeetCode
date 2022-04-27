class Solution:
    def checkString(self, s: str) -> bool:
        b_found = False
        for v in s:
            if b_found:
                if v == "a":
                    return False                
            else:
                if v == "b":
                    b_found = True
        return True