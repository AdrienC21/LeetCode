class Solution {
public:
    string reverseVowels(string s) {
        vector<char> L;
        for (auto &c : s) {
            L.push_back(c);
        }
        int i = 0;
        int j = L.size() - 1;
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        while (i < j) {
            if (vowels.find(L[i]) == vowels.end()) {
                i++;
            }
            else if (vowels.find(L[j]) == vowels.end()) {
                j--;
            }
            else {
                char temp = L[i];
                L[i] = L[j];
                L[j] = temp;
                i++;
                j--;
            }
        }
        string res;
        for (auto &c : L) {
            res += c;
        }
        return res;
    }
};
