class Solution {
public:
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        int n = nums.size();
        int m = multipliers.size();
        vector<vector<int>> dp;
        for (int i=0; i<(m+1); i++) {
            vector<int> sub_dp;
            for (int j=0; j<(m+1); j++) {
                sub_dp.push_back(0);
            }
            dp.push_back(sub_dp);
        }
        int score = INT_MIN;
        int res_left;
        int res_right;
        for (int k=1; k<(m+1); k++) {
            for (int l=0; l<(k+1); l++) {
                if (l == 0) {
                    res_left = INT_MIN;
                }
                else {
                    res_left = dp[l-1][k-l] + multipliers[k-1] * nums[l-1];
                }
                if (l == k) {
                    res_right = INT_MIN;
                }
                else {
                    res_right = dp[l][k-l-1] + multipliers[k-1] * nums[n-k+l];
                }
                dp[l][k-l] = std::max(res_left, res_right);

                if (k == m) {
                    score = std::max(score, dp[l][k-l]);
                }
            }
        }
        return score;
    }
};