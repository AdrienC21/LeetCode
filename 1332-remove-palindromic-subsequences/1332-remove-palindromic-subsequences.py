class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not(s):
            return 0
        if s == s[::-1]:
            return 1
        return 2
    # problem not well formulated ...
    """
    def removePalindromeSub(self, s: str) -> int:
        count = 0
        while s:
            n = len(s)
            max_radii = -1
            max_radii_pos = 0
            max_radii_even = False
            for i in range(n):
                radii = 0
                for j in range(1, min(i+1, n-i)):
                    if s[i+j] == s[i-j]:
                        radii += 1
                    else:
                        break
                if radii > max_radii:
                    max_radii = radii
                    max_radii_pos = i
            for i in range(n-1):
                if s[i] == s[i+1]:
                    radii = 1
                    for j in range(1, min(i+1, n-i-1)):
                        if s[i+1+j] == s[i-j]:
                            radii += 1
                        else:
                            break
                    
                    if radii > max_radii:
                        max_radii = radii
                        max_radii_pos = i
                        max_radii_even = True
            if max_radii_even:
                s = s[:max_radii_pos-(max_radii-1)] + s[max_radii_pos+max_radii+1:]
            else:
                s = s[:max_radii_pos-max_radii] + s[max_radii_pos+max_radii+1:]
            count += 1
        return count
    """
