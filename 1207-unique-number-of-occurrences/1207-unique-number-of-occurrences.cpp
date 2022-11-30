class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int,int> freq;
        for (auto & n : arr) {
            if (freq.find(n) == freq.end()) {
                freq[n] = 0;
            }
            freq[n]++;
        }
        unordered_set<int> s;
        for (auto v : freq) {
            if (s.find(v.second) != s.end()) {
                return false;
            }
            s.insert(v.second);
        }
        return true;
    }
};