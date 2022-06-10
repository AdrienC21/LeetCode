class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        longest_sub_string = 1
        
        # store the current substring (start at first character)
        current_streak = 1
        _set = set()
        _set.add(s[0])
        
        n = len(s)
        start = 0  # start of substring
        i = 1  # current pointer
        while i < n:
            if s[i] == s[i-1]:  # repeating character, we update the longest sub string and we search another one starting from i
                longest_sub_string = max(longest_sub_string, current_streak)
                current_streak = 1
                _set.clear()
                _set.add(s[i])
                start = i
                
            elif s[i] in _set:  # repeating character, update max, start new streak at j+1 where j such that s[i] == s[j]
                longest_sub_string = max(longest_sub_string, current_streak)
                for j in range(start, i):
                    if s[j] == s[i]:
                        start = j + 1
                        break
                    else:  # remove the character (between start and j)
                        _set.discard(s[j])
                        current_streak -= 1
                
            else:
                current_streak += 1
                _set.add(s[i])
            
            i += 1
        
        # update the max one last time
        longest_sub_string = max(longest_sub_string, current_streak)
        return longest_sub_string