class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        if (n <= 1) {
            return n;
        }
        int longest_sub_string = 1;
        
        // store the current substring (start at first character)
        int current_streak = 1;
        unordered_set<char> _set;
        _set.insert(s[0]);
        
        int start = 0;  // start of substring
        int i = 1;  // current pointer
        while (i < n) {
            if (s[i] == s[i-1]) {  // repeating character, we update the longest sub string and we search another one starting from i
                longest_sub_string = max(longest_sub_string, current_streak);
                current_streak = 1;
                _set.clear();
                _set.insert(s[i]);
                start = i;
            }
            else {
                if (_set.find(s[i]) != _set.end()) {  // repeating character, update max, start new streak at j+1 where j such that s[i] == s[j]
                    longest_sub_string = max(longest_sub_string, current_streak);
                    for (int j=start; j<i; j++) {
                        if (s[j] == s[i]) {
                            start = j + 1;
                            break;
                        }
                        else {  // remove the character (between start and j)
                            _set.erase(s[j]);
                            current_streak--;
                        }
                    }
                }
                else {
                    current_streak++;
                    _set.insert(s[i]);
                }
            }
            i++;
        }
        // update the max one last time
        longest_sub_string = max(longest_sub_string, current_streak);
        return longest_sub_string;
    }
};