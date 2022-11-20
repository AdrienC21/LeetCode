class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        L = []  # stack store results if parenthesis
        sign = 1
        currentNum = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                currentNum = 0
                while j < len(s) and s[j].isdigit():
                    currentNum = currentNum * 10 + int(s[j])
                    j += 1
                res += sign * currentNum  # update result
                i = j
            elif s[i] == "+":
                sign = 1
                i += 1
            elif s[i] == "-":
                sign = -1
                i += 1
            elif s[i] == "(":
                # put previous result and sign into the stack
                L.append(res)
                L.append(sign)
                res = 0  # reset calculation
                sign = 1
                i += 1
            elif s[i] == ")":
                sign = L.pop()
                prevRes = L.pop()
                res = prevRes + sign * res
                i += 1
            else:
                i += 1
        return res
