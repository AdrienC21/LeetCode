class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        int n1 = word1.size();
        int n2 = word2.size();
        int i = 0;
        int j = 0;
        int leni = word1[0].length();
        int lenj = word2[0].length();
        int ki = 0;
        int kj = 0;
        while ((i < n1) & (j < n2)) {
            if (word1[i][ki] != word2[j][kj]) {
                return false;
            }
            ki++;
            if (ki == leni) {
                ki = 0;
                i++;
                if (i < n1) {
                    leni = word1[i].length();
                }
            }
            kj++;
            if (kj == lenj) {
                kj = 0;
                j++;
                if (j < n2) {
                    lenj = word2[j].length();
                }
            }
        }
        return ((i == n1) & (j == n2));
    }
};