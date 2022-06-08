class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int N = nums.size();
        int res = 0;
        int n;  // when iterate nums later
        for (int i=31; i>=0; i--) {
            int mask = 1 << i;
            int ones = 0;
            for (int k=0; k<N; k++) {
                n = nums[k];
                if (n & mask) {
                    ones++;
                }
            }
            int zeros = N - ones;
            res += zeros * ones;
        }
        return res;
    }
};