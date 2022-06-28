class Solution {
public:
    int minDeletions(string s) {
        std::unordered_map<char, int> freq;  // frequency of each letter
        char c;
        for (int i=0; i<s.length(); i++) {
            c = s[i];
            if (freq.find(c) == freq.end()) {
                freq.insert({c, 0});
            }
            freq[c] += 1;
        }
        std::unordered_map<int, int> count;  // number of letters per frequence
        
        int f;
        for (auto& it: freq) {
            f = it.second;
            if (count.find(f) == count.end()) {
                count.insert({f, 0});
            }
            count[f] += 1;
        }

        bool double_frequencies = true;
        int number_deletions = 0;
        while (double_frequencies) {
            double_frequencies = false;
            for (auto& it: count) {
                f = it.first;
                if ((f != 0) and (count[f] >= 2)) {
                    double_frequencies = true;
                    number_deletions += (count[f] - 1);
                    count[f-1] += (count[f] - 1);
                    count[f] = 1;
                }
            }
        }
        return number_deletions;
    }
};