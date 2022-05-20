from collections import defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        lenFormula = len(formula)
        def recAtoms(s):
            lens = len(s)
            if not(s):
                return defaultdict(int)
            if s[0] == "(":
                i = 1
                count = 1  # count parenthesis
                while count != 0:
                    if s[i] == "(":
                        count += 1
                    elif s[i] == ")":
                        count -= 1
                        if count == 0:
                            break
                    i += 1
                f = recAtoms(s[1:i])
                i += 1
                if (i == lens) or not(s[i].isdigit()):  # factor=1
                    factor = 1
                    j = i  # to process the rest of the molecule
                else:
                    j = i + 1
                    while (j < lens) and s[j].isdigit():
                        j += 1
                    factor = int(s[i:j])
                if factor != 1:
                    for key in f:
                        f[key] *= factor
                # rest of the molecule
                f_next = recAtoms(s[j:])
                for key in f:
                    f_next[key] += f[key]
                return f_next
            if lens == 1:
                f = defaultdict(int)
                f[s[0]] = 1
                return f
            j = 1
            while (j < lens) and (s[j].islower()):
                j += 1
            if j == lens:  # no number + reach the end
                f = defaultdict(int)
                f[s] = 1
                return f
            if s[j].isdigit():  # there is a number
                atom = s[:j]
                k = j + 1
                while (k < lens) and (s[k].isdigit()):
                    k += 1
                factor = int(s[j:k])
                f_next = recAtoms(s[k:])
                f_next[atom] += factor
                return f_next
            # else, no number
            atom = s[:j]
            f_next = recAtoms(s[j:])
            f_next[atom] += 1
            return f_next

        final = list(recAtoms(formula).items())
        # sort the dic by letter
        final.sort(key=lambda x: x[0])
        res = []
        for (atom, count) in final:
            if count == 1:
                res.append(str(atom))
            else:
                res.append(f"{atom}{count}")
        
        return "".join(res)