class Solution {
public:
    bool checkIfPangram(string sentence) {
        unordered_set<char> s;
        for (auto &c : sentence) {
            s.insert(c);
            if (s.size() == 26) {
                return true;
            }
        }
        return false;
    }
};