class Solution {
public:
    std::tuple<int, vector<vector<int>>> recSearch(int i, int j, vector<vector<int>> dp, int m, int n) {
        if (dp[i][j] != -1) {
            return std::make_tuple(dp[i][j], dp);
        }
        int sub_res = 0;
        int sub_sub_res;
        if (i < (m-1)) {  // can go down
            tie(sub_sub_res, dp) = this->recSearch(i+1, j, dp, m, n);
            sub_res += sub_sub_res;
        }
        if (j < (n-1)) {  // can go right
            tie(sub_sub_res, dp) = this->recSearch(i, j+1, dp, m, n);
            sub_res += sub_sub_res;
        }
        dp[i][j] = sub_res;
        return std::make_tuple(sub_res, dp);
    }
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp;
        for (int i=0; i<m; i++) {
            vector<int> row;
            for (int j=0; j<n; j++) {
                row.push_back(-1);
            }
            dp.push_back(row);
        }
        for (int i=0; i<m; i++) {
            dp[i][n-1] = 1;
        }
        for (int j=0; j<n; j++) {
            dp[m-1][j] = 1;
        }
        int res;
        tie(res, dp) = this->recSearch(0, 0, dp, m, n);
        return res;
    }
};