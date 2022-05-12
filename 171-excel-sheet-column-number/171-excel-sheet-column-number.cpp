class Solution {
public:
    int titleToNumber(string columnTitle) {
        long long res = 0;
        long long pow_26 = 1;
        char c;
        for (int i=(columnTitle.length()-1); i>-1; i--) {
            c = columnTitle[i];
            res += ((c - 'A') + 1) * pow_26;
            pow_26 *= 26;
        }
        return res;
    }
};
