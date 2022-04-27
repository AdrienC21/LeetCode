class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        tot_count = 0
        list_of_candidates_p = []
        list_of_candidates_f = []
        for i, v in enumerate(s):
            if v == "(":
                if tot_count >= 0:
                    tot_count += 1
                    list_of_candidates_p.append(i)
            elif v == ")":
                if tot_count == 0:
                    list_of_candidates_f.append(i)
                else:
                    tot_count -= 1
                    list_of_candidates_p.pop(-1)
        new_s = list(s)
        for j in list_of_candidates_p:
            new_s[j] = "X"
        for j in list_of_candidates_f:
            new_s[j] = "X"
        new_s = "".join(new_s)
        return new_s.replace("X", "")