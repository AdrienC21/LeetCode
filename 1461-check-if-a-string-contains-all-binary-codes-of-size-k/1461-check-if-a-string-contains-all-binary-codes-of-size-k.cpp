class Solution {
public:
    bool hasAllCodes(string s, int k) {
        unordered_set<string> seen;
        int n = s.length();
        for (int i=(k-1); i<n; i++) {
            seen.insert(s.substr(i-k+1,k));
        }
        return (seen.size() == ((int) pow(2, k)));
    }
};