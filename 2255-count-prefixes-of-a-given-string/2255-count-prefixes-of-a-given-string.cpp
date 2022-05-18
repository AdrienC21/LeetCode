class Solution {
public:
    bool isPrefix(string word, string s) {
        int n = word.length();
        if (n > s.length()) {
            return false;
        }
        for (int i=0; i<n; i++) {
            if (word[i] != s[i]) {
                return false;
            }
        }
        return true;
    }
public:
    int countPrefixes(vector<string>& words, string s) {
        int count = 0;
        int wordsSize = words.size();
        string word;
        for (int i=0; i<wordsSize; i++) {
            word = words[i];
            if (this->isPrefix(word, s)) {
                count++;
            }
        }
        return count;
    }
};