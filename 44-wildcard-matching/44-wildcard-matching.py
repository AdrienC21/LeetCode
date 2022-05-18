class Solution:
    # Pointers on the pattern, the string and the stars!
    def isMatch(self, s: str, p: str) -> bool:
        lenp = len(p)
        lens = len(s)
        s_id = 0  # pointer on the string
        p_id = 0  # pointer on the pattert!
        match = 0  # pointer on s when we found star on p
        star_id = -1  # pointer on star
        while (s_id < lens):
            # ? or same character: move both pointers
            if (p_id < lenp) and (p[p_id] == "?" or s[s_id] == p[p_id]):
                s_id += 1
                p_id += 1
            # *, move only pattern pointer
            elif (p_id < lenp) and (p[p_id] == "*"):
                star_id = p_id
                match = s_id
                p_id += 1
            # there is no match, last pattern pointer was *:
            # go back to the pattern after the star & increase the string pointer
            elif (star_id != -1):
                p_id = star_id + 1
                match += 1
                s_id = match
            # pattern pointer is not * and we reached the end of p
            else:
                return False

        # if there are still characters in the pattern p, move pointer
        while (p_id < lenp) and (p[p_id] == "*"):
            p_id += 1
        # if string and pattern pointers reached the end, it's a match
        return (p_id == lenp)
    # Recursive solution (time limit exceeded on very long strings)
    """
    def recMatch(self, s: str, p: str) -> bool:
        # s empty
        if not(s):
            return not(p) or (p == "*")
        # p empty
        if not(p):
            return (s == "")
        # p len 1
        if len(p) == 1:  # p len 1
            if p == "*":
                return True
            if p == "?":
                return (len(s) == 1)
            if len(s) == 1:
                return (s == p)
            return False
        # p larger
        # first letter
        if p[0] == "?":
            return self.recMatch(s[1:], p[1:])
        if p[0] != "*":
            if p[0] != s[0]:
                return False
            return self.recMatch(s[1:], p[1:])
        # last letter
        if p[-1] == "?":
            return self.recMatch(s[:-1], p[:-1])
        if p[-1] != "*":
            if p[-1] != s[-1]:
                return False
            return self.recMatch(s[:-1], p[:-1])
        
        # last case, two * at the beginning and the end of p
        if self.recMatch("", p[1:-1]):
            return True
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if self.recMatch(s[i:j], p[1:-1]):
                    return True
        return False
    def isMatch(self, s: str, p: str) -> bool:
        # remove first multiple * in a row
        new_p = []
        i = 0
        while i < len(p):
            if p[i] != "*":
                new_p.append(p[i])
                i += 1
            else:
                new_p.append("*")
                j = i + 1
                while (j < len(p)) and (p[j] == "*"):
                    j += 1
                i = j
        new_p = "".join(new_p)
        return self.recMatch(s, new_p)
    """
