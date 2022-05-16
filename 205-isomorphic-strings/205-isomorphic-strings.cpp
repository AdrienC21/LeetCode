class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> hashmap;
        unordered_set<char> hashset_rev;  // set of seen letters in t
        int n_s = s.length();
        int n_t = t.length();
        if (n_s != n_t) {
            return false;
        }
        for (int i=0; i<n_s; i++) {
            char c1 = s[i];
            char c2 = t[i];
            if (hashmap.find(c1) != hashmap.end()) {  // found c1
                if (hashmap[c1] != c2) {  // c1 has already been paired
                    return false;
                }
            }
            else {
                if (hashset_rev.find(c2) != hashset_rev.end()) {  // found c2
                    return false;
                }
                hashset_rev.insert(c2);
                hashmap[c1] = c2;
            }
        }
        return true;
    }
};