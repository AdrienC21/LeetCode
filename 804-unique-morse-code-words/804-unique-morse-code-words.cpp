class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        std::array<string, 26> tab = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        unordered_set<string> transfo;
        for (auto &w : words) {
            vector<string> t;
            for (auto &c : w) {
                t.push_back(tab[(int)c - (int)'a']);
            }
            std::string s;
            for (auto & t_s : t) {
                s += t_s;
            }
            transfo.insert(s);
        }
        return transfo.size();
    }
};
