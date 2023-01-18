#include <numeric>

class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int tot_sum = std::accumulate(nums.begin(), nums.end(), 0);
        int current_min = 0;  // min running sum
        int current_max = 0;
        int tot_min = INT_MAX;  // min of all running sum
        int tot_max = INT_MIN;

        for (auto &n : nums) {
            current_min = std::min(current_min + n, n);
            current_max = std::max(current_max + n, n);
            tot_min = std::min(tot_min, current_min);
            tot_max = std::max(tot_max, current_max);
        }
        
        if (tot_max <= 0) {
            return tot_max;
        }
        return std::max(tot_max, tot_sum - tot_min);
    }
};