class Solution:
    def isValid(self, s: str) -> bool:
        L = []
        count_p = 0
        count_c = 0
        count_b = 0
        for v in s:
            if v == "(":
                L.append("(")
                count_p += 1
            elif v == "{":
                L.append("{")
                count_c += 1
            elif v == "[":
                L.append("[")
                count_b += 1
            elif v == ")":
                if not(L and (L.pop() == "(")):
                    return False
                count_p -= 1
            elif v == "}":
                if not(L and (L.pop() == "{")):
                    return False
                count_c -= 1
            else:  # ]
                if not(L and (L.pop() == "[")):
                    return False
                count_b -= 1
        return (count_p == 0) and (count_c == 0) and (count_b == 0)
