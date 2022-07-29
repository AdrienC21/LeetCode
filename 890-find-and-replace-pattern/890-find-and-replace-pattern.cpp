class Solution {
public:
    bool isSamePattern(string word, string pattern) {
        map<char, char> dic;
        map<char, char> inverse_dic;
        char c;
        for (int i=0; i<word.length(); i++) {
            c = word[i];
            if (dic.find(c) != dic.end()) {
                if (dic[c] != pattern[i]) {
                    return false;
                }
            }
            else {
                if (inverse_dic.find(pattern[i]) != inverse_dic.end()) {
                    if (inverse_dic[pattern[i]] != c) {
                        return false;
                    }
                }
                else {
                    dic[c] = pattern[i];
                    inverse_dic[pattern[i]] = c;
                }
            }
        }
        return true;
    }
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        vector<string> res;
        for (auto const& w : words) {
            if (this->isSamePattern(w, pattern)) {
                res.push_back(w);
            }
        }
        return res;
    }
};