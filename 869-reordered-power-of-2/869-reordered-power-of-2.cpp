class Solution {
public:
    vector<unordered_map<char, int>> counters;
    
    unordered_map<char, int> Counter(string s) {
        unordered_map<char, int> res;
        for (auto &c : s) {
            if (res.find(c) == res.end()) {
                res[c] = 0;
            }
            res[c] += 1;
        }
        return res;
    }
    
    Solution() {
        int power = 1;
        for (int i=0; i<30; i++) {  // 2**29 < 10**9 < 2**30
            unordered_map<char, int> c = this->Counter(std::to_string(power));
            this->counters.push_back(c);
            power *= 2;
        }
    }
    
    bool counters_equal(unordered_map<char, int> c1, unordered_map<char, int> c2) {
        if (c1.size() != c2.size()) {  // not same number of keys
            return false;
        }
        for (auto &it : c1) {
            if (c2.find(it.first) == c2.end()) {  // key not in c2
                return false;
            }
            if (it.second != c2[it.first]) {  // not same number of digit c
                return false;
            }
        }
        return true;
    }
    
    bool reorderedPowerOf2(int n) {
        unordered_map<char, int> n_c = this->Counter(std::to_string(n));
        for (auto &c : this->counters) {
            if (this->counters_equal(n_c, c)) {
                return true;
            }
        }
        return false;
    }
};