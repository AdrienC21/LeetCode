class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int freq1[26] = {};
        int freq2[26] = {};
        for (auto &c : ransomNote) {
            freq1[c - 'a'] += 1;
        }
        for (auto &c : magazine) {
            freq2[c - 'a'] += 1;
        }
        for (int i=0; i<26; i++) {
            if (freq1[i] > freq2[i]) {
                return false;
            }
        }
        return true;
    }
};