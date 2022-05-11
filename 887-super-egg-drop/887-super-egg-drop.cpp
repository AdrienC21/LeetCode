class Solution {
    // prettier and optimal solution from justforonce (1D dynamic programming)
    // O(klogn) time, O(k) time
    
    // idea, rephrase in how many floors can we cover in m moves with k eggs
    // dp[m][k] = dp[m - 1][k - 1] + 1 (egg break, so k-1 and we add one) + dp[m - 1][k] (egg survive)
public:
    int superEggDrop(int k, int n) {
        int m = 0;
        vector<int> dp;
        for (int i=0; i<(k+1); i++) {
            dp.push_back(0);
        }
        while (dp[k] < n) {
            m++;
            for (int i=k; i>0; i--) {
                dp[i] = dp[i] + dp[i-1] + 1;
            }
        }
        return m;
    }
};