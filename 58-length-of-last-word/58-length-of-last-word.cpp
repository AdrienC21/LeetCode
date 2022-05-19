class Solution {
public:
    int lengthOfLastWord(string s) {
        int n = s.length();
        int j = n - 1;
        while ((j >= 0) and (s[j] == ' ')) {
            j--;
        }
        int i = j;
        while ((i >= 0) and (s[i] != ' ')) {
            i--;
        }
        if (i < 0) {
            return j + 1;
        }
        return j - i;
    }
};