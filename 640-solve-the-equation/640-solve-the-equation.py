class Solution:
    def process(self, s: str):
        nb_x = 0
        res = 0
        i = 0
        len_s = len(s)
        while i < len_s:
            j = i + 1
            while (j < len_s) and (s[j] != "+") and (s[j] != "-"):  # don't stop until end the string or a new sign appear
                j += 1
            sign = 1 if s[i] == "+" else -1
            if s[j-1] == "x":  # update number of x
                nb_x += sign * int(s[i+1:j-1])
            else:  # update number
                res += sign * int(s[i+1:j])
            i = j
        return nb_x, res
            
            
    def solveEquation(self, equation: str) -> str:
        L1, L2 = equation.split("=")
        # preprocess
        if L1[0] not in ["+", "-"]:
            L1 = "+" + L1
        if L2[0] not in ["+", "-"]:
            L2 = "+" + L2
        L1 = L1.replace("+x", "+1x").replace("-x", "-1x")
        L2 = L2.replace("+x", "+1x").replace("-x", "-1x")
        nb_x_l1, res_l1 = self.process(L1)
        nb_x_l2, res_l2 = self.process(L2)
        
        nb_x = nb_x_l1 - nb_x_l2
        res = res_l2 - res_l1
        
        if nb_x:
            return f"x={res//nb_x}"
        else:
            if res:
                return "No solution"
            else:
                return "Infinite solutions"
