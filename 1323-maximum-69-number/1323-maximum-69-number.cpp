#include <string> 
class Solution {
public:
    int maximum69Number (int num) {
        int i = 0;
        auto s = std::to_string(num);
        int n = s.length();
        while ((i < n) & (s[i] == '9')) {
            i++;
        }
        if (i == n) {
            return num;  // only 9s
        }
        string s2 = s.substr(0, i) + "9" + s.substr(i+1);
        return stoi(s2);  // replace the leftmost 6 by a 9
    }
};