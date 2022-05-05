class Solution:    
    # Dynamic programming + recursion, time limit exceeded on fff....ffgggg...gggg
    """
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        def recSearch(i, j):
            nonlocal dp
            if dp[i][j] == -1:  # not yet calculated (and so i != j)
                if j == (i+1):
                    if s[i] == s[j]:  # palindrom length 2 (aa, bb, ...)
                        dp[i][j] = 2
                    else:  # no palindrom
                        dp[i][j] = 0
                elif s[i] == s[j]:
                    substring = recSearch(i+1, j-1)
                    if substring > 0:  # it wraps a palindrome, so we create a larger palindrom
                        dp[i][j] = substring + 2
                    else:
                        dp[i][j] = 0
                else:
                    dp[i][j] = 0
            return dp[i][j]
        current_max = 1
        current_max_ids = (0, 0)
        i = 0
        while (i < min((n-1), n-(current_max//2))):
            j = min(i+1, i+(current_max//2))
            while j < n:
                search = recSearch(i, j)
                if search > current_max:
                    current_max = search
                    current_max_ids = (i, j)
                j += 1
            i += 1
        return s[current_max_ids[0]:current_max_ids[1]+1]
    """
    
    # I discovered Manacher's algorithm, here is my implementation
    def longestPalindrome(self, s: str) -> str:

        sp = "|"  # s', s with | characters including boundaries
        # | are necessary for words like "cbbd", the radius are [0, 1, 0, 1, 2, 1, 0, 1, 0]
        # so the maximum is |b|b| with a radius of 2 and we thus capture the palindrome bb
        for c in s:
            sp = sp + c + "|"
        # len(sp) = len(PalindromeRadii) = 2 × len(S) + 1
        
        n = len(s)
        np = 2 * len(s) + 1  # = len(sp)
        PalindromeRadii = [0 for _ in range(np)]  # ri = radius of longest palindrome centered in i
        
        Center = 0
        Radius = 0
        
        while Center < np:
            # At the start of the loop, Radius is already set to a lower-bound for the longest radius.
            # In the first iteration, Radius is 0, but it can be higher.
            # Determine the longest palindrome starting at Center-Radius and going to Center+Radius
            while (Center-(Radius+1) >= 0) and (Center+(Radius+1) < np) and (sp[Center-(Radius+1)] == sp[Center+(Radius+1)]):
                Radius = Radius+1
            
            # Save the radius of the longest palindrome in the array
            PalindromeRadii[Center] = Radius
            
            # Below, Center is incremented.
            # If any precomputed values can be reused, they are.
            # Also, Radius may be set to a value greater than 0
            
            OldCenter = Center
            OldRadius = Radius
            Center = Center+1
            # Radius' default value will be 0, if we reach the end of the following loop. 
            Radius = 0 
            while (Center <= OldCenter + OldRadius):
                # Because Center lies inside the old palindrome and every character inside
                # a palindrome has a "mirrored" character reflected across its center, we
                # can use the data that was precomputed for the Center's mirrored point. 
                MirroredCenter = OldCenter - (Center - OldCenter)
                MaxMirroredRadius = OldCenter + OldRadius - Center
                if PalindromeRadii[MirroredCenter] < MaxMirroredRadius:
                    PalindromeRadii[Center] = PalindromeRadii[MirroredCenter]
                    Center = Center+1
                elif PalindromeRadii[MirroredCenter] > MaxMirroredRadius:
                    PalindromeRadii[Center] = MaxMirroredRadius
                    Center = Center+1
                else:  # PalindromeRadii[MirroredCenter] = MaxMirroredRadius
                    Radius = MaxMirroredRadius
                    break  # exit while loop early     

        max_index = 0
        max_radius = 0
        for i in range(np):
            if PalindromeRadii[i] > max_radius:
                max_index = i
                max_radius = PalindromeRadii[i]
        s = sp[max_index-max_radius:max_index+max_radius+1].replace("|", "")
        return s