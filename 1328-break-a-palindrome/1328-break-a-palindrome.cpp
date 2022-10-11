class Solution {
public:
    string breakPalindrome(string palindrome) {
        int n = palindrome.length();
        if (n == 1) {
            string res;
            return res;
        }
        vector<char> p;
        for (int i=0; i<n; i++) {
            p.push_back(palindrome[i]);
        }
        for (int i=0; i<(n/2); i++) {
            if (palindrome[i] != 'a') {
                palindrome[i] = 'a';
                string res;
                for (int i=0; i<n; i++) {
                    res += palindrome[i];
                }
                return res;
            }
        }
        char last_char = (int)palindrome[n-1] + 1;
        palindrome[n-1] = last_char;
        string res;
        for (int i=0; i<n; i++) {
            res += palindrome[i];
        }
        return res;
    }
};