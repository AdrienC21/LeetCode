#include <tuple>
class Solution {
public:
    std::tuple<int, vector<vector<int>>> recSearch(int i, int j, vector<vector<int>> dp) {
        if (dp[i][j] != -1) {
            return std::make_tuple(dp[i][j], dp);
        }
        int res = 0;
        int subres;
        for (int k=j; k<5; k++) {
            tie(subres, dp) = recSearch(i-1, k, dp);
            res = res + subres;
        }
        dp[i][j] = res;
        return std::make_tuple(res, dp);
    }
public:
    int countVowelStrings(int n) {
        // dp[i][j], number of word length i+1 that start with vowel j
        // a, e, i, o, u
        vector<vector<int>> dp;
        for (int i=0; i<n; i++) {
            vector<int> vect;
            for (int j=0; j<5; j++) {
                vect.push_back(-1);
            }
            dp.push_back(vect);
        }
        for (int j=0; j<5; j++) {
            dp[0][j] = 1;
        }
        int subres;
        for (int k=0; k<5; k++) {
            tie(subres, dp) = recSearch(n-1, k, dp);
        }
        int sum = 0;
        for (int j=0; j<5; j++) {
            sum = sum + dp[n-1][j];
        }
        return sum;

    }
};