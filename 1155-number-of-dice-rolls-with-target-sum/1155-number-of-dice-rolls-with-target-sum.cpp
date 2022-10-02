class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        // target+1 x nb dice matrix, dynamic programming
        vector<vector<int>> dp;
        for (int i=0; i<n; i++) {
            vector<int> sub_dp;
            for (int j=0; j<(target+1); j++) {
                sub_dp.push_back(0);
            }
            dp.push_back(sub_dp);
        }
        dp[0][0] = 0;  // no target 0 with 1 dice
        
        int mod = (int) (pow(10, 9) + 7);
        
        for (int i=1; i<(target+1); i++) {
            // 1 if target lower or equal than max dice value
            if (i > k) {
                dp[0][i] = 0;
            }
            else {
                dp[0][i] = 1;
            }
        }
        for (int j=1; j<n; j++) {
            for (int i=0; i<(target+1); i++) {
                for (int dice=1; dice<std::min(k+1, i+1); dice++) {
                    dp[j][i] += dp[j-1][i-dice];
                    dp[j][i] = dp[j][i] % mod;
                }
            }
        }
        return dp[n-1][target] % mod;
    }
};