class Solution {
public:
    // another approach, take into account the fact that there is only 26 letters
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        int n = s.length();
        int counts[26] = {0};
        for (int i = 0; i < n; i++) {
            counts[s[i] - 'a']++;
            counts[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (counts[i] != 0) {
                return false;
            }
        }
        return true;
    }
    // works, but slower!
    /*
    bool isAnagram(string s, string t) {
        map<char, int> h1;
        map<char, int> h2;
        for (auto &c : s) {
            if (h1.find(c) != h1.end()) {
                h1[c] += 1;
            }
            else {
                h1[c] = 1;
            }
        }
        for (auto &c : t) {
            if (h2.find(c) != h2.end()) {
                h2[c] += 1;
            }
            else {
                h2[c] = 1;
            }
        }
        if (h1.size() != h2.size()) {
            return false;
        }
        for (auto const& x : h1) {
            if (h2.find(x.first) == h2.end()) {  // letter in s not in t
                return false;
            }
            if (h2[x.first] != x.second) {  // not same amount of letter
                return false;
            }
        }
        return true;
    }
    */
};